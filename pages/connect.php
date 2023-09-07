<?php
$dbHost = 'localhost';
$dbUser = 'root'; // Replace with your MySQL username
$dbPass = ''; // Replace with your MySQL password
$dbName = 'internn';
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phonenumber = $_POST['phonenumber'];
    $dob = $_POST['dob'];
    $address = $_POST['address'];
    $gender = $_POST['gender'];
    $college = $_POST['college'];
    $city = $_POST['city'];    
    $branch = $_POST['branch'];    
    $education = $_POST['education'];    
    $skill1 = $_POST['skill1'];    
    $skill2 = $_POST['skill2'];    
    $skill3 = $_POST['skill3'];    
    $work_exp = $_POST['work_exp'];
    
   // Database connection
   $conn = new mysqli($dbHost, $dbUser, $dbPass, $dbName);
   if ($conn->connect_error) {
       die('Connection Failed: ' . $conn->connect_error);
   }
        $stmt = $conn->prepare("INSERT INTO internn(name, email, phonenumber, dob, address, gender, college, city, branch, education, skill1, skill2, skill3, work_exp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
        $stmt->bind_param("ssissssssssssi", $name, $email, $phonenumber, $dob, $address, $gender, $college, $city, $branch, $education, $skill1, $skill2, $skill3, $work_exp);
    
        if ($stmt->execute()) {
            echo "Registration Successful...";
        } else {
            echo "Error: " . $stmt->error;
        }
        
        $stmt->close();
        $conn->close();
    }
?>
