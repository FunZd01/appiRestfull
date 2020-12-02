from flask import Flask, jsonify,request

'''practica CRUD, con flask'''

app= Flask(__name__)

#importando base de datos emulada
from products import products

@app.route('/')
def index():
    return 'home'

@app.route('/products')
def getProducts():
    return jsonify( products )

@app.route('/products/<string:product_name>')
def Read(product_name):
    found = [ product for product in products if product['name']==product_name ]

    if found:
        return jsonify({ "product": found[0] })
    else:
        return 'no encontrado!'


@app.route('/products',methods=["POST"])
def Create():
    new_product = {
        "name": request.json["name"],
        "price": request.json[ "price" ],
        "quantity": request.json[ "quantity" ],
    }
    products.append(new_product)#agrega el nuevo elemento a la lista
    return "agregado exitoso"

@app.route('/products/<string:product_name>', methods=["PUT"])
def update(product_name):
    found = [ product for product in products if product['name'] == product_name ]

    if found:
        found[0][ "name" ] = request.json['name']
        found[0][ "price" ] = request.json['price']
        found[0][ "quantity" ] = request.json[ 'quantity' ]

        return 'editado correctamente!'
    else:
        return 'no encontrado!'

@app.route('/products/<string:product_name>', methods=['delete'])
def delete(product_name):
    # busca coincidencias
    found = [product for product in products if product_name==product['name']]
    
    if found:
        products.remove( found[0] )
        return jsonify({ "message": 'eliminado exitoso', "products ": products })
    
    return 'no existe el dato!'

if __name__ == "__main__":
    app.run(debug= True) 