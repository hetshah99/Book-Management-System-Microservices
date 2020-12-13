<?php

	include "db/db.php";

    $data = json_decode(file_get_contents("php://input"), true);

    $book_name = $data["book_name"];
    $author_name = $data["author_name"];
    $quantity = $data["quantity"];
	$price = $data["price"];
	
	$Query = "INSERT INTO `stock_management`(`book_name`, `author_name`, `quantity`, `price`) VALUES ('$book_name','$author_name','	$quantity','$price')";

	$result = mysqli_query($db, $Query);
			
	if($result) { echo "Book inserted successfully!"; }
	else { echo "Unable to insert the book!"; }
    
?>