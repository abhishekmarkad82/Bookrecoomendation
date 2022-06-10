from flask import Flask,render_template,request
import pickle
popular=pickle.load(open("popular_books.pkl","rb"))
#print(list(popular["Book-Title"]))
app=Flask(__name__) 

@app.route("/")
def index():
    return render_template("index.html",
     books=list(popular["Book-Title"].values),
     authors=list(popular["Book-Author"].values),
     votes=list(popular["count"].values),
     ratings=list(popular["mean"].values),
     images=list(popular["Image-URL-M"].values)
    )

@app.route("/recommend")
def recommend():
    return render_template("recommend.html")    
@app.route("/*")
def random():
    return "Not found"

if(__name__=="__main__"):
    app.run()    
