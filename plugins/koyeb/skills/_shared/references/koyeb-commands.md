#+#+#+#+ new content below
# Koyeb CLI - Command Index

Quick reference for all Koyeb CLI commands. For detailed flags, see the individual skill references.

## Global Flags

These flags are available on all commands:

- `-c, --config string` - Config file (default: `$HOME/.koyeb.yaml`)
- `-d, --debug` - Enable debug output
- `--debug-full` - Do not hide sensitive information in debug output
- `--force-ascii` - Only output ASCII characters
- `--full` - Do not truncate output
- `-h, --help` - Help for command
- `-o, --output string` - Output format: `yaml`, `json`, or `table` (default: `table`)
- `--organization string` - Organization ID
- `--token string` - API token
- `--url string` - API URL (default: `https://app.koyeb.com`)

## Command Index

### Apps
- `koyeb apps list` - List all apps
- `koyeb apps get NAME` - Get app details
- `koyeb apps describe NAME` - Describe app
- `koyeb apps create NAME` - Create new app
- `koyeb apps init NAME` - Create app and service in one command
- `koyeb apps update NAME` - Update app configuration
- `koyeb apps pause NAME` - Pause app
- `koyeb apps resume NAME` - Resume app
- `koyeb apps delete NAME` - Delete app

### Services
- `koyeb services list` - List services
- `koyeb services get NAME` - Get service details
- `koyeb services describe NAME` - Describe service
- `koyeb services create NAME` - Create service
- `koyeb services update NAME` - Update service
- `koyeb services delete NAME` - Delete service
- `koyeb services pause NAME` - Pause service
- `koyeb services resume NAME` - Resume service
- `koyeb services logs NAME` - Get service logs
- `koyeb services exec NAME CMD` - Execute command in service
- `koyeb services redeploy NAME` - Redeploy service
- `koyeb services unapplied-changes NAME` - Show pending changes

### Secrets
- `koyeb secrets list` - List secrets
- `koyeb secrets get NAME` - Get secret
- `koyeb secrets describe NAME` - Describe secret
- `koyeb secrets create NAME` - Create secret
- `koyeb secrets update NAME` - Update secret
- `koyeb secrets reveal NAME` - Reveal secret value
- `koyeb secrets delete NAME` - Delete secret

### Domains
- `koyeb domains list` - List domains
- `koyeb domains get NAME` - Get domain details
- `koyeb domains describe NAME` - Describe domain
- `koyeb domains create NAME` - Create domain
- `koyeb domains attach NAME APP` - Attach domain to app
- `koyeb domains detach NAME` - Detach domain from app
- `koyeb domains refresh NAME` - Refresh domain verification
- `koyeb domains delete NAME` - Delete domain

### Deployments
- `koyeb deployments list` - List deployments
- `koyeb deployments get NAME` - Get deployment details
- `koyeb deployments describe NAME` - Describe deployment
- `koyeb deployments logs NAME` - Get deployment logs
- `koyeb deployments cancel NAME` - Cancel deployment

### Instances
- `koyeb instances list` - List instances
- `koyeb instances get NAME` - Get instance details
- `koyeb instances describe NAME` - Describe instance
- `koyeb instances logs NAME` - Get instance logs
- `koyeb instances exec NAME CMD` - Execute command in instance
- `koyeb instances cp SRC DST` - Copy files to/from instance

### Databases
- `koyeb databases list` - List databases
- `koyeb databases get NAME` - Get database details
- `koyeb databases create NAME` - Create PostgreSQL database
- `koyeb databases update NAME` - Update database
- `koyeb databases delete NAME` - Delete database

### Volumes
- `koyeb volumes list` - List volumes
- `koyeb volumes get NAME` - Get volume details
- `koyeb volumes create NAME` - Create volume
- `koyeb volumes update NAME` - Update volume
- `koyeb volumes delete NAME` - Delete volume

### Archives
- `koyeb archives create NAME` - Create archive from directory

### Organizations
- `koyeb organizations list` - List organizations
- `koyeb organizations switch` - Switch organization context

### Deploy
- `koyeb deploy PATH APP/SERVICE` - Deploy directory to Koyeb

### Version
- `koyeb version` - Show CLI version


<!-- Detailed deploy flags moved to per-skill references. -->
