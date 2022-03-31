
from flask import Flask, jsonify, request
app = Flask(__name__)
task = [{
    "id":1,
    "title":u"computer science",
    "description":u"coding",
    "done":False
},

{
    "id":2,
    "title":u"Math",
    "description":u"numbers",
    "done":False
}]
@app.route("/add_data", methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"not working!"

        },400)
    task1={
        "id":task[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description","empty"),
        "done":False
    }
    task.append(task1)
    return jsonify({
        "status":"sucses",
        "message":"task added"
    })
@app.route("/get_data")
def get_task():
    return jsonify({
        "data":task
    })
if __name__ == "__main__":
    app.run(debug=True)