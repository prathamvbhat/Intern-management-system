<?php
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
    
    //Database connection
    $conn = new mysqli('localhost','root','','intern');
    if($conn->connect_error){
        die('Connection Failed : '.$conn->connect_error);
    }else{
        $stmt = $conn->prepare("insert into intern(name, email, phonenumber, dob, address, gender, college, city, branch, education, skill1, skill2, skill3, work_exp) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)");
        $stmt->bind_param("ssissssssssssi",$name, $email, $phonenumber, $dob, $address, $gender, $college, $city, $branch, $education, $skill1, $skill2, $skill3, $work_exp);
        $stmt->execute();
        echo "Registration Successful...";
        $stmt->close();
        $conn->close();
    }
?>