import pickle
import os
import base64

def reveal_flag():
    flag = open('flag.txt', 'r').read()
    flag = flag.strip()
    str_flag = ''
    for c in flag:
        str_flag += str(hex(ord(c))) + ' '
    print(str_flag)

def store_data():
    print("Input your encrypted authentication data for storage:")
    user_input = input("> ")
    try:
        data = base64.b64decode(user_input.encode())
        with open("auth_data.pkl", "wb") as f:
            f.write(data)
        print("Authentication data stored successfully!")
    except Exception as e:
        print(f"Error storing data: {e}")

def load_data():
    if not os.path.exists("auth_data.pkl"):
        print("No authentication data found. Please store your data first.")
        return
    try:
        with open("auth_data.pkl", "rb") as f:
            data = pickle.load(f)
            print("Decoding credentials!")
            print(f"Welcome, {data.get('user', 'unknown')}!")
            if data.get('auth') == 'admin':
                reveal_flag()
    except Exception as e:
        print(f"Error loading data: {e}")

def start_challenge():
    print("""
    ██████╗ ██╗ ██████╗██╗  ██╗██╗     ███████╗   ██╗   ██╗ █████╗ ██╗   ██╗██╗     ████████╗
    ██╔══██╗██║██╔════╝██║ ██╔╝██║     ██╔════╝   ██║   ██║██╔══██╗██║   ██║██║     ╚══██╔══╝
    ██████╔╝██║██║     █████╔╝ ██║     █████╗     ██║   ██║███████║██║   ██║██║        ██║
    ██╔═══╝ ██║██║     ██╔═██╗ ██║     ██╔══╝     ██║   ██║██╔══██║██║   ██║██║        ██║
    ██║     ██║╚██████╗██║  ██╗███████╗███████╗   ╚═████╔═╝██║  ██║╚██████╔╝███████╗   ██║
    ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝

    Welcome to PickleAuth Secure Vault!
    """)

    print("Options:")
    print("1. Store authentication data")
    print("2. Load authentication data")
    print("3. Exit")

    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            store_data()
        elif choice == "2":
            load_data()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    start_challenge()