from flask import Flask, request, jsonify
from link_summarizer import get_summarized_documents
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/link_summarizer', methods=['POST'])
def chat():
    input_text = request.json['message']
    response = get_summarized_documents(input_text)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)