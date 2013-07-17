import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Let\'s see how long you have lived in days, minutes and seconds.'