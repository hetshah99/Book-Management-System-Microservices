const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const cors = require("cors");

const app = express();
const port = 4000;

app.use(cors());
app.use(express.json());

let db = null;

MongoClient.connect('mongodb://localhost:27017', (err, connection) => {

    if (err) {
        console.log(err);
        console.log('Cannot Connect to MongoDB!');
    }
    else {
        db = connection.db('Inventory-Management');
        console.log('Connected to MongoDB...');
    }

});

app.get('/', (req, res) => {
    res.send('User-management service active!');
});

app.post('/register', (req, res) => {

    db.collection('Users').find({username: req.body.data.username}).toArray(function(err, docs) {

        if(err) {
            console.log(err);
            res.send(JSON.stringify({'error': 'MONGODB-ERROR'}));
        }
        else
        {
            if(docs.length === 0) {
                db.collection('Users').insertOne(req.body.data)
                    .then(r => { res.send(JSON.stringify({'message': 'REGISTRATION-SUCCESSFUL'})) })
                    .catch(reason => { res.send(JSON.stringify({'error': 'REGISTRATION-FAILED'})) });
            }
            else {
                res.send(JSON.stringify({'message': 'USER-ALREADY-REGISTERED'}));
            }
        }
    });

});

app.post('/login', (req, res) => {

    db.collection('Users').findOne({ $and: [{username: req.body.data.username}, {password: req.body.data.password}] }, function(err, doc) {

        if(err) {
            console.log(err);
            res.send(JSON.stringify({'error': 'MONGODB-ERROR'}));
        }
        else {
            if(doc) { res.send(JSON.stringify(doc)); }
            else { res.send(JSON.stringify({'message': 'WRONG-CREDENTIALS'})); }
        }
    });

});

app.listen(port, () => {
    console.log(`User-Management service listening at port ${port}`);
})