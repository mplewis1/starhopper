from flask import Flask, request, jsonify, render_template
import cohere
from integrations.box import search_box

co = cohere.Client('cUkUMhISEr8QsUhZ8uaVMxZtdL3UJrlaESCyNtHR')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def cohere_process(question):
    # Cohere API functionality
    response = co.generate(prompt=question, max_tokens=50)
    return response.text

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    question = data.get("question")
    box_developer_token = 'n3sDfWnjXDnjleep1OuJ2lewfj6DBhSU'
    box_results = search_box(question, box_developer_token)

    if box_results and box_results['entries']:
        first_result - box_results['entries'][0]
        file_info = f"File Name: {first_result['name']} (ID: {first_result['id']})"
    else:
        file_info = "No results found."
    
    answer = cohere_process(question)
    return jsonify({"answer": "This is a placeholder response", "source": "Placeholder source"})

if __name__ == '__main__':
    app.run(debug=True)
