from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def resume():
    return render_template('resume.html', title='Моє резюме')

@app.route('/contacts', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return f"<h2>Дякую, {name}! Ваше повідомлення отримано.</h2>"
    return render_template('contacts.html', title='Контакти')

if __name__ == '__main__':
    app.run(debug=True)