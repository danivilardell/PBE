<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <title>PBE web-client</title>
</head>

<?php

echo '
<body id="body" style="background-color:#e6e6e6">
    <center>
        <h1>PBE Web-Client</h1>
        <input type="text" id="queryText" placeholder="Insert Query">
        <br><br>
        <button id="queryButton" class="button-9">MAKE QUERY</button>
        <br><br><br><br>
        <div id="table">

        </div>
    </center>
</body>
<script src="main.js"></script>
';

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
</html>
