# Start Here
## Step 1
Create GitHub repo `sentinelx`, upload this structure, then protect `main` and `develop`.

## Step 2
Replace usernames in `.github/CODEOWNERS`.

## Step 3
Create first branches:
```bash
git switch -c develop
git push -u origin develop

git switch develop
git switch -c security/event-schema-v1
```

## First milestone
Freeze `schemas/events/security-event-v1.schema.json`, then build Scenario A: failed logins -> successful login -> suspicious PowerShell -> incident -> explanation -> simulated response.
