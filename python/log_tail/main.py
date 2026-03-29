#!/usr/bin/env python3
import argparse
import subprocess
import sys

SERVICES = {
        "hytale": "hytale.service",
        "network": "NetworkManager.service",
        "ssh": "sshd.service",
        }

def main():
    parser = argparse.ArgumentParser(description="Tail logs for a systemd service")
    parser.add_argument("service", help="Service shortcut or full systemd unit name", nargs="?")
    parser.add_argument("--list", action="store_true", help="List available services")
    parser.add_argument("--lines", type=int, default=50, help="Number of lines to show")
    parser.add_argument("--follow", action="store_true", help="Follow the log output")
    parser.add_argument("--filter", type=str, help="Only show lines containing this text")

    args = parser.parse_args()

    if args.list:
        print("Available services:")
        for name in SERVICES:
            print(f"- {name} -> {SERVICES[name]}")
        return

    unit = SERVICES.get(args.service, args.service)

    cmd = ["journalctl", "-u", unit, "-n", str(args.lines), "--no-pager"]

    if args.follow:
        cmd.remove("--no-pager")
        cmd.append("-f")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)

        output = result.stdout

        if args.filter:
            lines = output.splitlines()
            output = "\n".join(line for line in lines if args.filter.lower() in line.lower())

        print(output)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
