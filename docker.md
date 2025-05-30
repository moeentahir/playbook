# Docker
## ENTRYPINT vs CMD
First argument to CMD is the program name and rest are the arguments to that program
```
FROM ubuntu

# CMD "command" "arg1" "arg2"
CMD sleep 5
# or
# CMD "sleep" "5"
```

Will start the container with command `sleep 5`
```
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper               # will run as `sleep 5`
docker run ubuntu-sleeper sleep 10      # will run as `sleep 10`. Argument to the run command will replace prgram in CMD
```
If you want the program to be fixed to `sleep` and only pass the sleep seconds as arguments, then the ENTRYPOINT kicks in
```
FROM ubuntu

ENTRYPOINT ["sleep"]
```
To run the above container
```
docker run ubuntu-sleeper 10 # arguments will be apended to the program in ENBRYPOINT as opposed to they were replaced in CMD
```
If you want a default parameters to sleep command, that's when we would combine ENTRYPOINT and CMD
```
FROM ubuntu

ENTRYPOINT ["sleep"]
CMD 5
```
```
docker run ubuntu-sleeper               # will run as `sleep 5`
docker run ubuntu-sleeper 10            # will run as `sleep 10`
```
If you want to change the program for the ENTRYPOINT
```
docker run --entrypint sleep2.0 ubuntu-sleeper 10 # this will run the program as `sleep2.0 10`
```
#### Summary
The ENTRYPOINT specifies a command that will always be executed when the container starts. The CMD specifies arguments that will be fed to the ENTRYPOINT.

If you want to make an image dedicated to a specific command you will use ENTRYPOINT ["/path/dedicated_command"]

Otherwise, if you want to make an image for general purpose, you can leave ENTRYPOINT unspecified and use CMD ["/path/dedicated_command"] as you will be able to override the setting by supplying arguments to docker run.

![Image](images/kubenetes-entrypoint.png)
