import os

def clear_screen():
    os.system('clear')

def show_menu():
    clear_screen()
    print("\033[96mwelcome to telegrafter!\033[0m")
    print("show massages:\033[92m[1]\033[0m")
    print("send massage:\033[92m[2]\033[0m")
    print("exit:\033[92m[3]\033[0m")
    print("creator:\033[96mAMIR_CRAFTER\033[0m")
def run():
    input("\033[35mpress any key to start...\033[0m")
    while True:
        show_menu()
        choice = input("\033[33mtype your choice:\033[0m")

        if choice == "1":
            os.system("python messages.py")
        elif choice == "2":
            os.system("python send.py")
        elif choice == "0":
            print("\033[32mBye Bye!\033[0m")
            break
        else:
            input("\033[91myour choice is wrong!\033[0m")

run()
