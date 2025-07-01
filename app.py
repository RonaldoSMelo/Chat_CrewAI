from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'CrewAI Chat App - Simple Test Version'})

@app.route('/run', methods=['GET'])
@app.route('/run/', methods=['GET'])
def run():
    return jsonify({'status': 'running'}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'service': 'crewai-chat'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 