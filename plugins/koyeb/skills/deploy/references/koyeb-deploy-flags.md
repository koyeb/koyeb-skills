# Deploy Command Flags Reference

Complete reference for `koyeb deploy` command flags.

## Deploy
```
koyeb deploy <path> <app>/<service> [flags]
```

### Flags
- `--app string` - Service app
- `--archive string` - Archive ID
- `--archive-builder string` - Builder: "buildpack" or "docker" (default: "buildpack")
- `--archive-buildpack-build-command string` - Build command
- `--archive-buildpack-run-command string` - Run command
- `--archive-docker-args strings` - Docker arguments (can repeat)
- `--archive-docker-command string` - Docker CMD
- `--archive-docker-dockerfile string` - Dockerfile path
- `--archive-docker-entrypoint strings` - Docker entrypoint (can repeat)
- `--archive-docker-target string` - Docker target stage
- `--archive-ignore-dir strings` - Directories to ignore (default: .git, node_modules, vendor)
- `--autoscaling-average-cpu int` - Target CPU % for scaling (0 to disable)
- `--autoscaling-average-mem int` - Target memory % for scaling (0 to disable)
- `--autoscaling-concurrent-requests int` - Target concurrent requests for scaling (0 to disable)
- `--autoscaling-requests-per-second int` - Target requests/sec for scaling (0 to disable)
- `--autoscaling-requests-response-time int` - Target p95 response time ms for scaling (0 to disable)
- `--checks strings` - Health checks (format: `PORT:http:PATH` or `PORT:tcp`)
- `--checks-grace-period strings` - Health check grace period (format: `PORT=seconds`)
- `--config-file strings` - Config files to copy (format: `LOCAL:REMOTE[:PERMS]`)
- `--deployment-strategy string` - Strategy: "rolling", "blue-green", or "immediate"
- `--delete-after-delay duration` - Auto-delete after duration (e.g., 1h, 30m)
- `--delete-after-inactivity-delay duration` - Auto-delete after inactivity (e.g., 1h, 30m)
- `--env strings` - Environment variables (format: `KEY=VALUE` or `{{secret.name}}`)
- `--instance-type string` - Instance type (default: "nano")
- `--max-scale int` - Max replicas (default: 1)
- `--min-scale int` - Min replicas (default: 1)
- `--ports strings` - Port mappings (format: `PORT[:PROTOCOL]`)
- `--privileged` - Run in privileged mode
- `--proxy-ports strings` - Proxy ports (format: `PORT[:PROTOCOL]`)
- `--regions strings` - Deploy regions (can repeat)
- `--routes strings` - Routes (format: `PATH[:PORT]`)
- `--scale int` - Set min and max scale (default: 1)
- `--skip-cache` - Skip build cache
- `--type string` - Service type: "web", "worker", or "sandbox" (default: "web")
- `--volumes strings` - Volume mounts (format: `VOLUME:PATH`)
- `--wait` - Wait for deployment
- `--wait-timeout duration` - Deployment wait timeout (default: 5m)
