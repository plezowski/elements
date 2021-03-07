from flask import Flask, render_template
import markdown
import os, sys
import random

app = Flask(__name__)

with open("liste.md", "r", encoding="utf-8") as f:
    fichier_markdown = markdown.markdown(f.read(), extensions=["tables"])


@app.route("/")
def index():
    return render_template(
        "index.html", nom=sys.argv[1], fichier_markdown=fichier_markdown
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))