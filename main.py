from flask import Flask, render_template, url_for
import requests



app=Flask(__name__)

blog_url="https://api.npoint.io/3edc27e6e4f05fef7d0c"
response=requests.get(blog_url)
blog_post_json=response.json()



@app.route("/")
def home():
    
    return render_template("index.html", blogs=blog_post_json)

@app.route("/post/<int:blog_id>")
def show_post(blog_id):
    return render_template("post.html", blog=blog_post_json[blog_id-1])




@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")




if __name__=="__main__":
    app.run(debug=True)