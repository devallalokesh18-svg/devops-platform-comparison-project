from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)
tasks = [
    {"id": 1, "title": "Learn Git", "status": "Done"},
    {"id": 2, "title": "Build CI/CD pipeline", "status": "In Progress"},
]

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": len(tasks)+1, "title": title, "status": "Pending"})
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Done"
    return redirect(url_for("index"))

@app.route("/api/health")
def health():
    return jsonify({"status":"healthy","application":"DevOps Platform Comparison",
                    "timestamp":datetime.utcnow().isoformat()+"Z"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
