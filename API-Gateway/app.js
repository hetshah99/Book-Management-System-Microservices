const express = require('express')
const cors = require('cors')
const axios = require('axios')

const app = express()
const port = 3000

app.use(cors())
app.use(express.json())

app.get('/', (req, res) => {
    res.send('API gateway is active!');
})

app.post('/login', (req, res) => {

    axios.post('http://127.0.0.1:4000/login', { 'data': req.body.data })
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });

})

app.post('/register', (req, res) => {

    axios.post('http://127.0.0.1:4000/register', { 'data': req.body.data })
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });

})

app.get('/books', (req, res) => {

    axios.get('http://localhost/Book-Management-Service/ajax-get-books.php')
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify({ 'error': 'Error communicating with book-management API!' }));
        });

})

app.post('/books/delete', (req, res) => {

    axios.post('http://localhost/Book-Management-Service/ajax-delete-book.php', {'book_id': req.body.book_id})
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });
});

app.post('/books/add', (req, res) => {

    axios.post('http://localhost/Book-Management-Service/ajax-insert-book.php', req.body)
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });
});

app.put('/books/update', (req, res) => {

    axios.put('http://localhost/Book-Management-Service/ajax-update-book.php', req.body)
        .then(function (response) {
            res.send(JSON.stringify(response.data));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });
});

app.post('/send-email', (req, res) => {

    axios.post('http://127.0.0.1:6000/send-email', {'data': req.body})
        .then(function (response) {
            res.send(JSON.stringify({'message': 'Email Sent!'}));
        })
        .catch(function (error) {
            console.log(error);
            res.send(JSON.stringify('Error communicating with user-management service!'));
        });

})

app.listen(port, () => {
    console.log(`API-Gateway listening at port ${port}`);
})