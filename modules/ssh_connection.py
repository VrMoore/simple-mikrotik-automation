import paramiko

def connect_router() -> list[str] :

    username : str = input("Login    : ")
    password : str = input("Password : ")
    host_ip  : str = input("Host IP  : ")

    return [username, password, host_ip]