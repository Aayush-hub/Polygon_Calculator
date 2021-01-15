from flask import Flask , render_template , request
import math
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("form.html")

@app.route("/submit/")
def anwer():
    if request.args.get("shape"):
        global lis
        lis = request.args.get("shape").lower()
        
        if lis == "square":
            return render_template("form_sq.html")
        if lis == "rectangle":
            return render_template("form_rec.html")
        if lis == "triangle":
            return render_template("form_tria.html")
        if lis == "parallelogram":
            return render_template("form_par.html")
        if lis == "circle":
            return render_template("form_ci.html")
        if lis == "rhombus":
            return render_template("form_rho.html")
        if lis == "trapezoid":
            return render_template("form_tra.html")


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
    
    if lis == "parallelogram":
        if request.args.get("1st side") and request.args.get("2nd side") and request.args.get("3rd side") and request.args.get("4th side") and request.args.get("Base") and request.args.get("Height"):
            x = int(request.args.get("1st side"))
            y = int(request.args.get("2nd side"))
            z = int(request.args.get("3rd side"))
            w = int(request.args.get("4th side"))
            a = int(request.args.get("Base"))
            b = int(request.args.get("Height"))
            area = a*b
            perimeter = x+y+z+w
            return (f'Area is: {area}, Perimeter is: {perimeter}')
    
    if lis == "circle":
        if request.args.get("radius"):
            a = int(request.args.get("radius"))
            area = round(math.pi*a*a,3)
            perimeter = round(2*math.pi*a,3)
            return (f'Area is: {area}, Perimeter is: {perimeter}')
    
    if lis == "rhombus":
        if request.args.get("base") and request.args.get("height"):
            a = int(request.args.get("base"))
            b = int(request.args.get("height"))
            area = a*b
            perimeter = 4*a
            return (f'Area is: {area}, Perimeter is: {perimeter}')
    
    if lis == "trapezoid":
        if request.args.get("1st side") and request.args.get("2nd side") and request.args.get("3rd side") and request.args.get("4th side") and request.args.get("Large Base Length") and request.args.get("Small Base Length") and request.args.get("Height"):
            x = int(request.args.get("1st side"))
            y = int(request.args.get("2nd side"))
            z = int(request.args.get("3rd side"))
            w = int(request.args.get("4th side"))
            a = int(request.args.get("Large Base Length"))
            q = int(request.args.get("Small Base Length"))
            b = int(request.args.get("Height"))
            area = 0.5*((a+q)*b)
            perimeter = x+y+z+w
            return (f'Area is: {area}, Perimeter is: {perimeter}')
app.run()
