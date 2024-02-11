from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# MongoDB connection
client = MongoClient("mongodb+srv://blackloin:naruto45@cluster0.fmktl.mongodb.net/?retryWrites=true&w=majority")
db = client['keytechlabs']  # Assuming 'keytechlabs' is the correct database
components_collection = db['components_collection']
checklist_tech_collection = db['Checklist_tech']
powershell_checklist_collection = db['powershell_Checklist']

@app.route('/getChecklist/<path:url>', methods=['GET'])
def get_checklist(url):
    # Assuming the 'url' field in your documents
    document = checklist_tech_collection.find_one({"url": url})
    if document:
        document['_id'] = str(document['_id'])  # Convert ObjectId to string for JSON serialization
        return jsonify(document)
    else:
        return jsonify({"error": "Document not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
