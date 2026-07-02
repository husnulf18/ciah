from flask import Flask, render_template

loveee = Flask(__name__)

@loveee.route('/')
def home():
    return render_template('home.html')

# Baris ini sangat penting agar Vercel tahu penamaan file Anda
app = loveee

if __name__ == "__main__":
    loveee.run(port=4444, debug=True)