## Docker dev
### Build Docker image
```
$ docker build -t funnypress-ws-dev -f Dockerfile.dev .
```
### Launch Docker WS
```
$ docker run --name funnypress-ws-dev -it --rm -p 8000:8000 -v $(pwd)/app:/app funnypress-ws-dev
```