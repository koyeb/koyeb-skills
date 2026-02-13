# Services Command Flags Reference

Complete reference for all `koyeb services` command flags.

## List
```
koyeb services list [flags]
  -a, --app string      Filter by app
  -n, --name string     Filter by service name
```

## Get/Describe
```
koyeb services get NAME [flags]
koyeb services describe NAME [flags]
  -a, --app string      Service app
```

## Create
```
koyeb services create NAME [flags]
```

### Flags
- `-a, --app string` - Service app (required)
- `--archive string` - Archive ID to deploy
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
- `--deep-sleep-delay` — Duration after which an idle service enters deep sleep (e.g., --deep-sleep-delay 30m)
    - Note: Set either `--light-sleep-delay` or `--deep-sleep-delay` to 0 to disable that sleep mode.
- `--deployment-strategy string` - Strategy: "rolling", "blue-green", or "immediate"
- `--delete-after-delay duration` - Auto-delete after duration (e.g., 1h, 30m)
- `--delete-after-inactivity-delay duration` - Auto-delete after inactivity (e.g., 1h, 30m)
- `--docker string` - Docker image
- `--docker-args strings` - Docker CMD arguments (can repeat)
- `--docker-command string` - Docker CMD
- `--docker-entrypoint strings` - Docker entrypoint (can repeat)
- `--docker-private-registry-secret string` - Private registry secret
- `--env strings` - Environment variables (format: `KEY=VALUE` or `{{secret.name}}`)
- `--git string` - Git repository URL
- `--git-branch string` - Git branch (default: "main")
- `--git-build-command string` - Build command (legacy)
- `--git-builder string` - Builder: "buildpack" or "docker" (default: "buildpack")
- `--git-buildpack-build-command string` - Build command
- `--git-buildpack-run-command string` - Run command
- `--git-docker-args strings` - Docker arguments (can repeat)
- `--git-docker-command string` - Docker CMD
- `--git-docker-dockerfile string` - Dockerfile path
- `--git-docker-entrypoint strings` - Docker entrypoint (can repeat)
- `--git-docker-target string` - Docker target stage
- `--git-no-deploy-on-push` - Disable auto-deploy on push
- `--git-run-command string` - Run command (legacy)
- `--git-sha string` - Commit SHA to deploy
- `--git-workdir string` - Subdirectory containing code
- `--instance-type string` - Instance type (default: "nano")
    - See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for available instance types by region.
- `--light-sleep-delay` — Duration after which an idle service enters deep sleep (e.g., --deep-sleep-delay 30m)
    - Note: Set either `--light-sleep-delay` or `--deep-sleep-delay` to 0 to disable that sleep mode.
- `--max-scale int` - Max replicas (default: 1)
- `--min-scale int` - Min replicas (default: 1)
- `--ports strings` - Port mappings (format: `PORT[:PROTOCOL]`)
- `--privileged` - Run in privileged mode
- `--proxy-ports strings` - Proxy ports (format: `PORT[:PROTOCOL]`)
- `--regions strings` - Deploy regions (can repeat)
    - See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for available regions by instance type.
- `--routes strings` - Routes (format: `PATH[:PORT]`)
- `--scale int` - Set min and max scale (default: 1)
- `--skip-cache` - Skip build cache
- `--type string` - Service type: "web", "worker", or "sandbox" (default: "web")
- `--volumes strings` - Volume mounts (format: `VOLUME:PATH`)
- `--wait` - Wait for deployment
- `--wait-timeout duration` - Deployment wait timeout (default: 5m)

## Update
```
koyeb services update NAME [flags]
```

Same flags as create, plus:
- `--name string` - New service name
- `--override` - Override config instead of merging
- `--save-only` - Save without deploying
- `--skip-build` - Use last successful build

## Delete
```
koyeb services delete NAME [flags]
  -a, --app string      Service app
```

## Pause/Resume
```
koyeb services pause NAME [flags]
koyeb services resume NAME [flags]
  -a, --app string      Service app
```

## Logs
```
koyeb services logs NAME [flags]
  -a, --app string               Service app
  -e, --end-time string          Return logs before this date
  --instance string              Filter by instance
  --order string                 Order: "asc" or "desc" (default: "asc")
  --regex-search string          Regex filter
  -s, --start-time string        Return logs after this date
  --tail                         Tail logs
  --text-search string           Text filter
  -t, --type string              Log type: "runtime" or "build"
```

## Exec
```
koyeb services exec NAME CMD -- [args...] [flags]
  -a, --app string      Service app
```

## Redeploy
```
koyeb services redeploy NAME [flags]
  -a, --app string              Service app
  --skip-build                  Use last successful build
  --use-cache                   Use cache
  --wait                        Wait for deployment
  --wait-timeout duration       Deployment wait timeout (default: 5m)
```

## Unapplied Changes
```
koyeb services unapplied-changes SERVICE_NAME [flags]
  -a, --app string      Service app
```
