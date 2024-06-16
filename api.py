from fastapi import FastAPI

app = FastAPI()


# Fehler extra eingebaut lassen? lul
@app.get("/portainer")
def read_root():
    return {"create volume": "sudo docker volume create portainer_data",
            "create portainer": "sudo docker run -d -p 9001:9001 --name portainer "
                                "--restart=always -v "
                                "/var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data "
                                "portainer/portainer-ce:latest" }


#
@app.get("/portainer/connect")
def portainer_connect():
    return {}


@app.get("/docker/commands")
def docker_commands():
    return {"stop": "sudo docker stop {id}",
            "remove": "sudo docker rm {id}"}
