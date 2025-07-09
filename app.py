from flask import Flask, send_from_directory
import os

app = Flask(name, static_folder='public')

@app.route('/')
def catalog():
    return send_from_directory('public', 'catalog.html')

if name == 'main':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
