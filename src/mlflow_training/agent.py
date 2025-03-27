from langchain.schema import SystemMessage
from langchain_core.messages import HumanMessage
from langchain.tools import BaseTool
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langgraph.graph import END, START, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from typing import Annotated, TypedDict

from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import mlflow.pyfunc


# Create Agent
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


def create_agent_node_with_tools(
    system_message: str,
    tools: list[BaseTool],
):
    model_with_tools = ChatOpenAI(
        model_name="gpt-4o",
        temperature=0.001,
        streaming=True,
    ).bind_tools(tools=tools)

    def call_model(state: AgentState):
        # call model
        messages = [SystemMessage(content=system_message)] + state["messages"]
        response = model_with_tools.invoke(messages)
        return {"messages": response}

    return call_model


def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "END"


def create_graph(system_message: str, tools: list[BaseTool]):

    agent_node = create_agent_node_with_tools(
        system_message=system_message, tools=tools
    )

    tools_node = ToolNode(tools=tools, name="TestCreatorTools", handle_tool_errors=True)

    # create graph
    graph = StateGraph(AgentState)

    # nodes
    graph.add_node("agent", agent_node)
    graph.add_node("tools", tools_node)
    graph.add_edge(START, "agent")
    graph.add_edge("tools", "agent")

    graph.add_conditional_edges(
        "agent", should_continue, {"tools": "tools", "END": END}
    )

    checkpointer = MemorySaver()
    compiled_graph = graph.compile(checkpointer=checkpointer)
    return compiled_graph


class LangGraphWrapper(mlflow.pyfunc.PythonModel):
    def __init__(self, system_message: str, tools: list[BaseTool]):
        # Save the parameters for later use.
        self.system_message = system_message
        self.tools = tools

    def load_context(self, context):
        # This is called when the model is loaded. You can initialize your graph here.
        wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
        self.agent = create_graph(system_message=self.system_message, tools=self.tools)

    def predict(self, context, model_input):

        # Convert input to a dictionary if it's a DataFrame.
        if hasattr(model_input, "iloc"):
            # For now, assume a single row input.
            input_dict = model_input.iloc[0].to_dict()
        else:
            input_dict = model_input

        config = {
            "configurable": {"thread_id": input_dict["session_id"]},
        }

        response = self.agent.invoke(
            input={"messages": HumanMessage(input_dict["query"])}, config=config
        )
        return response["messages"][-1].content
