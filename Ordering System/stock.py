import psycopg2
import pika, os
import json


from flask import Flask,request, redirect,render_template
import psycopg2
import pika, os
import time
import json as json1
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="book management"
)
mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/order", methods=["GET"])
def order():
    
    print("hi")
    #RABBITMQ SUBSCRIBE QUEUE1
    url = os.environ.get('CLOUDAMQP_URL', '')
    params = pika.URLParameters(url)
    connection2 = pika.BlockingConnection(params)
    channel = connection2.channel() # start a channel
    channel.queue_declare(queue='queue1')
    
    method_frame, header_frame, body = channel.basic_get(queue = 'queue1')
    #print(body)      
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    connection2.close() 

    json = json1.loads(body)
    
    print(json)
    
    sel="SELECT quantity from `stock_management` where book_id='" + json["bid"] + "'"
    
    print(sel)
    mycursor.execute(sel)
        
    myresult = mycursor.fetchone()
    print(myresult)
    
    quant=-1
    cquant=json["quant"]
    if myresult is not None:
        if(myresult[0] is not None):
            quant= myresult[0]
    print(quant)
    mssg="nothing"
    if quant==-1:
        mssg="product does not exist"
    elif int(quant)>=int(cquant):
        mssg="accepted"
        sel="Update `stock_management` set quantity=" + str(int(quant)-int(cquant)) +" where book_id='" + json["bid"] + "'"
        mycursor.execute(sel)
        print('Hii')
        mydb.commit()
    else:
        mssg=" product quantity not sufficint"
    print(cquant)
    url = os.environ.get('CLOUDAMQP_URL', '')
    params = pika.URLParameters(url)
    connection2 = pika.BlockingConnection(params)
    channel = connection2.channel() # start a channel
    channel.queue_declare(queue='queue2')
    
    channel.basic_publish(exchange='',
                          routing_key='queue2',
                          body=mssg
                          )
    connection2.close()
    print("Order checked !")
    
    #UPDATING STOCK AVAILABILITY
if __name__ == '__main__':
    app.run(debug=False, port=8000)

