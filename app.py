#for backend, we made this file
from flask import Flask
app = Flask(__name__)
@app.route('/')
def new():
    return "Job tracker is running"

if __name__ == '__main__':
    app.run(debug=True,port=5000)