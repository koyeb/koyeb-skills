# Expected Behavior (Claude Code)

## 1. List apps
- Uses `apps` skill
- Runs: `koyeb app list`

## 2. Create app + service
- Uses `apps` then `services` skills
- Runs: `koyeb app create demo-app`
- Then: `koyeb service create demo-app ...` (asks for required config)

## 3. Pause app
- Uses `apps` skill
- Runs: `koyeb app pause demo-app`
- Confirms with `koyeb app get demo-app` or `koyeb app describe demo-app`

## 4. Service logs
- Uses `services` skill
- Runs: `koyeb service logs demo-service`

## 5. Deploy service
- Uses `deploy` skill or `services` skill
- Runs: `koyeb service deploy demo-service ...` or `koyeb service redeploy demo-service`

## 6. Attach domain
- Uses `domains` skill
- Runs: `koyeb domain attach example.com --service demo-service`

## 7. Secret create + reveal
- Uses `secrets` skill
- Runs: `koyeb secret create DATABASE_URL --value "postgres://..."`
- Then: `koyeb secret reveal DATABASE_URL`

## 8. Deployments list + logs
- Uses `deployments` skill
- Runs: `koyeb deployment list --service demo-service`
- Then: `koyeb deployment logs <deployment-id>`

## 9. Instances list + exec
- Uses `instances` skill
- Runs: `koyeb instance list --service demo-service`
- Then: `koyeb instance exec <instance-id> -- ls -la`

## 10. Volumes
- Uses `volumes` skill
- Runs: `koyeb volume create data-vol ...`
- Then: `koyeb volume list`

## 11. Databases
- Uses `databases` skill
- Runs: `koyeb database create demo-db ...`
- Then: `koyeb database list`

## 12. CLI version
- Uses `version` skill
- Runs: `koyeb version`
