from flask import Flask, request, jsonify
import cohere

co - cohere.Client('cUkUMhISEr8QsUhZ8uaVMxZtdL3UJrlaESCyNtHR')

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Starhopper!"

def cohere_process(question):
    # Cohere API functionality
    response = co.generate(prompt=question, max_tokens=50)
    return response.text

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get("question")
    answer = cohere_process(question)
    return jsonify({"answer": "This is a placeholder response", "source": "Placeholder source"})

if __name__ == '__main__':
    app.run(debug=True)
