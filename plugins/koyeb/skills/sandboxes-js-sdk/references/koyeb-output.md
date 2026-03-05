# Output and formatting

When automation is required, prefer JSON output if supported:

```
koyeb <resource> list --output json
```

If JSON output is unavailable, parse tabular output carefully and avoid assumptions about column order.
