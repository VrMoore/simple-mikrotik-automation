import paramiko

def connect_router() -> list[str] :
    # Default username
    
    username = input("Login     : ")
    password = input("Password  : ")
    ip_host = input("Input your client IP gateway : ")

    return [username, password, ip_host]

if __name__ == "__main__" :

    connect_router()