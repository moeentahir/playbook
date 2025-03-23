# Docker
## Entry points
```
FROM ubuntu

CMD sleep 5
```
is same as
```
FROM ubuntu

CMD "sleep" "5"
```
This will start the container and run the program as `sleep 5`
