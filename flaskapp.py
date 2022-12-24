from flask import Flask,jsonify, request

app = Flask(__name__)

contactList = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9876543222', 
        'done': False
    }
]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            
        },400)

    contact = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    #append to the contactList
    return jsonify({
        
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : contactList
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
