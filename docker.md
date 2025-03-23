# Docker
## Entry points
### CMD
First argument to CMD is the program name and rest are the arguments to that program
```
FROM ubuntu

# CMD "command" "arg1" "arg2"
CMD sleep 5
# or
# CMD "sleep" "5"
```

Will start the container with command `sleep 5`
