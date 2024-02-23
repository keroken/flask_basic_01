from flask import Flask, request, session, redirect
app = Flask(__name__)
app.secret_key = '9KStWezC' # random key

@app.route('/')
def index():
  # input form for user name
  return """
  <html><body><h1>Input User Name</h1>
  <form action="/setname" method="GET">
    User Name: <input type="text" name="username">
    <input type="submit" value="Start">
  </form></body></html>
  """

@app.route('/setname')
def setname():
  # get user name
  name = request.args.get('username')
  if not name: return redirect('/')
  # save name to session
  session['name'] = name
  # redirect to another page
  return redirect('/morning')

def getLinks():
  return """
  <ul><li><a href="/morning">Morning Greeting</a></li>
  <li><a href="/hello">Afternoon Greeting</a></li>
  <li><a href="/night">Night Greeting</a></li></ul>
  """

@app.route('/morning')
def morning():
  if not ('name' in session):
      return redirect('/')
  return """
  <h1>Good morning, {0}!</h1>{1}
  """.format(session['name'], getLinks())

@app.route('/hello')
def hello():
  if not ('name' in session):
      return redirect('/')
  return """<h1>Hello, {0}!!</h1>{1}
  """.format(session['name'], getLinks())

@app.route('/night')
def night():
  if not ('name' in session):
      return redirect('/')
  return """<h1>Good evening, {0}!!!</h1>{1}
  """.format(session['name'], getLinks())

if __name__ == '__main__':
  app.run(host='0.0.0.0')
