from flask import Flask, request, redirect
import os
app = Flask(__name__)

DATA_FILE = './board-data.txt'

@app.route('/')
def index():
  message = 'no message'
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'rt') as f:
      message = f.read()

  return """
    <html><body>
      <h1>Message Board</h1>
      <div>{0}</div>
      <h3>Update Board</h3>
      <form action="/write" method="POST">
        <textarea name="message" rows="6" cols="60"></textarea><br />
        <input type="submit" value="write">
      </form>
    </body><html>
  """.format(message)

@app.route('/write', methods=['POST'])
def write():
  if 'message' in request.form:
    message = str(request.form['message'])
    with open(DATA_FILE, 'wt') as f:
      f.write(message)

  return redirect('/')

@app.route('/user/<user_id>')
def users(user_id):
  return "user {0}'s page".format(user_id)

if __name__ == '__main__':
  app.run(host='0.0.0.0')
