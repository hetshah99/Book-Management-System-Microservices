<?php

	include "db/db.php";

    $data = json_decode(file_get_contents("php://input"), true);

    $book_id = $data["book_id"];
    $book_name = $data["book_name"];
    $author_name = $data["author_name"];
    $quantity = $data["quantity"];
	$price = $data["price"];
	
	$Query = "UPDATE stock_management SET book_name = '$book_name', author_name = '$author_name', quantity = '$quantity', price = '$price' WHERE book_id = '$book_id'";

	$result = mysqli_query($db, $Query);
			
	if($result) { echo "Book updated successfully!"; }
	else { echo "Unable to update the book!"; }
    
?>