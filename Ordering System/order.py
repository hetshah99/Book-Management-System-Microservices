# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:11:48 2020

@author: HETSHAH
"""

from flask import Flask,request, redirect,render_template
import psycopg2
import pika, os
import time
import json as JSON
import requests


app = Flask(__name__)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form
        print(req)
        connection = psycopg2.connect(user="postgres",
                                  password="het",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
        cursor = connection.cursor()
        cursor.execute("ROLLBACK")
        
        
        json = JSON.dumps(req);
        print(json)
        temp =requests.get('http://127.0.0.1:8000/order')
        time.sleep(2)
        temp =requests.get('http://127.0.0.1:8000/order')
        
        
        #RABBITMQ PUBLISH QUEUE1
        url = os.environ.get('CLOUDAMQP_URL', '')
        params = pika.URLParameters(url)
        connection2 = pika.BlockingConnection(params)
        channel = connection2.channel()
        channel.queue_declare(queue='queue1')
        
        channel.basic_publish(exchange='',
                              routing_key='queue1',
                              body=json
                              )
        connection2.close()
        
        #RABBITMQ SUBSCRIBE QUEUE2
        time.sleep(15)
        url = os.environ.get('CLOUDAMQP_URL', '')
        params = pika.URLParameters(url)
        connection2 = pika.BlockingConnection(params)
        channel = connection2.channel()
        channel.queue_declare(queue='queue2')
        
        method_frame, header_frame, body = channel.basic_get(queue = 'queue2')
        print(body)
        print("Status about your order : ", body)      
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        connection2.close()
        body= body.strip()
        postgres_insert_query = """ INSERT INTO bookorder (bid,qty,status ) VALUES (%s,%s,%s)"""
        record_to_insert = (req['bid'],req['quant'],str(body))
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        
        if(connection):
            cursor.close()
            connection.close()

        return render_template("sign_up1.html")
            
    return render_template("sign_up.html")

@app.route('/orderinfo')
def v_timestamp():
    connection = psycopg2.connect(user="postgres",
                                  password="het",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM bookorder")
    data = mycursor.fetchall()
    return render_template('orderinfo.html', data=data)
if __name__ == '__main__':
    app.run(debug=False, port=8080)
