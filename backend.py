from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In a real application, you'd use a database
feedback_data = []

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    try:
        data = request.form.to_dict()
        # Add timestamp
        data['timestamp'] = datetime.now().isoformat()
        feedback_data.append(data)
        
        # Save to file (in production, use database)
        with open('feedback.json', 'w') as f:
            json.dump(feedback_data, f, indent=2)
        
        return jsonify({'status': 'success', 'message': 'Feedback submitted successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/get-feedback', methods=['GET'])
def get_feedback():
    return jsonify(feedback_data), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)