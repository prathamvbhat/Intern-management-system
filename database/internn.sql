CREATE DATABASE internn;
use DATABASE internn;
CREATE TABLE internn (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phonenumber INT NOT NULL,
    dob DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    gender CHAR(1) NOT NULL,
    college VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    branch VARCHAR(255) NOT NULL,
    education VARCHAR(255) NOT NULL,
    skill1 VARCHAR(255) NOT NULL,
    skill2 VARCHAR(255) NOT NULL,
    skill3 VARCHAR(255) NOT NULL,
    work_exp INT NOT NULL
);
