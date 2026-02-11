# Deployments Command Flags Reference

Complete reference for all `koyeb deployments` command flags.

## List
```
koyeb deployments list [flags]
  --app string       Filter by app
  --service string   Filter by service
```

## Get/Describe
```
koyeb deployments get NAME [flags]
koyeb deployments describe NAME [flags]
```

## Logs
```
koyeb deployments logs NAME [flags]
  -e, --end-time string       Return logs before this date
  --order string              Order: "asc" or "desc" (default: "asc")
  --regex-search string       Regex filter
  -s, --start-time string     Return logs after this date
  --tail                      Tail logs
  --text-search string        Text filter
  -t, --type string           Log type: "runtime" or "build"
```

## Cancel
```
koyeb deployments cancel NAME [flags]
```
