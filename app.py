from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///IOT.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db=SQLAlchemy(app)

class Iot(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    mail=db.Column(db.String(100),nullable=False)
    name=db.Column(db.String(50),nullable=False)
    
def __repr__(self) -> str:
    return f"{self.sno}-{self.mail}"

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        mail1=request.form['mail1']
        name1=request.form['name1']
        iot=Iot(mail=mail1,name=name1)
        db.session.add(iot)
        db.session.commit()
    alldat=Iot.query.all()
    return render_template('index.html',alldat=alldat)

@app.route('/delete/<int:sno>')
def delete(sno):
    dat=Iot.query.filter_by(sno=sno).first()
    db.session.delete(dat)
    db.session.commit()
    return redirect('/')

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method =="POST":
        mail1=request.form['mail1']
        name1=request.form['name1']
        dat=Iot.query.filter_by(sno=sno).first()
        dat.mail=mail1
        dat.name=name1
        db.session.add(dat)
        db.session.commit()
        return redirect('/')
    alldat=Iot.query.filter_by(sno=sno).first()
    return render_template('update.html',alldat=alldat)


if __name__=="__main__":
    app.run(debug=True)