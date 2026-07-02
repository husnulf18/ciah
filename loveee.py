from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    # Menambahkan port=4444 di dalam app.run
    app.run(port=4444, debug=True)