from flask import Flask, render_template, url_for
import requests



app=Flask(__name__)

blog_url="https://api.npoint.io/bd3389b6ea02b071067c"
response=requests.get(blog_url)
blog_post_json=response.json()


@app.route("/")
def home():
    
    return render_template("index.html", blogs=blog_post_json)

# @app.post("/")
# def home(blog_number):
#     blog_number=int(blog_number) - 1
#     # # if int(blog_number) > len(blog_post_json):
#     #     pass
#     # else:
#     #     return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__=="__main__":
    app.run(debug=True)