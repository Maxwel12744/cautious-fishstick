  CREATE DATABASE IF NOT EXISTS students_db;
  USE students_db;

  CREATE TABLE IF NOT EXISTS results (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100),
      midterm INT,
      final INT,
      total INT
  );