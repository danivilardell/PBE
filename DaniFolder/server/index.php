<?php

$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "PBEDB";

$PBEDB = new mysqli($servername, $username, $password, $dbname);

$userId = $_GET["userId"];

$sql = "SELECT  Name, UserId FROM students WHERE UserId = $userId";

if(isset($userId)) {
    $result = $PBEDB->query($sql);

    $index = 0;
    while($row = $result->fetch_assoc()) $index++;

    //http://localhost:9000/?userId="A2304D2"
    if($index == 0) echo json_encode(array("res" => "Id not found"));
    else echo json_encode(array("res" => "Id found"));
}

?>
