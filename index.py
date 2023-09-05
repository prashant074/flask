from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form['username']
        pw = request.form['password']
        if data == 'admin' and pw == 'admin':
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
        print(data) 
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)