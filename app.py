from flask import Flask, jsonify, request

app = Flask(__name__)


stores = [
    {
        'name': 'default-store',
        'items': [
            {
                'item_name': 'default-item',
                'price': 200
            }
        ]
    }
]


# POST /store -> name
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    store = {
        'name': data['name'],
        'items': []
    }
    stores.append(store)
    return jsonify(store)


# GET /store/<name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<name>/item -> name, price
@app.route('/store/<name>/item', methods=['POST'])
def create_item(name):
    for store in stores:
        if store['name'] == name:
            data = request.get_json()
            item = {
                'item_name': data['item_name'],
                'price': data['price']
            }
            store['items'].append(item)
            return jsonify(item)
    return jsonify({'message': 'store not found'})


# GET /store/<name>/item
@app.route('/store/<name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run(debug=True)