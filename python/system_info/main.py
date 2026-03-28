#!/usr/bin/env python3
import argparse
import platform
import socket
import os

def get_info():
    return {
        "hostname": socket.gethostname(),
        "os": f"{platform.system()} {platform.release()}",
        "machine": platform.machine(),
        "python": platform.python_version(),
        "cwd": os.getcwd()
    }

def main():
    parser = argparse.ArgumentParser(description="System Info CLI Tool")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--field", type=str, help="Show a specific field")

    args = parser.parse_args()
    info = get_info()

    if args.field:
        print(info.get(args.field, "Unknown field"))
        return

    if args.json:
        import json
        print(json.dumps(info, indent=2))
        return

    print("System Info")
    print("-----------")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
