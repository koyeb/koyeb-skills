# Koyeb CLI Flags: Volumes

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

## `koyeb volumes create`

```text
Options:
  -h, --help              help for create
      --read-only         Force the volume to be read-only
      --region string     Region of the volume (default "was")
      --size int          Size of the volume in GB (default -1)
      --snapshot string   Specify a snapshot to use to create the volume from

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

## `koyeb volumes delete`

```text
Options:
  -h, --help   help for delete

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

## `koyeb volumes get`

```text
Options:
  -h, --help   help for get

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

## `koyeb volumes list`

```text
Options:
  -h, --help   help for list

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

## `koyeb volumes update`

```text
Options:
  -h, --help          help for update
      --name string   Change the volume name
      --size int      Increase the volume size (default -1)

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
