# Koyeb Sandbox JS SDK

Package: `@koyeb/sandbox-sdk` (inspected v1.0.7)

## Install

- `npm install @koyeb/sandbox-sdk`
- `pnpm add @koyeb/sandbox-sdk`

## Default sandbox image

Reference: https://www.koyeb.com/docs/sandboxes/sandbox-default-image

If no image is specified when creating a sandbox, Koyeb uses a default Ubuntu 22.04–based image with common tools preinstalled, including system utilities (curl, wget, git, jq, zip/unzip, file, procps, ca-certificates), language runtimes/toolchains (Node.js, Python3, Go, Ruby, Rust, Elixir/Erlang, Java, Bun, Deno), and AI tooling (Mistral Vibe, Codex, Gemini, OpenCode).

## Exports

- `Sandbox`
- Errors: `MissingApiTokenError`, `InvalidPortError`, `SandboxTimeoutError`, `NoSandboxSecretError`, `SandboxRequestError`

## Create options

`Sandbox.create(options?: CreateSandboxOptions): Promise<Sandbox>`

`CreateSandboxOptions` (all optional):
- `image: string`
	- Accepts any public Docker Hub image name. For private images, provide `registry_secret`.
- `name: string`
- `wait_ready: boolean`
- `instance_type: string`
	- See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for available instance types by region.
- `exposed_port_protocol: 'http' | 'http2'`
- `env: Record<string, string>`
- `region: string`
	- See [plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md](plugins/koyeb/skills/_shared/references/koyeb-regions-instance-types.md) for valid region IDs.
- `api_token: string`
- `timeout: number`
- `idle_timeout: number`
- `enable_tcp_proxy: boolean`
- `privileged: false`
- `registry_secret?: string`
- `delete_after_create?: number`
- `delete_after_sleep?: number`
- `_experimental_enable_light_sleep: false`

If `api_token` is not provided, the SDK reads `KOYEB_API_TOKEN` from the environment.

## Sandbox static methods

- `Sandbox.create(options?) : Promise<Sandbox>`
- `Sandbox.get_from_id(serviceId: string, apiToken?: string): Promise<Sandbox>`

## Sandbox instance API

Identifiers
- `app_id: string`
- `service_id: string`
- `name: string`
- `id: string` (getter)

Lifecycle and health
- `wait_ready(timeout?: number, pollInterval?: number, signal?: AbortSignal): Promise<boolean>`
- `wait_tcp_proxy_ready(timeout?: number, pollInterval?: number, signal?: AbortSignal): Promise<boolean>`
- `is_healthy(): Promise<boolean>`
- `delete(): Promise<void>`

Networking
- `get_tcp_proxy_info(): Promise<[host: string, public_port: number] | undefined>`
- `get_domain(): Promise<koyeb.Domain>`
- `get_sandbox_url(): Promise<string>`
- `expose_port(port: number): Promise<{ port: number; exposed_at: string }>`
- `unexpose_port(port?: number): Promise<void>`

HTTP helpers
- `fetch(path: string, init: RequestInit, requestBody?: unknown): Promise<Response>`
- `request(path: string, init: RequestInit, requestBody?: unknown): Promise<any>`

Command execution
- `exec(cmd: string, opts?: { cwd?: string; env?: Record<string, string>; signal?: AbortSignal }): Promise<{ stdout: string; stderr: string; code: number }>`
    - Note: use stderr and stdout to monitor outcomes of commands
- `exec_stream(cmd: string, opts?: { cwd?: string; env?: Record<string, string>; signal?: AbortSignal }): SandboxExec`
    - Note: use stderr and stdout to monitor outcomes of commands

`SandboxExec` events:
- `stdout`: `{ stream: 'stdout'; data: string }`
- `stderr`: `{ stream: 'stderr'; data: string }`
- `exit`: `{ code: number; error: boolean }`
- `end`: `Event`

Processes
- `launch_process(cmd: string, options?: { cwd?: string; env?: Record<string, string> }): Promise<string>`
- `kill_process(processId: string): Promise<void>`
- `list_processes(): Promise<SandboxProcess[]>`
- `kill_all_processes(): Promise<number>`

`SandboxProcess` fields:
- `id: string`
- `command: string`
- `status: SandboxProcessStatus`
- `pid: string`

`SandboxProcessStatus`: `'running' | 'completed' | 'failed' | 'killed'`

Filesystem
- `filesystem: SandboxFilesystem`

## Filesystem API (`SandboxFilesystem`)

- `mkdir(path: string, recursive?: boolean): Promise<void>`
- `list_dir(path?: string): Promise<string[]>`
- `delete_dir(path: string): Promise<void>`
- `write_file(path: string, content: string): Promise<void>`
	- Note: `write_file` and `write_files` require the parent directory to exist. Use `mkdir` (with `recursive: true` as needed) before writing to new directories.
- `write_files(files: Array<{ path: string; content: string }>): Promise<void>`
- `read_file(path: string): Promise<{ content: string; encoding: string }>`
- `rename_file(old_path: string, new_path: string): Promise<void>`
- `rm(path: string, recursive?: boolean): Promise<void>`
- `exists(path: string): Promise<boolean>`
- `is_file(path: string): Promise<boolean>`
- `is_dir(path: string): Promise<boolean>`
- `upload_file(local_path: string, remote_path: string): Promise<void>`
- `download_file(local_path: string, remote_path: string): Promise<void>`

## Usage examples

### Create a sandbox and run a command

```js
import { Sandbox } from '@koyeb/sandbox-sdk';

const sandbox = await Sandbox.create({
	image: 'ubuntu',
	name: 'example-sandbox',
	wait_ready: true,
});

const result = await sandbox.exec("echo 'Hello World'");
console.log(result.stdout.trim());

await sandbox.delete();
```

### Stream command output

```js
const stream = sandbox.exec_stream(
	"python3 -c \"import time\nfor i in range(3):\n print(i)\n time.sleep(0.5)\""
);

stream.addEventListener('stdout', (evt) => {
	console.log(evt.data.data);
});

stream.addEventListener('exit', (evt) => {
	console.log('exit code:', evt.data.code);
});
```

### File operations

```js
const fs = sandbox.filesystem;
await fs.write_file('/tmp/hello.txt', 'Hello from JS');
const info = await fs.read_file('/tmp/hello.txt');
console.log(info.content);
```

### Expose a port

```js
await sandbox.launch_process('python3 -m http.server 8080', { cwd: '/tmp' });
const exposed = await sandbox.expose_port(8080);
console.log(exposed.exposed_at);
```

### Auto-delete lifecycle

```js
const sandbox = await Sandbox.create({
	name: 'auto-delete',
	delete_after_create: 60,
	delete_after_sleep: 300,
});
```

### Upload and download files

```js
const fs = sandbox.filesystem;
await fs.upload_file('./local.txt', '/tmp/remote.txt');
await fs.download_file('./downloaded.txt', '/tmp/remote.txt');
```
