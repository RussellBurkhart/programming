import platform
import socket
import os

def main():
    print("System Info")
    print("--------------")
    print(f"Hostname: {socket.gethostname()}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Machine: {platform.machine()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current directory: {os.getcwd()}")

if __name__ == "__main__":
    main()
