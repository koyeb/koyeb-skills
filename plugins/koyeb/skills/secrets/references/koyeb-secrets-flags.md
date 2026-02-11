# Secrets Command Flags Reference

Complete reference for all `koyeb secrets` command flags.

## List/Get/Describe
```
koyeb secrets list [flags]
koyeb secrets get NAME [flags]
koyeb secrets describe NAME [flags]
```

## Create
```
koyeb secrets create NAME [flags]
  --registry-keyfile string     Registry keyfile (for registry-gcp)
  --registry-name string        Registry name (for registry-azure)
  --registry-password string    Registry password (for registry-*)
  --registry-url string         Registry URL (for registry-private, registry-gcp)
  --registry-username string    Registry username (for registry-*)
  --type string                 Type: simple, registry-dockerhub, registry-private, registry-digital-ocean, registry-gitlab, registry-gcp, registry-azure (default: "simple")
  -v, --value string            Secret value
  --value-from-stdin            Read value from stdin
```

## Update
```
koyeb secrets update NAME [flags]
  --registry-keyfile string     Registry keyfile (for registry-gcp)
  --registry-name string        Registry name (for registry-azure)
  --registry-password string    Registry password (for registry-*)
  --registry-url string         Registry URL (for registry-private, registry-gcp)
  --registry-username string    Registry username (for registry-*)
  -v, --value string            New secret value
  --value-from-stdin            Read value from stdin
```

## Reveal
```
koyeb secrets reveal NAME [flags]
```

## Delete
```
koyeb secrets delete NAME [flags]
```
