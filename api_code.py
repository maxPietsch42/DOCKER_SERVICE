import starlette.responses
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"Begruessung": "Herzlichen Glückwunsch! Du hast die IP richtig abgetippt und benutzt sogar den richtigen "
                           "port!"}


@app.get("/portainer")
def read_root():
    return {"create volume": "sudo docker volume create portainer_data",
            "create portainer": "sudo docker run -d -p 8000:8000 --name portainer "
                                "--restart=always -v "
                                "/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data "
                                "portainer/portainer-ce:latest" }


@app.get("/docker/commands")
def docker_commands():
    return {"syntax": "sudo docker {command}",
            "run {image}": "startet einen container mit dem angegbenen image",
            "stop {id}": "stoppt den container mit der entsprechenden ID",
            "remove {id}": "entfernt den container mit der entsprechenden ID",
            "ps": "listet laufenden container auf",
            "ps -a": "listet alle container auf",
            "rmi {id}": "entfernt ein image"}


@app.get("/docker/build/commands")
def docker_build_commands():
    return {"command": "sudo docker build -t {NamedesImages} ."}


@app.get("/docker/run/flags")
def docker_run_flags():
    return {"-d": "detach, Container läuft im Hintergrund",
            "-v": "bindet ein Volume an den Container",
            "-e": "Umgebungsvariablen zum voreinstellen des Containers",
            "-p": "Port des Containers im Format HOSTPORT:CONTAINERPORT ",
            "--name": "Name des Containers",
            "--restart": "gibt an wann der container neu gestartet werden soll"}


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
    return open("api_code.py", "r").read()