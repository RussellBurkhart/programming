#!/usr/bin/env python3
import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Homelab toolkit")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("info", help="Show system info")
    subparsers.add_parser("status", help="Show server status")

    logs_parser = subparsers.add_parser("logs", help="Show service logs")
    logs_parser.add_argument("service")
    logs_parser.add_argument("--lines", type=int, default=50)
    logs_parser.add_argument("--follow", action="store_true")
    logs_parser.add_argument("--filter", type=str)

    args, extra = parser.parse_known_args()

    if args.command == "info":
        cmd = ["sysinfo"] + extra
    elif args.command == "status":
        cmd = ["server-status"] + extra
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
