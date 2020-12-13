import grpc
from concurrent import futures
import time

import support_pb2
import support_pb2_grpc

import smtplib
import os

class customerSupportServicer(support_pb2_grpc.customerSupportServicer):
    def userSupport(self,request,context):
        response=support_pb2.systemResponse()
        response.response="200 Okay"
        # EMAIL_ID=os.environ.get('EMAIL_ID')
        EMAIL_ID = '18bit164@nirmauni.ac.in'
        # EMAIL_PASS=os.environ.get('EMAIL_PASS')
        EMAIL_PASS = 'Priyank.py_1999'
        with smtplib.SMTP('smtp.gmail.com',587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ID,EMAIL_PASS)
            subject='Hello there!'
            body='Thank you for your interest. We will get back to you soon.'
            message=f'Subject: {subject}\n\n{body}'
            msg=subject+'\n\n'+body
            smtp.sendmail(EMAIL_ID,request.email,message)
            smtp.quit()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

support_pb2_grpc.add_customerSupportServicer_to_server(customerSupportServicer(),server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

    #protoc-gen-grpc --js_out=import_style=commonjs.binary:./client/ --grpc_out=./client --proto_path./proto/ ./proto/support.proto