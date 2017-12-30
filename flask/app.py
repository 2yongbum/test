from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'
    
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name='world'):
    return render_template('page.html', name=name)
    
@app.route('/post/<int:post_id>')
def show_port(post_id):
    return 'Post %d' % post_id
    
@app.route('/sanding', methods=['POST', 'GET'])
def sanding():
    return str(request.args)
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
  
