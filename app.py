from icecream import ic
from flask import Flask

array = [10, 20, 30, 40]
print(array)
ic(array)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Ma Koré'

if __name__ == '__main__':
    app.run(debug=True)

