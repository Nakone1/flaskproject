from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = '90667433b3bc0dd06025e5b4e1f6cf5d'

@app.route("/home")
def home():
    return render_template('home.html') 

@app.route("/about")
def about():
    return render_template('about.html', title='About')   

if __name__ == '__main__':
	app.run(debug=True)