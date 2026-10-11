# COMMAND CHEAT SHEET
python -m venv .venv
pip install -r requirements.txt
pytest -q
python app.py

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_URL
git push -u origin main
git checkout -b feature/new-feature
git push -u origin feature/new-feature

docker build -t student-devops-app .
docker run -p 5000:5000 student-devops-app
