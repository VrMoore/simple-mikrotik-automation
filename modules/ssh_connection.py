import paramiko

class askUser() :

    def __init__(self) :
        pass

    def main_menu(self) :
        # Default username
        
        username = input("Login     : ")
        password = input("Password  : ")
        ip_host = input("Input your client IP gateway : ")

askUser()