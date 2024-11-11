import flask as fk

app = fk.Flask(__name__)
@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)