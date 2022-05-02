<?php
$servername = "localhost";
$username = "root";
$password = "1234";
$dbname = "PBEDB";

function dayToInt($day)
{
    switch($day) {
        case "Mon":
            return 0;
        case "Tue":
            return 1;
        case "Wed":
            return 2;
        case "Thu":
            return 3;
        case "Fri":
            return 4;
        case "Sat":
            return 5;
        case "Sun":
            return 6;
    }
}

$PBEDB = new mysqli($servername, $username, $password, $dbname);

$limit = $_GET['limit'];
$day = $_GET['day'];
$hour = $_GET['hour']['gt'];
$hourgte = $_GET['hour']['gte'];

if(isset($limit)) { //Retorna un nombre total limit de classes
    $weekDay = date('w') - 1; //gets day of week as number(0=sunday,1=monday...,6=sat)

    $sql = "SELECT Day, Hour, Subject, Room FROM timetables ORDER BY
         CASE
              WHEN Day = 'Mon' THEN " . (0 - $weekDay + 7)%7 .
              " WHEN Day = 'Tue' THEN " . (1 - $weekDay + 7)%7 .
              " WHEN Day = 'Wed' THEN " . (2 - $weekDay + 7)%7 .
              " WHEN Day = 'Thu' THEN " . (3 - $weekDay + 7)%7 .
              " WHEN Day = 'Fri' THEN " . (4 - $weekDay + 7)%7 .
              " WHEN Day = 'Sat' THEN " . (5 - $weekDay + 7)%7 .
              " WHEN Day = 'Sunday' THEN " . (6 - $weekDay)%7 . "
         END ASC, Hour ASC;";
    $result = $PBEDB->query($sql);

    $timetables = array();

    // output data of each row
    $index = 0;
    while($row = $result->fetch_assoc() and $index < $limit) {
        //echo "Day: " . $row["Day"]. "<br>Hour: " . $row["Hour"]. "<br>Subject " . $row["Subject"]. "<br>Room " . $row["Room"]. "<br>";
        $timetables[] = $row;
        $index++;
    }

    echo json_encode($timetables);

} else if(isset($day)) { //Returns first class after day and hour specified
    //localhost:9000/timetable.php?day=Tue&hour[gt]=08:00:00
    $sql = "SELECT Day, Hour, Subject, Room FROM timetables ORDER BY
         CASE
              WHEN Day = 'Mon' THEN " . (0 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Tue' THEN " . (1 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Wed' THEN " . (2 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Thu' THEN " . (3 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Fri' THEN " . (4 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Sat' THEN " . (5 - dayToInt($day) + 7)%7 .
              " WHEN Day = 'Sunday' THEN " . (6 - dayToInt($day))%7 . "
         END ASC, Hour ASC;";
    $result = $PBEDB->query($sql);

    $found = false;

    while($row = $result->fetch_assoc()) {
        //echo "Day: " . $row["Day"]. "<br>Hour: " . $row["Hour"]. "<br>Subject " . $row["Subject"]. "<br>Room " . $row["Room"]. "<br>";
        if($row["Day"] == $day) {
            if(isset($hour)) {
                if($row["Hour"] > $hour) {
                    echo json_encode($row);
                    $found = true;
                    break;
                }
            }else if(isset($hourgte)) {
                if($row["Hour"] >= $hour) {
                    echo json_encode($row);
                    $found = true;
                    break;
                }
            }
        }else {
            echo json_encode($row);
            $found = true;
            break;
        }

    }

    if($found == false) {
        echo json_encode($PBEDB->query($sql)->fetch_assoc());
    }

} else {
//http://localhost:9000/?request=timetables

    $weekDay = date('w') - 1; //gets day of week as number(0=sunday,1=monday...,6=sat)

    $sql = "SELECT Day, Hour, Subject, Room FROM timetables ORDER BY
         CASE
              WHEN Day = 'Mon' THEN " . (0 - $weekDay + 7)%7 .
              " WHEN Day = 'Tue' THEN " . (1 - $weekDay + 7)%7 .
              " WHEN Day = 'Wed' THEN " . (2 - $weekDay + 7)%7 .
              " WHEN Day = 'Thu' THEN " . (3 - $weekDay + 7)%7 .
              " WHEN Day = 'Fri' THEN " . (4 - $weekDay + 7)%7 .
              " WHEN Day = 'Sat' THEN " . (5 - $weekDay + 7)%7 .
              " WHEN Day = 'Sunday' THEN " . (6 - $weekDay)%7 . "
         END ASC, Hour ASC;";
    $result = $PBEDB->query($sql);

    $timetables = array();

    // output data of each row
    while($row = $result->fetch_assoc()) {
        //echo "Day: " . $row["Day"]. "<br>Hour: " . $row["Hour"]. "<br>Subject " . $row["Subject"]. "<br>Room " . $row["Room"]. "<br>";
        $timetables[] = $row;
    }

    echo json_encode($timetables);

}

?>
