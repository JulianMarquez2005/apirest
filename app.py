#vamos a traer un framework#
from flask import Flask, jsonify, request

app = Flask(__name__)
#este es mi servidor ahora vamos a inicializarlo#

#vamos a importar los productos#

from products import products

#crearemos una ruta de prueba para ver si esta funcionando mi servidor#
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong!"})

#crearemos una ruta para mandar un metodo get#
@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Product's List" })
#el servidor me esta respondiendo con mi lista de productos#

#haremos que solo nos devuelva el objeto deseado#

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    #recorremos nuestros productos si el nombre que nos estan dando coincide con el nombre de la lista lo va a retornar#
    productsFound = [product for product in products if product['name'] == product_name]
    #haremos una validacion#
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "Product not found"})
#crearemos otra ruta para añadir un dato#
@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

#ahora haremos que podamos actualizar un dato#
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    #recorremos los datos#
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})

#Ahora utilizaremos una ruta para eliminar#
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product ['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
        "message": "Product Deleted",
        "products": products
        })
    return jsonify({"message": "Product Not Found"})






if __name__ == '__main__':
    app.run(debug=True, port=5000)
