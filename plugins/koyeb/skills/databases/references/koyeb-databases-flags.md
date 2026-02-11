# Databases Command Flags Reference

Complete reference for all `koyeb databases` command flags.

## List
```
koyeb databases list [flags]
```

## Get
```
koyeb databases get NAME [flags]
  --app string      App context (format: app-name/database-name)
```

## Create
```
koyeb databases create NAME [flags]
  --app string            App context (format: app-name/database-name)
  --db-name string        Database name (default: "koyebdb")
  --db-owner string       Database owner (default: "koyeb-adm")
  --instance-type string  Instance type: free, small, medium, large (default: "free")
  --pg-version int        PostgreSQL version (default: 16)
  --region string         Deploy region (default: "was")
```

## Update
```
koyeb databases update NAME [flags]
  --app string            App context (format: app-name/database-name)
  --instance-type string  Instance type: free, small, medium, large (default: "free")
  --name string           New database name
```

## Delete
```
koyeb databases delete NAME [flags]
```
