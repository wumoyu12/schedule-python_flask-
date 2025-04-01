from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/process', methods=['POST'])
def process():
    schedule = []
    for period in range(1, 9):
        course = request.form.get(f'course{period}', 'N/A')
        teacher = request.form.get(f'teacher{period}', 'N/A')
        room = request.form.get(f'room{period}', 'N/A')
        schedule.append([f'Period {period}', course, teacher, room])
    
    return render_template('output.html', schedule=schedule)

if __name__ == '__main__':
    app.run()
