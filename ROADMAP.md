# Programming Roadmap

This document tracks my progress, current state, and next steps.

---

## Phase 1 — Foundations (Completed)

Built and learned:

### Tools
- `system_info`
  - Basic CLI tool
  - JSON output
  - Field selection

- `server_status`
  - Uptime, disk, memory, containers
  - CLI flags
  - JSON output

- `log_tail`
  - systemd log viewer
  - Service shortcuts
  - Filtering
  - Follow mode

### Key Concepts Learned
- argparse CLI design
- Writing reusable scripts
- Debugging real issues
- Using subprocess
- Structuring Python projects
- Git + GitHub workflow

---

## Phase 2 — CLI Integration (Completed)

Created unified command:

### `homelab`
- `homelab info`
- `homelab status`
- `homelab logs`

### Architecture Upgrade
- Moved logic into modules:
  - `lib/system.py`
  - `lib/status.py`
  - `lib/logs.py`
- Reduced subprocess usage
- Created a reusable codebase

### Key Concepts Learned
- Subcommands (like git/docker)
- Argument forwarding
- Modular design
- Separating logic from CLI

---

## Current State

I now have:
- Multiple working CLI tools
- A unified command (`homelab`)
- Modular Python code structure
- GitHub project tracking real progress

---

## Phase 3 — Next Steps

### Short Term
- [ ] Add more services to log shortcuts
- [ ] Improve output formatting (colors, tables)
- [ ] Add error handling and validation
- [ ] Standardize flags across commands

### Medium Term
- [ ] Package project (pip installable)
- [ ] Add configuration file support
- [ ] Add caching for faster commands
- [ ] Create install script for new systems

### Long Term
- [ ] Web dashboard for homelab
- [ ] API for metrics
- [ ] Remote monitoring support
- [ ] Expand into full dev toolkit

---

## Notes

This repository represents my learning journey.
I am intentionally keeping earlier tools to track progress over time.
