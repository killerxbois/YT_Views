
from flask import Flask, request, render_template_string
from datetime import datetime
import os

app = Flask(__name__)
ADMIN_PASSWORD = "Admin0110409"

HTML = """
<!DOCTYPE html>
<html>
<head><title>YT Views Admin</title></head>
<body>
    <h2>YT Views - Admin Panel</h2>
    {% if not authorized %}
    <form method="POST">
        <input type="password" name="password" placeholder="Admin Password" required>
        <input type="submit" value="Login">
    </form>
    {% else %}
    <h3>Recent Logs</h3>
    <pre>{{ logs }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def admin():
    authorized = False
    logs = ""
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            authorized = True
            if os.path.exists("logs/requests.log"):
                with open("logs/requests.log") as f:
                    logs = f.read()
            else:
                logs = "No logs yet."
    return render_template_string(HTML, authorized=authorized, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
