
```bash
# encoding files
base64 -i NAME-OF-INPUT-FILE.py -o NAME-OF-OUTPUT-FILE.solution

# decoding file
base64 -i NAME-OF-INPUT-FILE.solution --decode > NAME-OF-OUTPUT-FILE.py

# find and free-up an occupied port
lsof -i tcp:PORT
kill PID1, PID2, ....
```
