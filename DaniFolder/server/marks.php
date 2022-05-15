<?php

$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "PBEDB";

$PBEDB = new mysqli($servername, $username, $password, $dbname);

$userId = $_GET["userId"];
$marklt = $_GET["mark"]["lt"];
$marklet = $_GET["mark"]["let"];
$subject = $_GET["subject"];

if(isset($subject)) $sql = "SELECT  subject, name, mark FROM marks WHERE UserId = $userId AND subject = $subject ORDER BY
            subject ASC;";
else $sql = "SELECT  subject, name, mark FROM marks WHERE UserId = $userId ORDER BY
            subject ASC;";

$result = $PBEDB->query($sql);

if(isset($marklt) or isset($marklet)) {
    //http://localhost:9000/marks.php?userId="A2304D2"&mark[let]=5&subject="DSBM"
    $tasks = array();

    // output data of each row
    while($row = $result->fetch_assoc()) {
        if(isset($marklt) and $row["mark"] < $marklt) $tasks[] = $row;
        else if(isset($marklet) and $row["mark"] <= $marklet) $tasks[] = $row;
    }
    echo json_encode($tasks);
} else {
    //http://localhost:9000/marks.php?userId="A2304D2"
    $tasks = array();

    // output data of each row
    while($row = $result->fetch_assoc()) {
        $tasks[] = $row;
    }
    echo json_encode($tasks);
}

?>
