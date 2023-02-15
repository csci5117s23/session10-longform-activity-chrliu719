from flask import Flask, request, render_template

# instance of flask, the server
app = Flask(__name__)

@app.route('/')
def fanpage():
  return render_template('fanpage.html') 