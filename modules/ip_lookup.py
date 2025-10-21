import subprocess

def run_bash() -> None:

    subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "./helpers/ipList.ps1"])

    return None