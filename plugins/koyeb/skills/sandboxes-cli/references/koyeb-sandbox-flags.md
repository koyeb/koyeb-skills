# Koyeb CLI Flags: Sandbox

Reference generated from `koyeb --help` output.

## Global Flags

- `-c, --config string` - Config file (default: `$HOME/.koyeb.yaml`)
- `-d, --debug` - Enable debug output
- `--debug-full` - Show sensitive info in debug output
- `--force-ascii` - Only output ASCII characters
- `--full` - Do not truncate output
- `-o, --output output` - Output format (`yaml`, `json`, `table`)
- `--organization string` - Organization ID
- `--token string` - API token
- `--url string` - API URL
- `-h, --help` - Show help

## `koyeb sandbox create`

```text
Options:
  -a, --app string                               Sandbox application
      --config-file strings                      Config files (LOCAL:REMOTE:PERMS)
      --deep-sleep-delay duration                Delay after which an idle service is put to deep sleep. Use duration format (e.g., '5m', '30m', '1h'). Set to 0 to disable.
      --delete-after-delay duration              Auto-delete after duration (e.g., '24h')
      --delete-after-inactivity-delay duration   Auto-delete after inactivity (e.g., '1h')
      --docker string                            Docker image (default: koyeb/sandbox)
      --docker-args strings                      Docker command arguments
      --docker-command string                    Docker command
      --docker-entrypoint strings                Docker entrypoint
      --docker-private-registry-secret string    Docker private registry secret
      --env strings                              Environment variables (KEY=VALUE)
  -h, --help                                     help for create
      --instance-type string                     Instance type (default "nano")
      --light-sleep-delay duration               Delay after which an idle service is put to light sleep. Use duration format (e.g., '1m', '5m', '1h'). Set to 0 to disable.
      --min-scale int                            Min scale (default 1)
      --privileged                               Run in privileged mode
      --regions strings                          Deployment regions
      --wait                                     Wait until sandbox deployment is done
      --wait-timeout duration                    Wait timeout duration (default 5m0s)

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox expose-port`

```text
Options:
  -h, --help   help for expose-port

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs download`

```text
Options:
  -h, --help   help for download

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs ls`

```text
Options:
  -h, --help   help for ls
  -l, --long   Use long listing format with details

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs mkdir`

```text
Options:
  -h, --help   help for mkdir

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs read`

```text
Options:
  -h, --help   help for read

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs rm`

```text
Options:
  -h, --help        help for rm
  -r, --recursive   Remove directories recursively

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs upload`

```text
Options:
  -f, --force       Overwrite existing remote directory
  -h, --help        help for upload
  -r, --recursive   Upload directories recursively

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox fs write`

```text
Options:
  -f, --file string   Read content from local file
  -h, --help          help for write

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox health`

```text
Options:
  -h, --help   help for health

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox kill`

```text
Options:
  -h, --help   help for kill

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox list`

```text
Options:
  -a, --app string    App
  -h, --help          help for list
  -n, --name string   Sandbox name

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox logs`

```text
Options:
  -f, --follow   Follow log output (like tail -f)
  -h, --help     help for logs

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox ps`

```text
Options:
  -h, --help   help for ps

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox run`

```text
Options:
      --cwd string    Working directory for the command
      --env strings   Environment variables (KEY=VALUE)
  -h, --help          help for run
      --stream        Stream output in real-time
      --timeout int   Command timeout in seconds (default 30)

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox start`

```text
Options:
      --cwd string    Working directory for the process
      --env strings   Environment variables (KEY=VALUE)
  -h, --help          help for start

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```

## `koyeb sandbox unexpose-port`

```text
Options:
  -h, --help   help for unexpose-port

Options inherited from parent commands:
  -c, --config string         config file (default is $HOME/.koyeb.yaml)
  -d, --debug                 enable the debug output
      --debug-full            do not hide sensitive information (tokens) in the debug output
      --force-ascii           only output ascii characters (no unicode emojis)
      --full                  do not truncate output
      --organization string   organization ID
  -o, --output output         output format (yaml,json,table)
      --token string          API token
      --url string            url of the api (default "https://app.koyeb.com")
```
