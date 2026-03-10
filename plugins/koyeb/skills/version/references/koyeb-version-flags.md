# Koyeb CLI Flags: Version

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

## `koyeb version`

```text
Options:
  -h, --help   help for version

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
