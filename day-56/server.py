from flask import Flask, render_template
app = Flask(__name__)

# chrome developer -> console -> document.body.contentEditable=true
# need to save website with changes and add it back into code for updates

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
