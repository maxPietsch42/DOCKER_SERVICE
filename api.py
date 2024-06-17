import starlette.responses #Braucht ihr nicht
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"begruessung": "Herzlichen glückwunsch du hast die IP richtig abgetippt und sogar den richtigen port "
                           "benutzt"}


@app.get("/portainer")
def read_root():
    return {"create volume": "sudo docker volume create portainer_data",
            "create portainer": "sudo docker run -d -p 8000:8000 --name portainer "
                                "--restart=always -v "
                                "/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data "
                                "portainer/portainer-ce:latest" }


@app.get("/docker/run/commands")
def docker_commands():
    return {"stop": "sudo docker stop {id}",
            "remove": "sudo docker rm {id}",
            "ps": "listet laufenden container auf",
            "ps -a": "listet alle container auf"}


@app.get("/docker/flags")
def docker_flags():
    return {"-d": "detach, Container läuft im Hintergrund",
            "-v": "bindet ein Volume an den Container",
            "-e": "Umgebungsvariablen zum voreinstellen des Containers",
            "-p": "Port des Containers im Format HOSTPORT:CONTAINERPORT "}

@app.get("")

@app.get("/source", response_class=starlette.responses.PlainTextResponse)
def source():
    return open("api.py", "r").read()


#docker file name ändern
@app.get("/dockerfile", response_class=starlette.responses.PlainTextResponse)
def dockerffilee():
    return open("Dockerfile", "r").read()

