from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Path to the text file
TEXT_FILE = 'editable_text.txt'

# Load text from file
def load_text():
    try:
        with open(TEXT_FILE, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

# Save text to file
def save_text(text):
    with open(TEXT_FILE, 'w') as file:
        file.write(text)

@app.route('/')
@app.route('/index.html') # get method
def index():
    text = load_text()
    return render_template('index.html', the_title='Text Editor', text=text)

@app.route('/save', methods=['POST'])
def save():
    text = request.form['editor']
    save_text(text)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
