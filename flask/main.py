from flask import Flask , render_template , request
app = Flask(__name__)
# data = {"Square":["Area:"],"Rectangle":["auidchq"],"Triangle":["auidchq"],"Parallelogram":["auidchq"],"Circle":["auidchq"],"Rhombus":["auidchq"],"Trapezoid":["auidchq"]}

@app.route("/")
def hello():
    return render_template("form.html")
@app.route("/submit/")
def anwer():
    if request.args.get("shape"):
        global lis
        lis = request.args.get("shape")
        
        if lis == "square":
            return render_template("form_sq.html")
        if lis == "rectangle":
            return render_template("form_rec.html")
        if lis == "triangle":
            return render_template("form_tria.html")

@app.route("/submit/shape")
def out():
    if lis == "square":
        
        if request.args.get("side"):
            a = int(request.args.get("side"))
            area = a*a
            perimeter = 4*a
            return (f'Area is: {area}, Perimeter is: {perimeter}')
    if lis == "rectangle":
        
        if request.args.get("length") and request.args.get("breadth"):
            a = int(request.args.get("length"))
            b = int(request.args.get("breadth"))
            area = a*b
            perimeter = 2*(a+b)
            return (f'Area is: {area}, Perimeter is: {perimeter}')
    if lis == "triangle":
        if request.args.get("1st co-ordinate") and request.args.get("2nd co-ordinate") and request.args.get("3rd co-ordinate") and request.args.get("Base") and request.args.get("Height"):
            x = int(request.args.get("1st co-ordinate"))
            y = int(request.args.get("2nd co-ordinate"))
            z = int(request.args.get("3rd co-ordinate"))
            a = int(request.args.get("Base"))
            b = int(request.args.get("Height"))
            area = 0.5*(a*b)
            perimeter = x+y+z
            return (f'Area is: {area}, Perimeter is: {perimeter}')
            

app.run()