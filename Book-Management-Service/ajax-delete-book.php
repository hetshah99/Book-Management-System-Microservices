<?php

include "db/db.php";

$data = json_decode(file_get_contents("php://input"),true);

if(isset($data['book_id']))
{
	$book_id = $data['book_id'];

	$sqlDelete ="DELETE FROM `stock_management` WHERE book_id='$book_id'";
	$result = mysqli_query($db, $sqlDelete);

	if($result) { echo "Book deleted!"; }
	else { echo "Unable to delete the book!"; }
}
else { echo "book_id not received!"; }

?>