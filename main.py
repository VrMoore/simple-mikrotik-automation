from modules import hotspot as hotspotC
from modules import system_info as systemC

class Menu() :

    def __init__(self) :
        pass

    def main_menu(self) :
        
        print(f"""
            \n 
            ================================================

                WELCOME TO MIKROTIK AUTOMATION

                Choose option :
                    1. Hotspot Setup
                    2. Blocking Website
                    3. Blocking Time
                       ....
                    9. System Info

            ================================================
            \n
        """)

        ask_user = input("Option : ")
        self.run_selected_opt(option=ask_user)

    def run_selected_opt(self, option : str) :

        if option == '1' :
            run_hotspot = hotspotC.hotspotSetup()
        elif option == '2' :
            print("You choose number 2")
        elif option == '3' :
            print("You choose number 3")
        elif option == '9' :
            run_system_info = systemC.systemMenu()
        else :
            print("Out")


if __name__ == "__main__" :
    run_menu = Menu()
    run_menu.main_menu()
