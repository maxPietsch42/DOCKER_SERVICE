import starlette.responses #Braucht ihr nicht
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"begruessung": "Herzlichen Glückwunsch! Du hast die IP richtig abgetippt und benutzt sogar den richtigen "
                           "port"}


@app.get("/portainer")
def read_root():
    return {"create volume": "sudo docker volume create portainer_data",
            "create portainer": "sudo docker run -d -p 8000:8000 --name portainer "
                                "--restart=always -v "
                                "/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data "
                                "portainer/portainer-ce:latest" }


@app.get("/docker/run/commands")
def docker_run_commands():
    return {"stop": "sudo docker stop {id}",
            "remove": "sudo docker rm {id}",
            "ps": "listet laufenden container auf",
            "ps -a": "listet alle container auf"}


@app.get("/docker/build/commands")
def docker_build_commands():
    return {"command": "sudo docker build -t {NamedesImages} ."}


@app.get("/docker/flags")
def docker_flags():
    return {"-d": "detach, Container läuft im Hintergrund",
            "-v": "bindet ein Volume an den Container",
            "-e": "Umgebungsvariablen zum voreinstellen des Containers",
            "-p": "Port des Containers im Format HOSTPORT:CONTAINERPORT "}


@app.get("/docker/dockerfile")
def docker_dockerfile():
    return {"FROM {image}": "Gibt das Basis-Image an, von dem das neue Image abgeleitet wird",
            "RUN {command}": "Führt Befehle innerhalb des Containers aus, um die Umgebung einzurichten",
            "COPY {quelle} {ziel}": "Kopiert Dateien oder Verzeichnisse vom Host-Dateisystem in das Image",
            "WORKDIR {pfad/des/arbeitsverzeichnisses}": "Arbeitsverzeichnis in welchem gearbeitet wird",
            "CMD {['python','app.py']}": "Befehle zum ausführen einer Anwendung",
            "EXPOSE {port}": "Port unter welchem die Anwendung laufen soll"}


@app.get("/requirements", response_class=starlette.responses.PlainTextResponse)
def requirements():
    return "fastapi\nuvicorn"


@app.get("/source", response_class=starlette.responses.PlainTextResponse)
def source():
    return open("api.py", "r").read()