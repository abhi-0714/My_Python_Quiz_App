from flask import Flask, render_template, request

app = Flask(__name__)

# Define your questions
questions = [
    {"question": "In which continent does India lie", "options": ["Asia", "Africa", "Europe"], "answer": "Asia"},
    {"question": "What OS does Macbook's use?", "options": ["Android", "Mac OS", "Windows"], "answer": "Mac OS"},
    {"question": "Which company does not manufacture Fridge?", "options": ["Microsoft", "Samsung", "LG"], "answer": "Microsoft"}
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'question{i+1}')
        if user_answer == q['answer']:
            score += 1
    return f'You got {score}/{len(questions)} correct.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

