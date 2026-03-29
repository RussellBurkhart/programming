# server_status

A small Python CLI tool for checking basic server health.

## What it shows

- Uptime
- Disk usage
- Memory usage
- Running Podman containers

## Run

```bash
python3 main.py
#Shows everything
```

```bash
python3 main.py --uptime
#Shows only uptime
```

```bash
python3 main.py --disk
#Shows only disk usage
```

```bash
python3 main.py --memory
#Shows only memory usage
```

```bash
python3 main.py --podman
#Shows active containers
```
