from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample in-memory database
items = [
    {"id": 1, "name": "Apple", "price": 200},
    {"id": 2, "name": "Banana", "price": 120}
]

# 1. GET - Fetch all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# 2. GET - Fetch a single item by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# 3. POST - Add a new item
@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    new_item = {
        "id": len(items) + 1,
        "name": data.get("name"),
        "price": data.get("price")
    }
    items.append(new_item)
    return jsonify(new_item), 201

# 4. PUT - Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item["name"] = data.get("name", item["name"])
            item["price"] = data.get("price", item["price"])
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# 5. DELETE - Remove an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
