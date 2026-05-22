from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = open(os.path.join(os.path.dirname(__file__), '..', 'templates', 'index.html')).read()

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(debug=True)
