from crypt import methods
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def hello(id: int):
    return jsonify({"id": id,"nome": "Rafael"})

@app.route('/soma', methods=['POST'])
def soma():
    if request.method == 'POST':
        listValues = json.loads(request.data)['valores']
        soma = sum(listValues)

        return jsonify({'Soma': soma})
    else:
        return ''

if __name__ == '__main__':
    try:
        app.run(debug=True)
        print('running')
    except Exception as error:
        print(error.message)