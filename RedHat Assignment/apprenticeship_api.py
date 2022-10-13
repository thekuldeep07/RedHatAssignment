from flask import Flask, jsonify,make_response,request
from flask_mongoengine import MongoEngine

app=Flask(__name__)
database="pizza_house"
DB_URI="mongodb+srv://thekuldeep_07:{}@pythoncluster.bvnlu19.mongodb.net/{}?retryWrites=true&w=majority".format("asxzasxz07",database)
app.config["MONGODB_HOST"]=DB_URI

db=MongoEngine()
db.init_app(app)

'''
Sample Request Body according to the Question
{
    "order":["pizza1","pizza2"]
}
'''

class Order(db.Document):
    order=db.ListField()


    def to_json(self):
        return{
            "order":self.order
        }



#for displaying welcome message
@app.route("/welcome",methods=["GET"])
def welcome_message():
    return make_response("Welcome to Pizza House",200)



#for recieving the orders
@app.route("/order",methods=["POST"])
def take_order():
    content=request.json
    order=Order(order=content["order"])
    order.save()
    return make_response(str(order.pk),201)



@app.route('/getorders',methods=["GET"])
def getAllOrders():
    orders=[]
    for order in Order.objects:
        orders.append(order)
    if orders:
        return make_response(jsonify(orders),200)
    else:
        return make_response("",204)



@app.route('/getorders/<order_id>',methods=["GET"])
def getOrderById(order_id):
    order_obj=Order.objects().with_id(order_id)
    if order_obj:
        return make_response(jsonify(order_obj.to_json()),200)
    else:
        return make_response("",404)
        
if  __name__== "__main__":
    app.run()