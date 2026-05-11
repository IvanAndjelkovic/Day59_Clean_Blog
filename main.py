from flask import Flask, render_template, url_for


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<string:name_page>")
def page(name_page):
    
    return render_template(f"{name_page}.html")


if __name__=="__main__":
    app.run(debug=True)