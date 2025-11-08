from flask import Flask, request, jsonify
from main import CodebaseGenius

app = Flask(__name__)
genius = CodebaseGenius()

@app.route('/analyze', methods=['POST'])
def analyze_repo():
    data = request.json
    github_url = data.get('github_url')
    
    if not github_url:
        return jsonify({"error": "github_url is required"}), 400
    
    result = genius.analyze_repository(github_url)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)