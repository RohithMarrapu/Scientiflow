from flask import Flask, jsonify
from ec2_manager import launch_instance, terminate_instance

app = Flask(__name__)
instance_map = {}

@app.route("/launch", methods=["POST"])
def launch():
    instance = launch_instance()
    instance_map['id'] = instance.id
    return jsonify({"message": "Instance launched", "id": instance.id})

@app.route("/terminate", methods=["POST"])
def terminate():
    if 'id' not in instance_map:
        return jsonify({"error": "No instance to terminate"}), 400
    terminate_instance(instance_map['id'])
    return jsonify({"message": "Instance terminated"})

if __name__ == "__main__":
    app.run(debug=True)
