# Instances Command Flags Reference

Complete reference for all `koyeb instances` command flags.

## List
```
koyeb instances list [flags]
  --app string       Filter by app
  --service string   Filter by service
```

## Get/Describe
```
koyeb instances get NAME [flags]
koyeb instances describe NAME [flags]
```

## Logs
```
koyeb instances logs NAME [flags]
  -e, --end-time string       Return logs before this date
  --order string              Order: "asc" or "desc" (default: "asc")
  --regex-search string       Regex filter
  -s, --start-time string     Return logs after this date
  --tail                      Tail logs
  --text-search string        Text filter
```

## Exec
```
koyeb instances exec NAME CMD -- [args...] [flags]
```

## Copy
```
koyeb instances cp SRC DST [flags]
```
