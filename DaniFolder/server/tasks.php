<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "PBEDB";


$userId = $_GET['userId'];

$PBEDB = new mysqli($servername, $username, $password, $dbname);

$sql = "SELECT  Date, Subject, Name FROM tasks WHERE UserId = $userId ORDER BY date ASC";

$result = $PBEDB->query($sql);

$dategte = $_GET['date']['gte'];
$dategt = $_GET['date']['gt'];
$limit = $_GET['limit'];

if(!isset($limit)) $limit = 1e8;

if(isset($dategte) or isset($dategt)) {
    //http://localhost:9000/tasks.php/?userId="A2304D2"&date[gt]=2022-02-24&limit=2

    if(isset($dategte) and $dategte == "now") $dategte = date("Y-m-d");
    else if(isset($dategt) and $dategt == "now") $dategt = date("Y-m-d");

    echo $dategt;
    $tasks = array();

    // output data of each row
    $index = 0;
    while($row = $result->fetch_assoc() and $index < $limit) {
        //echo "Day: " . $row["Day"]. "<br>Hour: " . $row["Hour"]. "<br>Subject " . $row["Subject"]. "<br>Room " . $row["Room"]. "<br>";
        if(isset($dategte)  and $row["Date"] >= $dategte) {
            $tasks[] = $row;
            $index++;
        }
        else if(isset($dategt) and $row["Date"] > $dategt){
            $tasks[] = $row;
            $index++;
        }
    }
    echo json_encode($tasks);
} else {
    $tasks = array();

    // output data of each row
    while($row = $result->fetch_assoc()) {
        //echo "Day: " . $row["Day"]. "<br>Hour: " . $row["Hour"]. "<br>Subject " . $row["Subject"]. "<br>Room " . $row["Room"]. "<br>";
        $tasks[] = $row;
    }
    echo json_encode($tasks);
}
?>
