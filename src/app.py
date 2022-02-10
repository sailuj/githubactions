from flask import


app = flask(__name__)

@app.rout("/")
def index():
    retun "Hello, world!"


if __name__ "__main__":
    app.run()
