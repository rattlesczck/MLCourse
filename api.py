## Put and delete --> HTTP verbs
## Working with API's --> JSON


from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in the to do list

items = [
    {"id":1, "name":"Item1", "description":"This is item 1"},  
    {"id":2, "name":"Item2", "description":"This is item 2"}
]

@app.route("/")
def home():
    return f"Welcome to the TO-DO List app"

## Retrieve all items
@app.route("/items",methods= ['GET'])
def getitems():
    return jsonify(items)

## retrieve specific items by id
@app.route("/items/<int:itemid>", methods=['GET'])
def getitem(itemid):
    item = next((item for item in items if item["id"]==itemid), None)
    if item == None:
        return jsonify({"error": "item not found"})
    return jsonify(item)

@app.route("/items",methods=['POST'])
def createitem():
    if not request.json or not 'name' in request.json: 
        return jsonify({"error" : "item not found"})
    newitem = {
        "id": items[-1]["id"] +1 if items else 1,
        "name":request.json['name'],
        "description" : request.json['description']
        
        
    }
        
    items.append(newitem)
    return jsonify(newitem)

## Put --> update an existing items

@app.route("/items/<int:itemid>", methods=['PUT'])
def updateitem(itemid):
    item = next((item for item in items if item["id"]==itemid), None)
    
    if item is None:
        return jsonify({"error":"item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

@app.route("/items/<int:itemid>", methods = ['DELETE'])
def deleteitem(itemid):
    global items
    items = [item for item in items if item['id']!=itemid]   
    return jsonify({"result":"Item deleted successfully"})
    

if __name__ == "__main__":
    app.run(debug=True)