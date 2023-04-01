from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
    'id' : 1,
    'title' : 'Backend Engineer',
    'location' : 'San Francisco, USA',
    'salary' : '$120,000'
    },
    {
    'id' : 2,
    'title' : 'Frontend Engineer',
    'location' : 'Remotely',
    'salary' : '$12,000'
    },
    {
    'id' : 3,
    'title' : 'Data Analysis',
    'location' : 'Remotely',
    'salary' : '$220,000'
    }
]

@app.route("/")
def hello_pine():
    return render_template('home.html', jobs=JOBS, company_name='Pine')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)