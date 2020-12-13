const express = require('express')
const cors = require('cors')

const app = express()

const grpc= require('grpc');
const messages= require('./support_pb');
const services= require('./support_grpc_pb');

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.send('Customer-Support is active!');
})

app.post('/send-email', (req, res) => {
    console.log('User Query: ' + req.body.data.emailText);
    main(req.body.data.emailText);
    res.send('Email Sent!');
})

app.listen(6000, () => {
    console.log(`Customer-Support service listening at port 6000`);
})

function main(emailText){
    const client=new services.customerSupportClient(
        'localhost:50051', grpc.credentials.createInsecure(),
    );

    const supportRequest= new messages.userQuery();
    supportRequest.setEmail('17bit103@nirmauni.ac.in');
    supportRequest.setQuery(emailText);

    client.userSupport(supportRequest,function(error,response){
        if(error)
        {
            console.log('this is an error',error);
            return "Error!"
        }
        else
        {
            console.log('response from python server');
            return "Sent!"
        }
    });

}