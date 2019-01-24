from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    a='Khan'
    name= 'abc'
    list =['Mahesh','Durgesh','Kumawat']
    return render_template('tmp.html',name=name,list=list) + a
if __name__ =="__main__":
    app.run(debug = True)

