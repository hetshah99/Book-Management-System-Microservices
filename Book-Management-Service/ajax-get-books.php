<?php 

	include "db/db.php";
	
	$query ="SELECT * FROM `stock_management` ORDER By book_id desc";
	$result = mysqli_query($db, $query);

	$data = array();

	while($row = mysqli_fetch_assoc($result)) {
		$data[] = $row;
	}

	mysqli_free_result($result);
	echo json_encode($data);

?>