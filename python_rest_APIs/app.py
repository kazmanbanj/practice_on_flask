from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': 'My item',
                'price': 15.00
            }
        ]
    }
]

@app.route('/')
def home():
    """
    docstring
    """
    return render_template('index.html')


# POST - used to receive data
# GET - used to send data back only


# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    """
    docstring
    """
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)



# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    """
    docstring
    """
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})



# GET /store
@app.route('/store')
def get_stores():
    """
    docstring
    """
    return jsonify({'stores': stores})



# POST /store/<string:name>/item {name: price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item():
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})



# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    """ 
    docstring
    """
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})



app.run(port=5000)