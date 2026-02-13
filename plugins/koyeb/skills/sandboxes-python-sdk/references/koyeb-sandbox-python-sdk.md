# Koyeb Sandbox Python SDK

Package: `koyeb-sdk` (inspected v1.2.2)

## Install

- `pip install koyeb-sdk`

## Default sandbox image

Reference: https://www.koyeb.com/docs/sandboxes/sandbox-default-image

If no image is specified when creating a sandbox, Koyeb uses a default Ubuntu 22.04–based image with common tools preinstalled, including system utilities (curl, wget, git, jq, zip/unzip, file, procps, ca-certificates), language runtimes/toolchains (Node.js, Python3, Go, Ruby, Rust, Elixir/Erlang, Java, Bun, Deno), and AI tooling (Mistral Vibe, Codex, Gemini, OpenCode).

## Exports

From `koyeb.sandbox`:
- `Sandbox`, `AsyncSandbox`
- `SandboxFilesystem`, `SandboxExecutor`, `AsyncSandboxExecutor`
- `FileInfo`, `ProcessInfo`, `ExposedPort`
- `SandboxStatus`, `SandboxError`, `SandboxTimeoutError`
- `CommandResult`, `CommandStatus`, `SandboxCommandError`

## Sandbox.create (sync)

`Sandbox.create(...) -> Sandbox`

Parameters (with defaults):
- `image: str = "koyeb/sandbox"`
	- Accepts any public Docker Hub image name. For private images, provide `registry_secret`.
- `name: str = "quick-sandbox"`
- `wait_ready: bool = True`
- `instance_type: str = "micro"`
	- See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for available instance types by region.
- `exposed_port_protocol: Optional[str] = None` ("http" or "http2")
- `env: Optional[Dict[str, str]] = None`
- `region: Optional[str] = None` (default region noted in docstring: "na")
	- See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for valid region IDs.
- `api_token: Optional[str] = None` (uses `KOYEB_API_TOKEN` env var)
- `timeout: int = 300`
- `idle_timeout: int = 0`
    - Note: set to 0 if you don't want the sandbox to ever go to sleep. When you wake it back up, it will be back to its default state.
- `enable_tcp_proxy: bool = False`
- `privileged: bool = False`
- `registry_secret: Optional[str] = None`
- `_experimental_enable_light_sleep: bool = False`
- `delete_after_delay: int = 0`
- `delete_after_inactivity_delay: int = 0`
- `app_id: Optional[str] = None` (use existing app)

## Sandbox.get_from_id (sync)

`Sandbox.get_from_id(id: str, api_token: Optional[str] = None) -> Sandbox`

## Sandbox instance methods (sync)

Lifecycle and status
- `wait_ready(timeout: int = DEFAULT_INSTANCE_WAIT_TIMEOUT, poll_interval: float = DEFAULT_POLL_INTERVAL) -> bool`
- `wait_tcp_proxy_ready(timeout: int = DEFAULT_INSTANCE_WAIT_TIMEOUT, poll_interval: float = DEFAULT_POLL_INTERVAL) -> bool`
- `is_healthy() -> bool`
- `delete() -> None`
- `update_lifecycle(delete_after_delay: Optional[int] = None, delete_after_inactivity: Optional[int] = None) -> None`

Networking
- `get_domain() -> Optional[str]`
- `get_tcp_proxy_info() -> Optional[tuple[str, int]]`
- `get_sandbox_url() -> Optional[str]` (internal helper)
- `expose_port(port: int) -> ExposedPort`
- `unexpose_port() -> None`

Processes
- `launch_process(cmd: str, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None) -> str`
- `kill_process(process_id: str) -> None`
- `list_processes() -> List[ProcessInfo]`
- `kill_all_processes() -> int`

Command execution
- `exec(command: str, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None, timeout: int = 30, on_stdout: Optional[Callable[[str], None]] = None, on_stderr: Optional[Callable[[str], None]] = None) -> CommandResult`
    - Note: use on_sterr and on_stdout to monitor progress, especially on long processes. Alternatively, store the result and use .stderr and .stdout to get feedback.

`ProcessInfo` fields:
- `id: str`
- `command: str`
- `status: str` (e.g., "running", "completed")
- `pid: Optional[int]`
- `exit_code: Optional[int]`
- `started_at: Optional[str]`
- `completed_at: Optional[str]`

Interfaces
- `filesystem: SandboxFilesystem`
- `exec: SandboxExecutor`

## AsyncSandbox

`AsyncSandbox.create(...) -> AsyncSandbox` (same parameters as sync)
`AsyncSandbox.get_from_id(id: str, api_token: Optional[str] = None) -> AsyncSandbox`

## Async Sandbox instance methods

Lifecycle and status
- `wait_ready(timeout: int = DEFAULT_INSTANCE_WAIT_TIMEOUT, poll_interval: float = DEFAULT_POLL_INTERVAL) -> bool`
- `wait_tcp_proxy_ready(timeout: int = DEFAULT_INSTANCE_WAIT_TIMEOUT, poll_interval: float = DEFAULT_POLL_INTERVAL) -> bool`
- `is_healthy() -> bool`
- `delete() -> None`
- `update_lifecycle(delete_after_delay: Optional[int] = None, delete_after_inactivity: Optional[int] = None) -> None`

Networking
- `get_domain() -> Optional[str]`
- `get_tcp_proxy_info() -> Optional[tuple[str, int]]`
- `get_sandbox_url() -> Optional[str]` (internal helper)
- `expose_port(port: int) -> ExposedPort`
- `unexpose_port() -> None`

Processes
- `launch_process(cmd: str, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None) -> str`
- `kill_process(process_id: str) -> None`
- `list_processes() -> List[ProcessInfo]`
- `kill_all_processes() -> int`

Command execution
- `exec(command: str, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None, timeout: int = 30, on_stdout: Optional[Callable[[str], None]] = None, on_stderr: Optional[Callable[[str], None]] = None) -> CommandResult`

Interfaces
- `filesystem: AsyncSandboxFilesystem`
- `exec: AsyncSandboxExecutor`

## Command execution (`SandboxExecutor`)

`SandboxExecutor.__call__(command: str, cwd: Optional[str] = None, env: Optional[Dict[str, str]] = None, timeout: int = 30, on_stdout: Optional[Callable[[str], None]] = None, on_stderr: Optional[Callable[[str], None]] = None) -> CommandResult`
    - Note: use on_sterr and on_stdout to monitor progress, especially on long processes. Alternatively, store the result and use .stderr and .stdout to get feedback.

Async: `AsyncSandboxExecutor.__call__(...) -> CommandResult`

`CommandResult` fields:
- `stdout: str`
- `stderr: str`
- `exit_code: int`
- `status: CommandStatus`
- `duration: float`
- `command: str`
- `args: Optional[List[str]]`

## Filesystem (`SandboxFilesystem`)

- `write_file(path: str, content: Union[str, bytes], encoding: str = "utf-8") -> None`
	- Note: `write_file` requires the parent directory to exist. Use `mkdir` before writing to new directories.
- `read_file(path: str, encoding: str = "utf-8") -> FileInfo`
- `mkdir(path: str) -> None`
- `list_dir(path: str = ".") -> List[str]`
- `delete_file(path: str) -> None`
- `delete_dir(path: str) -> None`
- `rename_file(old_path: str, new_path: str) -> None`
- `move_file(source_path: str, destination_path: str) -> None`
- `write_files(files: List[Dict[str, str]]) -> None`
- `exists(path: str) -> bool`
- `is_file(path: str) -> bool`
- `is_dir(path: str) -> bool`
- `rm(path: str, recursive: bool = False) -> None`
- `upload_file(local_path: str, remote_path: str) -> None`
    - Note: `upload_file` requires the parent directory for the remote_path to exist. You must use `mkdir` before uploading to new directories.
- `download_file(local_path: str, remote_path: str) -> None`

`open(path: str, mode: str = "r", encoding: str = "utf-8") -> SandboxFileIO`

## Async filesystem (`AsyncSandboxFilesystem`)

Async equivalents:
- `write_file(path: str, content: Union[str, bytes], encoding: str = "utf-8") -> None`
	- Note: `write_file` requires the parent directory to exist. You must use `mkdir` before writing to new directories.
- `read_file(path: str, encoding: str = "utf-8") -> FileInfo`
- `mkdir(path: str) -> None`
- `list_dir(path: str = ".") -> List[str]`
- `delete_file(path: str) -> None`
- `delete_dir(path: str) -> None`
- `rename_file(old_path: str, new_path: str) -> None`
- `move_file(source_path: str, destination_path: str) -> None`
- `write_files(files: List[Dict[str, str]]) -> None`
- `exists(path: str) -> bool`
- `is_file(path: str) -> bool`
- `is_dir(path: str) -> bool`
- `upload_file(local_path: str, remote_path: str, encoding: str = "utf-8") -> None`
    - Note: `upload_file` requires the parent directory for the remote_path to exist. You must use `mkdir` before uploading to new directories.
- `download_file(remote_path: str, local_path: str, encoding: str = "utf-8") -> None`
- `ls(path: str = ".") -> List[str]`
- `rm(path: str, recursive: bool = False) -> None`
- `open(path: str, mode: str = "r", encoding: str = "utf-8") -> AsyncSandboxFileIO`

## File handles

`SandboxFileIO`:
- `read() -> Union[str, bytes]`
- `write(content: Union[str, bytes]) -> None`
- `close() -> None`
- Context manager: `__enter__`, `__exit__`

`AsyncSandboxFileIO`:
- `read() -> Union[str, bytes]`
- `write(content: Union[str, bytes]) -> None`
- `close() -> None`
- Async context manager: `__aenter__`, `__aexit__`

## Usage examples

### Create a sandbox and run a command (sync)

```python
from koyeb import Sandbox

sandbox = Sandbox.create(
	image="ubuntu",
	name="example-sandbox",
	wait_ready=True,
)

result = sandbox.exec("echo 'Hello World'")
print(result.stdout.strip())

sandbox.delete()
```

### Create a sandbox and run a command (async)

```python
import asyncio
from koyeb import AsyncSandbox

async def main():
	sandbox = await AsyncSandbox.create(
		image="ubuntu",
		name="example-sandbox",
		wait_ready=True,
	)
	result = await sandbox.exec("echo 'Hello World'")
	print(result.stdout.strip())
	await sandbox.delete()

asyncio.run(main())
```

### File operations

```python
fs = sandbox.filesystem
fs.mkdir("/tmp")
fs.write_file("/tmp/hello.txt", "Hello from Python")
info = fs.read_file("/tmp/hello.txt")
print(info.content)
```

### Expose a port

```python
process_id = sandbox.launch_process("python3 -m http.server 8080", cwd="/tmp")
exposed = sandbox.expose_port(8080)
print(exposed.exposed_at)
```

### Manage background processes

```python
process_id = sandbox.launch_process("python3 -c 'import time; time.sleep(60)'")
processes = sandbox.list_processes()
for p in processes:
	print(p.id, p.command, p.status)
sandbox.kill_process(process_id)
```

### Auto-delete lifecycle

```python
sandbox = Sandbox.create(
	name="auto-delete",
	delete_after_delay=60,
	delete_after_inactivity_delay=300,
)

# Update lifecycle later
sandbox.update_lifecycle(delete_after_delay=120, delete_after_inactivity=600)
```

### Upload and download files

```python
fs = sandbox.filesystem
fs.upload_file("./local.txt", "/tmp/remote.txt")
fs.download_file("/tmp/remote.txt", "./downloaded.txt")
```
