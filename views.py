from flask import  Blueprint,  render_template, request
from .models import Recipies
from .restaurants import yelp_api, city_name
import random

views = Blueprint('views', __name__)

city = city_name()

@views.route('')
def default():
    
    return render_template("default.html")

# Render the cuisines webpage
@views.route('/cuisines')
def cuisines():
    # newplayer = Recipies(Cusineid  = 3, name = " Kung Pao Chicken", link ="https://www.youtube.com/watch?v=_QWXjebXiWk")
    # newplayer2 = Recipies(Cusineid = 3, name = " Dumplings", link ="https://www.youtube.com/watch?v=EKltq6jpFvk")
    # newplayer3 = Recipies(Cusineid = 3, name = " Chow Mein", link ="https://www.youtube.com/watch?v=b3dMfLZayt0")	
    # db.session.add(newplayer)
    # db.session.add(newplayer2)
    # db.session.add(newplayer3)
    # db.session.commit()
    choices = ['/gre','/chin','/amer','/indi','/mex','/all']
    return render_template("cuisines.html", choice = random.choice(choices))

@views.route('/all', methods = ['POST', 'GET'])
def All():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(0)
            else:
                return restaurants("any")
        if 'form1' in request.form:
            return recipes(0)
        if 'form2' in request.form:
            return restaurants("any")
    return render_template("AllRecipies.html")

@views.route('/amer', methods = ['POST', 'GET'])
def American():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(1)
            else:
                return restaurants("american")
        if 'form1' in request.form:
            return recipes(1)
        if 'form2' in request.form:
            return restaurants("american")
    return render_template("American.html")

# Render Chinese food webpage
@views.route('/chin', methods = ['POST', 'GET'])
def China():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(3)
            else:
                return restaurants("Chinese")
        if 'form1' in request.form:
            return recipes(3)
        if 'form2' in request.form:
            return restaurants("Chinese")
    return render_template("China.html")

# Render Greek food webpage
@views.route('/gre', methods = ['POST', 'GET'])
def Greek():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(2)
            else:
                return restaurants("Greek")
        if 'form1' in request.form:
            return recipes(2)
        if 'form2' in request.form:
            return restaurants("Greek")
    return render_template("Greek.html")

# Render Indian food webpage
@views.route('/indi', methods = ['POST', 'GET'])
def Indian():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(5)
            else:
                return restaurants("Indian")
        if 'form1' in request.form:
            return recipes(5)
        if 'form2' in request.form:
            return restaurants("Indian")
    return render_template("Indian.html")

# Render Mexican food webpage
@views.route('/mex', methods = ['POST', 'GET'])
def Mexican():
    num = random.choice([0,1])
    if request.method == 'POST':
        if 'form0' in request.form:
            if num == 0:
                return recipes(4)
            else:
                return restaurants("Mexican")
        if 'form1' in request.form:
            return recipes(4)
        if 'form2' in request.form:
            return restaurants("Mexican")

    return render_template("Mexican.html")

@views.route('')
def restaurants(name):
    n = name + " food"
    # Retrieve restaurants from the yelp api
    dict = yelp_api(n, city)
    # Store the restaurant details
    lst = dict["name"]
    lst2 = dict["url"]
    lst3 = dict["display_phone"]
    lst4 = dict["display_address"]
    lst5 = dict["rating"]
    lst6 = []
    for i in range(len(lst)):
        lst6.append([lst[i],lst2[i],lst3[i],lst4[i],lst5[i]])
    # Pass restaurant information to the restaurants webpage
    return render_template("restaurants.html",  output_data = dict, output = lst6, choice = random.choice(lst2))

@views.route('')
def recipes(idnum):
    if idnum == 0:
        data1 = Recipies.query.filter().all()
    else:   
        data1 = Recipies.query.filter(Recipies.Cusineid == idnum)
    lst=[]
    for i in data1:
        lst.append(i.link)
    return render_template("recipies.html",  output_data = data1, choice = random.choice(lst))