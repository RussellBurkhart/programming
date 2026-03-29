# log_tail

A small Python CLI tool for viewing systemd service logs.

## Features

- Tail logs for known service shortcuts
- Tail logs for full systemd unit names
- Show a specific number of lines
- Follow live log output
- List available built-in service shortcuts

## Built-in shortcuts

- `hytale` -> `hytale.service`
- `network` -> `NetworkManager.service`
- `ssh` -> `sshd.service`

## Usage

Show available shortcuts:

```bash
python3 main.py --list
```

Show logs for a service:

```bash
python3 main.py ssh
```

Show a specific number of lines:

```bash
python3 main.py ssh --lines 20
```

Follow live logs:

```bash
python3 main.py ssh --follow
```
