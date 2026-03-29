#!/usr/bin/env python3
import os
import argparse
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
    parser = argparse.ArgumentParser(description="Server status CLI tool")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--uptime", action="store_true", help="Show uptime only")
    parser.add_argument("--disk", action="store_true", help="Show disk usage only")
    parser.add_argument("--memory", action="store_true", help="Show memory usage only")
    parser.add_argument("--podman", action="store_true", help="Show running containers only")

    args = parser.parse_args()
    
    data = {
            "uptime": get_uptime(),
            "disk": get_disk(),
            "memory": get_memory(),
            "podman": get_podman(),
            }

    if args.json:
        import json
        print(json.dumps(data, indent=2))
        return

    if args.uptime:
        print(get_uptime())
        return

    if args.disk:
        print(get_disk())
        return

    if args.memory:
        print(get_memory())
        return

    if args.podman:
        print(get_podman())
        return

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
