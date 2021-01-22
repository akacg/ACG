from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="User Form")

@app.route('/details')
def details():
    form=forms.AddPersonForm
    return render_template('details.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)