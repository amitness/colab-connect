import subprocess
from importlib import import_module
import uuid
import subprocess

message = """
- Ready!
- Open VSCode on your laptop and open the command prompt
- Select: 'Remote-Tunnels: Connect to Tunnel' to connect to colab
""".strip()


def start_tunnel() -> None:
    command = "./code tunnel --accept-server-license-terms --random-name"
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    show_outputs = False
    while True:
        line = p.stdout.readline().decode("utf-8")
        if show_outputs:
            print(line.strip())
        if "To grant access to the server" in line:
            print(line.strip())
        if "Open this link" in line:
            print(message)
            print("Logs:")
            show_outputs = True
            line = ""
        if line == "" and p.poll() is not None:
            break
    return None


def run(command: str) -> None:
    process = subprocess.run(command.split())
    if process.returncode == 0:
        print(f"Ran: {command}")


def colabtunnel() -> None:
    print("Mounting Google Drive...")
    drive = import_module("google.colab.drive")
    drive.mount("/content/drive")

    print("Installing python libraries...")
    run("pip3 install --user flake8 black ipywidgets")
    run("pip3 install -U ipykernel")
    run("sudo apt install htop -y")

    print("Installing vscode-cli...")
    run(
        "curl -Lk https://code.visualstudio.com/sha/download?build=stable&os=cli-alpine-x64 --output vscode_cli.tar.gz"
    )
    run("tar -xf vscode_cli.tar.gz")

    print("Starting the tunnel")
    start_tunnel()
