# Koyeb CLI Flags: Services

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

## `koyeb services create`

```text
Options:
  -a, --app string                               Service application
      --archive string                           Archive ID to deploy
      --archive-builder string                   Builder to use, either "buildpack" (default) or "docker" (default "buildpack")
      --archive-buildpack-build-command string   Buid command
      --archive-buildpack-run-command string     Run command
      --archive-docker-args strings              Set arguments to the docker command. To provide multiple arguments, use the --archive-docker-args flag multiple times.
      --archive-docker-command string            Set the docker CMD explicitly. To provide arguments to the command, use the --archive-docker-args flag.
      --archive-docker-dockerfile string         Dockerfile path
      --archive-docker-entrypoint strings        Docker entrypoint
      --archive-docker-target string             Docker target
      --archive-ignore-dir strings               Set directories to ignore when building the archive.
                                                 To ignore multiple directories, use the flag multiple times.
                                                 To include all directories, set the flag to an empty string. (default [.git,node_modules,vendor])
      --autoscaling-average-cpu int              Target CPU usage (in %) to trigger a scaling event. Set to 0 to disable CPU autoscaling.
      --autoscaling-average-mem int              Target memory usage (in %) to trigger a scaling event. Set to 0 to disable memory autoscaling.
      --autoscaling-concurrent-requests int      Target concurrent requests to trigger a scaling event. Set to 0 to disable concurrent requests autoscaling.
      --autoscaling-requests-per-second int      Target requests per second to trigger a scaling event. Set to 0 to disable requests per second autoscaling.
      --autoscaling-requests-response-time int   Target p95 response time to trigger a scaling event (in ms). Set to 0 to disable concurrent response time autoscaling.
      --checks strings                           Update service healthchecks (available for services of type "web" only)
                                                 For HTTP healthchecks, use the format <PORT>:http:<PATH>, for example --checks 8080:http:/health
                                                 For TCP healthchecks, use the format <PORT>:tcp, for example --checks 8080:tcp
                                                 To delete a healthcheck, use !PORT, for example --checks '!8080'
      --checks-grace-period strings              Set healthcheck grace period in seconds.
                                                 Use the format <healthcheck>=<seconds>, for example --checks-grace-period 8080=10
      --config-file strings                      Copy a local file to your service container using the format LOCAL_FILE:PATH:[PERMISSIONS]
                                                 for example --config-file /etc/data.yaml:/etc/data.yaml:0644
                                                 To delete a config file, use !PATH, for example --config-file !/etc/data.yaml
      --deep-sleep-delay duration                Delay after which an idle service is put to deep sleep. Use duration format (e.g., '5m', '30m', '1h'). Set to 0 to disable.
      --delete-after-delay duration              Automatically delete the service after this duration from creation. Use duration format (e.g., '1h', '30m', '24h'). Set to 0 to disable.
      --delete-after-inactivity-delay duration   Automatically delete the service after being inactive (sleeping) for this duration. Use duration format (e.g., '1h', '30m', '24h'). Set to 0 to disable.
      --deployment-strategy STRATEGY             Deployment strategy, either "rolling" (default), "blue-green" or "immediate".
      --docker string                            Docker image
      --docker-args strings                      Set arguments to the docker command. To provide multiple arguments, use the --docker-args flag multiple times.
      --docker-command string                    Set the docker CMD explicitly. To provide arguments to the command, use the --docker-args flag.
      --docker-entrypoint strings                Docker entrypoint. To provide multiple arguments, use the --docker-entrypoint flag multiple times.
      --docker-private-registry-secret string    Docker private registry secret
      --env strings                              Update service environment variables using the format KEY=VALUE, for example --env FOO=bar
                                                 To use the value of a secret as an environment variable, use the following syntax: --env FOO={{secret.bar}}
                                                 To delete an environment variable, prefix its name with '!', for example --env '!FOO'
      --git string                               Git repository
      --git-branch string                        Git branch (default "main")
      --git-build-command string                 Buid command (legacy, prefer git-buildpack-build-command)
      --git-builder string                       Builder to use, either "buildpack" (default) or "docker" (default "buildpack")
      --git-buildpack-build-command string       Buid command
      --git-buildpack-run-command string         Run command
      --git-docker-args strings                  Set arguments to the docker command. To provide multiple arguments, use the --git-docker-args flag multiple times.
      --git-docker-command string                Set the docker CMD explicitly. To provide arguments to the command, use the --git-docker-args flag.
      --git-docker-dockerfile string             Dockerfile path
      --git-docker-entrypoint strings            Docker entrypoint
      --git-docker-target string                 Docker target
      --git-no-deploy-on-push                    Disable new deployments creation when code changes are pushed on the configured branch
      --git-run-command string                   Run command (legacy, prefer git-buildpack-run-command)
      --git-sha string                           Git commit SHA to deploy
      --git-workdir string                       Path to the sub-directory containing the code to build and deploy
  -h, --help                                     help for create
      --instance-type string                     Instance type (default "nano")
      --light-sleep-delay duration               Delay after which an idle service is put to light sleep. Use duration format (e.g., '1m', '5m', '1h'). Set to 0 to disable.
      --max-scale int                            Max scale (default 1)
      --min-scale int                            Min scale (default 1)
      --ports strings                            Update service ports (available for services of type "web" only) using the format PORT[:PROTOCOL], for example --port 8080:http
                                                 PROTOCOL defaults to "http". Supported protocols are "http", "http2" and "tcp"
                                                 To delete an exposed port, prefix its number with '!', for example --port '!80'
      --privileged                               Whether the service container should run in privileged mode
      --proxy-ports strings                      Update service proxy ports (available for services of type "web" only) using format PORT[:PROTOCOL], for example --proxy-ports 22:tcp
                                                 PROTOCOL defaults to "tcp". Supported protocols are "tcp".To delete a proxy port, prefix its number with '!', for example --proxy-ports '!80'
      --regions strings                          Add a region where the service is deployed. You can specify this flag multiple times to deploy the service in multiple regions.
                                                 To update a service and remove a region, prefix the region name with '!', for example --region '!par'
                                                 If the region is not specified on service creation, the service is deployed in was
      --routes strings                           Update service routes (available for services of type "web" only) using the format PATH[:PORT], for example '/foo:8080'
                                                 PORT defaults to 8000
                                                 To delete a route, use '!PATH', for example --route '!/foo'
      --scale int                                Set both min-scale and max-scale (default 1)
      --skip-cache                               Whether to use the cache when building the service
      --type string                              Service type, one of "web", "worker" or "sandbox" (default "web")
      --volumes strings                          Update service volumes using the format VOLUME:PATH, for example --volume myvolume:/data.To delete a volume, use !VOLUME, for example --volume '!myvolume'
      --wait                                     Waits until service deployment is done
      --wait-timeout duration                    Duration the wait will last until timeout (default 5m0s)

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

## `koyeb services delete`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for delete

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

## `koyeb services describe`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for describe

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

## `koyeb services exec`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for exec

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

## `koyeb services get`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for get

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

## `koyeb services list`

```text
Options:
  -a, --app string    App
  -h, --help          help for list
  -n, --name string   Service name

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

## `koyeb services logs`

```text
Options:
  -a, --app string                Service application
      --end-time string           Return logs before this date
  -h, --help                      help for logs
      --instance string           Instance
      --order asc                 Order logs by asc or `desc` (default "asc")
      --regex-search string       Filter logs returned with this regex
      --since HumanFriendlyDate   DEPRECATED. Use --tail --start-time instead. (default 0001-01-01 00:00:00 +0000 UTC)
      --start-time string         Return logs after this date
      --tail                      Tail logs if no --end-time is provided.
      --text-search string        Filter logs returned with this text
  -t, --type string               Type (runtime, build)

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

## `koyeb services pause`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for pause

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

## `koyeb services redeploy`

```text
Options:
  -a, --app string              Service application
  -h, --help                    help for redeploy
      --skip-build              If there has been at least one past successfully build deployment, use the last one instead of rebuilding. WARNING: this can lead to unexpected behavior if the build depends, for example, on environment variables.
      --use-cache               Use cache to redeploy
      --wait                    Waits until service deployment is done.
      --wait-timeout duration   Duration the wait will last until timeout (default 5m0s)

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

## `koyeb services resume`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for resume

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

## `koyeb services scale`

```text
Options:
  -a, --app string        Service application
  -h, --help              help for scale
      --instances int     Number of instances to scale to (used with --regions or alone for all regions) (default 1)
      --regions strings   Regions to apply --instances count to (e.g., 'fra', 'was')
      --scale strings     Scale configuration per region in format 'region:instances' (e.g., 'fra:3'). Can be specified multiple times.

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
Use "koyeb services scale [command] --help" for more information about a command.
```

## `koyeb services scale delete`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for delete

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

## `koyeb services scale get`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for get

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

## `koyeb services scale update`

```text
Options:
  -a, --app string        Service application
  -h, --help              help for update
      --instances int     Number of instances to scale to (used with --regions or alone for all regions) (default 1)
      --regions strings   Regions to apply --instances count to (e.g., 'fra', 'was') or '!region' to remove (e.g., '!fra')
      --scale strings     Scale configuration per region in format 'region:instances' (e.g., 'fra:3') or '!region' to remove (e.g., '!fra'). Can be specified multiple times.

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

## `koyeb services unapplied-changes`

```text
Options:
  -a, --app string   Service application
  -h, --help         help for unapplied-changes

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

## `koyeb services update`

```text
Options:
  -a, --app string                               Service application
      --archive string                           Archive ID to deploy
      --archive-builder string                   Builder to use, either "buildpack" (default) or "docker" (default "buildpack")
      --archive-buildpack-build-command string   Buid command
      --archive-buildpack-run-command string     Run command
      --archive-docker-args strings              Set arguments to the docker command. To provide multiple arguments, use the --archive-docker-args flag multiple times.
      --archive-docker-command string            Set the docker CMD explicitly. To provide arguments to the command, use the --archive-docker-args flag.
      --archive-docker-dockerfile string         Dockerfile path
      --archive-docker-entrypoint strings        Docker entrypoint
      --archive-docker-target string             Docker target
      --archive-ignore-dir strings               Set directories to ignore when building the archive.
                                                 To ignore multiple directories, use the flag multiple times.
                                                 To include all directories, set the flag to an empty string. (default [.git,node_modules,vendor])
      --autoscaling-average-cpu int              Target CPU usage (in %) to trigger a scaling event. Set to 0 to disable CPU autoscaling.
      --autoscaling-average-mem int              Target memory usage (in %) to trigger a scaling event. Set to 0 to disable memory autoscaling.
      --autoscaling-concurrent-requests int      Target concurrent requests to trigger a scaling event. Set to 0 to disable concurrent requests autoscaling.
      --autoscaling-requests-per-second int      Target requests per second to trigger a scaling event. Set to 0 to disable requests per second autoscaling.
      --autoscaling-requests-response-time int   Target p95 response time to trigger a scaling event (in ms). Set to 0 to disable concurrent response time autoscaling.
      --checks strings                           Update service healthchecks (available for services of type "web" only)
                                                 For HTTP healthchecks, use the format <PORT>:http:<PATH>, for example --checks 8080:http:/health
                                                 For TCP healthchecks, use the format <PORT>:tcp, for example --checks 8080:tcp
                                                 To delete a healthcheck, use !PORT, for example --checks '!8080'
      --checks-grace-period strings              Set healthcheck grace period in seconds.
                                                 Use the format <healthcheck>=<seconds>, for example --checks-grace-period 8080=10
      --config-file strings                      Copy a local file to your service container using the format LOCAL_FILE:PATH:[PERMISSIONS]
                                                 for example --config-file /etc/data.yaml:/etc/data.yaml:0644
                                                 To delete a config file, use !PATH, for example --config-file !/etc/data.yaml
      --deep-sleep-delay duration                Delay after which an idle service is put to deep sleep. Use duration format (e.g., '5m', '30m', '1h'). Set to 0 to disable.
      --delete-after-delay duration              Automatically delete the service after this duration from creation. Use duration format (e.g., '1h', '30m', '24h'). Set to 0 to disable.
      --delete-after-inactivity-delay duration   Automatically delete the service after being inactive (sleeping) for this duration. Use duration format (e.g., '1h', '30m', '24h'). Set to 0 to disable.
      --deployment-strategy STRATEGY             Deployment strategy, either "rolling" (default), "blue-green" or "immediate".
      --docker string                            Docker image
      --docker-args strings                      Set arguments to the docker command. To provide multiple arguments, use the --docker-args flag multiple times.
      --docker-command string                    Set the docker CMD explicitly. To provide arguments to the command, use the --docker-args flag.
      --docker-entrypoint strings                Docker entrypoint. To provide multiple arguments, use the --docker-entrypoint flag multiple times.
      --docker-private-registry-secret string    Docker private registry secret
      --env strings                              Update service environment variables using the format KEY=VALUE, for example --env FOO=bar
                                                 To use the value of a secret as an environment variable, use the following syntax: --env FOO={{secret.bar}}
                                                 To delete an environment variable, prefix its name with '!', for example --env '!FOO'
      --git string                               Git repository
      --git-branch string                        Git branch (default "main")
      --git-build-command string                 Buid command (legacy, prefer git-buildpack-build-command)
      --git-builder string                       Builder to use, either "buildpack" (default) or "docker" (default "buildpack")
      --git-buildpack-build-command string       Buid command
      --git-buildpack-run-command string         Run command
      --git-docker-args strings                  Set arguments to the docker command. To provide multiple arguments, use the --git-docker-args flag multiple times.
      --git-docker-command string                Set the docker CMD explicitly. To provide arguments to the command, use the --git-docker-args flag.
      --git-docker-dockerfile string             Dockerfile path
      --git-docker-entrypoint strings            Docker entrypoint
      --git-docker-target string                 Docker target
      --git-no-deploy-on-push                    Disable new deployments creation when code changes are pushed on the configured branch
      --git-run-command string                   Run command (legacy, prefer git-buildpack-run-command)
      --git-sha string                           Git commit SHA to deploy
      --git-workdir string                       Path to the sub-directory containing the code to build and deploy
  -h, --help                                     help for update
      --instance-type string                     Instance type (default "nano")
      --light-sleep-delay duration               Delay after which an idle service is put to light sleep. Use duration format (e.g., '1m', '5m', '1h'). Set to 0 to disable.
      --max-scale int                            Max scale (default 1)
      --min-scale int                            Min scale (default 1)
      --name string                              Specify to update the service name
      --override                                 Override the service configuration with the new configuration instead of merging them
      --ports strings                            Update service ports (available for services of type "web" only) using the format PORT[:PROTOCOL], for example --port 8080:http
                                                 PROTOCOL defaults to "http". Supported protocols are "http", "http2" and "tcp"
                                                 To delete an exposed port, prefix its number with '!', for example --port '!80'
      --privileged                               Whether the service container should run in privileged mode
      --proxy-ports strings                      Update service proxy ports (available for services of type "web" only) using format PORT[:PROTOCOL], for example --proxy-ports 22:tcp
                                                 PROTOCOL defaults to "tcp". Supported protocols are "tcp".To delete a proxy port, prefix its number with '!', for example --proxy-ports '!80'
      --regions strings                          Add a region where the service is deployed. You can specify this flag multiple times to deploy the service in multiple regions.
                                                 To update a service and remove a region, prefix the region name with '!', for example --region '!par'
                                                 If the region is not specified on service creation, the service is deployed in was
      --routes strings                           Update service routes (available for services of type "web" only) using the format PATH[:PORT], for example '/foo:8080'
                                                 PORT defaults to 8000
                                                 To delete a route, use '!PATH', for example --route '!/foo'
      --save-only                                Save the new configuration without deploying it
      --scale int                                Set both min-scale and max-scale (default 1)
      --skip-build                               If there has been at least one past successfully build deployment, use the last one instead of rebuilding. WARNING: this can lead to unexpected behavior if the build depends, for example, on environment variables.
      --skip-cache                               Whether to use the cache when building the service
      --type string                              Service type, one of "web", "worker" or "sandbox" (default "web")
      --volumes strings                          Update service volumes using the format VOLUME:PATH, for example --volume myvolume:/data.To delete a volume, use !VOLUME, for example --volume '!myvolume'
      --wait                                     Waits until the service deployment is done
      --wait-timeout duration                    Duration the wait will last until timeout (default 5m0s)

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
