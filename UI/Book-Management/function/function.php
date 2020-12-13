<?php
include "db/db.php";
function Redirect_to($New_Locaton){
	header("Location:".$New_Locaton);
	exit;
}
