from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
  {
    'id': 1,
    'title': 'Data analyst',
    'location': 'San Francisco, USA',
    'salary': 'USD 100,000'
  },
  {
    'id': 2,
    'title': 'Data scientist',
    'location': 'New Delhi, India',
    'salary': 'USD 150,000'
  },
  {
    'id': 1,
    'title': 'Front-end engineer',
    'location': 'Remote',
  },
  {
    'id': 1,
    'title': 'Backend engineer',
    'location': 'San Francisco, USA',
    'salary': 'USD 120,000'
  }
]

@app.route('/')
def hello_world():
  return render_template("home.html", roles = jobs)


@app.route('api/jobs')
def list_jobs():
  return jsonify(jobs)

if __name__ == "__main__":
  app.run(host = '0.0.0.0' ,debug = True)