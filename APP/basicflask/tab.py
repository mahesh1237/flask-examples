from flask import Flask, render_template
app = Flask(__name__)
@app.route('/table')
def table():
   diction={'maths':73,'C':58,'Java':55}
   print(diction)
   return render_template('table.html',table = diction) 
if __name__ =="__main__":
    app.run(debug = True)
