from flask import Flask

app = Flask(__name__)
app.config['DEBuG'] = True

@app.route("/")
def index():
    return


app.run()