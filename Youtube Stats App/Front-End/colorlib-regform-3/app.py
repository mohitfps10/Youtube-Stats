from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")


@app.route('/result',methods = ['GET','POST'])
def result():
  
    if request.method == 'POST':
      id1 = request.form["Channel Id"]
      
      return render_template("pass.html",id1 = id1)
     
      
if __name__ == '__main__':
   app.run(debug = True)