from flask import Flask , render_template , request
import joblib

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("home.html")


@app.route("/predict" , methods=["post"])
def predict():

    model = joblib.load("diabetic_80.pkl")

    preg = request.form.get("preg")
    plas = request.form.get("plas")
    pres = request.form.get("pres")
    skin = request.form.get("skin")
    test = request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")
    
    output = model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])

    if output[0]==0:
        data = "not diabetic"
    else:
        data = "diabetic"

    return render_template("predict.html" , data = data)



app.run(debug = True)