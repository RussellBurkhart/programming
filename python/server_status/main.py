import os
import subprocess

def get_uptime():
    return subprocess.getoutput("uptime -p")

def get_disk():
    return subprocess.getoutput("df -h /")

def get_memory():
    return subprocess.getoutput("free -h")

def get_podman():
    output = subprocess.getoutput('podman ps --format "{{.Names}}: {{.Status}}"')
    return output if output.strip() else "No running containers"

def main():
    print("Server Status")
    print("----------------")

    print("\nUptime: ")
    print(get_uptime())

    print("\n\nDisk Usage: ")
    print(get_disk())

    print("\n\nMemory: ")
    print(get_memory())

    print("\n\nContainers:\n")
    print(get_podman())

if __name__ == "__main__":
    main()
