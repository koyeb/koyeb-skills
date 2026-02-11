# Apps Command Flags Reference

Complete reference for all `koyeb apps` command flags.

## List
```
koyeb apps list [flags]
```
No command-specific flags.

## Get/Describe
```
koyeb apps get NAME [flags]
koyeb apps describe NAME [flags]
```
No command-specific flags.

## Create
```
koyeb apps create NAME [flags]
  --delete-when-empty   Auto-delete app after last service deleted
```

## Update
```
koyeb apps update NAME [flags]
  --delete-when-empty   Auto-delete app after last service deleted
  -D, --domain string   Change subdomain (without .koyeb.app)
  -n, --name string     Change app name
```

## Init (Create App and Service)
```
koyeb apps init NAME [flags]
```
Uses the same flags as `koyeb services create` for the service portion.

## Pause/Resume
```
koyeb apps pause NAME [flags]
koyeb apps resume NAME [flags]
```
No command-specific flags.

## Delete
```
koyeb apps delete NAME [flags]
```
No command-specific flags.
