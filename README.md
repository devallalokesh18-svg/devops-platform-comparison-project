# DevOps Platform Comparison - Complete Project

**Topic:** Compare GitHub, GitLab, and Bitbucket by managing a sample software project.

This is ONE working Flask application demonstrating Git, branches, code review, automated testing, Docker and CI/CD.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
python app.py
```
Open http://127.0.0.1:5000

If PowerShell blocks activation:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Git workflow
```bash
git init
git add .
git commit -m "Initial project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
git checkout -b feature/new-feature
git add .
git commit -m "Add new feature"
git push -u origin feature/new-feature
```
Create a Pull Request on GitHub/Bitbucket or Merge Request on GitLab.

## Docker
```bash
docker build -t student-devops-app .
docker run -p 5000:5000 student-devops-app
```

## CI/CD
GitHub: `.github/workflows/ci.yml` -> GitHub Actions
GitLab: `.gitlab-ci.yml` -> GitLab CI/CD
Bitbucket: `bitbucket-pipelines.yml` -> Bitbucket Pipelines

Pipeline: Checkout -> Install -> Test -> Docker Build

## Comparison
| Feature | GitHub | GitLab | Bitbucket |
|---|---|---|---|
| Git hosting | Yes | Yes | Yes |
| Code review | Pull Request | Merge Request | Pull Request |
| CI/CD | GitHub Actions | GitLab CI/CD | Bitbucket Pipelines |
| Issues | Yes | Yes | Yes |
| Project management | Projects | Boards/Issues | Jira integration |
| Strongest ecosystem | Developer/Open source | Integrated DevOps | Atlassian |

## Demo
1. Run the app.
2. Run `pytest -q`.
3. Show Git history and branches.
4. Show Dockerfile.
5. Show the three CI/CD files.
6. Push to a platform.
7. Create a feature branch and Pull/Merge Request.
8. Show the automated pipeline.
9. Explain the comparison.
