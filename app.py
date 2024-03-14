from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/pages/home.html')

@app.route('/what-i-do')
def what_i_do():
    return render_template('/pages/what-i-do.html')

@app.route('/projects')
def projects():
    return render_template('/pages/projects.html')

@app.route('/blog')
def blog():
    return render_template('/pages/blog.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)