#!/usr/bin/env python3
import argparse
import subprocess
import sys
from lib.system import print_info
from lib.status import print_status

def main():
    parser = argparse.ArgumentParser(description="Homelab toolkit")
    subparsers = parser.add_subparsers(dest="command")

    info_parser = subparsers.add_parser("info", help="Show system info")
    info_parser.add_argument("--json", action="store_true")

    status_parser = subparsers.add_parser("status", help="Show server status")
    status_parser.add_argument("--json", action="store_true")

    logs_parser = subparsers.add_parser("logs", help="Show service logs")
    logs_parser.add_argument("service")
    logs_parser.add_argument("--lines", type=int, default=50)
    logs_parser.add_argument("--follow", action="store_true")
    logs_parser.add_argument("--filter", type=str)

    args = parser.parse_args()

    if args.command == "info":
        print_info(as_json=args.json)  # Use the imported function
        return
    elif args.command == "status":
        print_status(as_json=args.json)
        return
    elif args.command == "logs":
        cmd = ["log-tail", args.service, "--lines", str(args.lines)]
        if args.follow:
            cmd.append("--follow")
        if args.filter:
            cmd.extend(["--filter", args.filter])
    else:
        parser.print_help()
        sys.exit(1)

    subprocess.run(cmd, check=False)

if __name__ == "__main__":
    main()
