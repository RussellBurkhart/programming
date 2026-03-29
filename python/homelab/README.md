# homelab

A unified CLI wrapper for my homelab tools.

## Commands

### info
Show system information.

```bash
homelab info
homelab info --json
```

### status
Show server status information.

```bash
homelab status
homelab status --disk
homelab status --memory
homelab status --podman
homelab status --json
```

### logs
Show service logs.

```bash
homelab logs ssh --lines 20
homelab logs hytale --filter world
homelab logs network --follow
```
