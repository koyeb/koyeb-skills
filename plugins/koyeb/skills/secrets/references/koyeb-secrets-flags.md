# Koyeb CLI Flags: Secrets

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

## `koyeb secrets create`

```text
Options:
  -h, --help                       help for create
      --registry-keyfile string    Registry URL. Only valid with --type=registry-gcp, otherwise ignored
      --registry-name string       Registry name. Only valid with --type=registry-azure, otherwise ignored
      --registry-url string        Registry URL. Only valid with --type=registry-private and --type=registry-gcp, otherwise ignored
      --registry-username string   Registry username. Only valid with --type=registry-*
      --type type                  Secret type (simple, registry-dockerhub, registry-private, registry-digital-ocean, registry-gitlab, registry-gcp, registry-azure) (default simple)
  -v, --value string               Secret Value
      --value-from-stdin           Secret Value from stdin

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

## `koyeb secrets delete`

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

## `koyeb secrets describe`

```text
Options:
  -h, --help   help for describe

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

## `koyeb secrets get`

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

## `koyeb secrets list`

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

## `koyeb secrets reveal`

```text
Options:
  -h, --help   help for reveal

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

## `koyeb secrets update`

```text
Options:
  -h, --help                       help for update
      --registry-keyfile string    Registry URL. Only valid with --type=registry-gcp, otherwise ignored
      --registry-name string       Registry name. Only valid with --type=registry-azure, otherwise ignored
      --registry-url string        Registry URL. Only valid with --type=registry-private and --type=registry-gcp, otherwise ignored
      --registry-username string   Registry username. Only valid with --type=registry-*
  -v, --value string               Secret Value
      --value-from-stdin           Secret Value from stdin

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
