# Sandboxes Command Flags Reference

Complete reference for all `koyeb sandbox` command flags.

## Usage

`koyeb sandbox [command] [flags]`

Aliases: `sandbox`, `sb`

## Commands

- `create`: Create a new sandbox
- `expose-port`: Expose a port from the sandbox via TCP proxy
- `fs`: Filesystem operations
- `health`: Check sandbox health status
- `kill`: Kill a background process in the sandbox
- `list`: List sandboxes
- `logs`: Stream logs from a background process
- `ps`: List background processes in the sandbox
- `run`: Execute a command in the sandbox
- `start`: Start a background process in the sandbox
- `unexpose-port`: Unexpose the currently exposed port

## Command Flags

Top-level flags for `koyeb sandbox`:

- `-h, --help`: help for sandbox

## Global Flags

Global flags apply to all Koyeb CLI commands:

- `-c, --config string`: config file (default is $HOME/.koyeb.yaml)
- `-d, --debug`: enable the debug output
- `--debug-full`: do not hide sensitive information (tokens) in the debug output
- `--force-ascii`: only output ascii characters (no unicode emojis)
- `--full`: do not truncate output
- `--organization string`: organization ID
- `-o, --output output`: output format (yaml,json,table)
- `--token string`: API token
- `--url string`: url of the api (default "https://app.koyeb.com")

## Subcommand Flags

### `create`

Usage: `koyeb sandbox create NAME [flags]`

- `-a, --app string`: Sandbox application
- `--config-file strings`: Config files (LOCAL:REMOTE:PERMS)
- `--deep-sleep-delay duration`: Delay after which an idle service is put to deep sleep (e.g., `5m`, `30m`, `1h`), 0 to disable
- `--delete-after-delay duration`: Auto-delete after duration (e.g., `24h`)
- `--delete-after-inactivity-delay duration`: Auto-delete after inactivity (e.g., `1h`)
- `--docker string`: Docker image (default: `koyeb/sandbox`)
- `--docker-args strings`: Docker command arguments
- `--docker-command string`: Docker command
- `--docker-entrypoint strings`: Docker entrypoint
- `--docker-private-registry-secret string`: Docker private registry secret
- `--env strings`: Environment variables (KEY=VALUE)
- `-h, --help`: help for create
- `--instance-type string`: Instance type (default `nano`)
- `--light-sleep-delay duration`: Delay after which an idle service is put to light sleep (e.g., `1m`, `5m`, `1h`), 0 to disable
- `--min-scale int`: Min scale (default 1)
- `--privileged`: Run in privileged mode
- `--regions strings`: Deployment regions
- `--wait`: Wait until sandbox deployment is done
- `--wait-timeout duration`: Wait timeout duration (default `5m0s`)

### `expose-port`

Usage: `koyeb sandbox expose-port NAME PORT [flags]`

- `-h, --help`: help for expose-port

### `fs`

Usage: `koyeb sandbox fs [command]`

Filesystem subcommands:

#### `fs download`

Usage: `koyeb sandbox fs download NAME REMOTE_PATH LOCAL_PATH [flags]`

- `-h, --help`: help for download

#### `fs ls`

Usage: `koyeb sandbox fs ls NAME [PATH] [flags]`

- `-h, --help`: help for ls
- `-l, --long`: Use long listing format with details

#### `fs mkdir`

Usage: `koyeb sandbox fs mkdir NAME PATH [flags]`

- `-h, --help`: help for mkdir

#### `fs read`

Usage: `koyeb sandbox fs read NAME PATH [flags]`

- `-h, --help`: help for read

#### `fs rm`

Usage: `koyeb sandbox fs rm NAME PATH [flags]`

- `-h, --help`: help for rm
- `-r, --recursive`: Remove directories recursively

#### `fs upload`

Usage: `koyeb sandbox fs upload NAME LOCAL_PATH REMOTE_PATH [flags]`

- `-f, --force`: Overwrite existing remote directory
- `-h, --help`: help for upload
- `-r, --recursive`: Upload directories recursively

#### `fs write`

Usage: `koyeb sandbox fs write NAME PATH [CONTENT] [flags]`

- `-f, --file string`: Read content from local file
- `-h, --help`: help for write

### `health`

Usage: `koyeb sandbox health NAME [flags]`

- `-h, --help`: help for health

### `kill`

Usage: `koyeb sandbox kill NAME PROCESS_ID [flags]`

- `-h, --help`: help for kill

### `list`

Usage: `koyeb sandbox list [flags]`

- `-a, --app string`: App
- `-h, --help`: help for list
- `-n, --name string`: Sandbox name

### `logs`

Usage: `koyeb sandbox logs NAME PROCESS_ID [flags]`

- `-f, --follow`: Follow log output (like tail -f)
- `-h, --help`: help for logs

### `ps`

Usage: `koyeb sandbox ps NAME [flags]`

- `-h, --help`: help for ps

Aliases: `ps`, `list-processes`

### `run`

Usage: `koyeb sandbox run NAME COMMAND [ARGS...] [flags]`

- `--cwd string`: Working directory for the command
- `--env strings`: Environment variables (KEY=VALUE)
- `-h, --help`: help for run
- `--stream`: Stream output in real-time
- `--timeout int`: Command timeout in seconds (default 30)

### `start`

Usage: `koyeb sandbox start NAME COMMAND [ARGS...] [flags]`

- `--cwd string`: Working directory for the process
- `--env strings`: Environment variables (KEY=VALUE)
- `-h, --help`: help for start

Aliases: `start`, `launch`

### `unexpose-port`

Usage: `koyeb sandbox unexpose-port NAME [flags]`

- `-h, --help`: help for unexpose-port

