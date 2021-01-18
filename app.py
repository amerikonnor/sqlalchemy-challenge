from flask import Flask

app = Flash(__name__)

@app.route("/")
def index():
    return 'Welcome to my homepage!'