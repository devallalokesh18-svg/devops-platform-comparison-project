# FACULTY DEMO GUIDE

1. Start:
`pip install -r requirements.txt`
`python app.py`

2. Open http://127.0.0.1:5000 and demonstrate adding/completing a task.

3. Run:
`pytest -q`

4. Show:
- Dockerfile
- .github/workflows/ci.yml
- .gitlab-ci.yml
- bitbucket-pipelines.yml

5. Explain:
GitHub -> GitHub Actions
GitLab -> GitLab CI/CD
Bitbucket -> Bitbucket Pipelines

6. Create a feature branch, make a small change, commit and push it. Create a Pull Request/Merge Request and show the CI result.

7. Build:
`docker build -t student-devops-app .`
