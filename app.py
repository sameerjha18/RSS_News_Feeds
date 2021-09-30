from flask import Flask
from rss import rss

app = Flask(__name__)
app.register_blueprint(rss)