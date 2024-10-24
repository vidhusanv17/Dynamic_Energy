<?php
// Database connection details
$host = 'localhost';
$dbname = 'energy';
$username = 'root';
$password = 'admin';

// Create a connection to the database
$conn = new mysqli($host, $username, $password, $dbname);

// Check if the connection was successful
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the data from the POST request
$data = json_decode(file_get_contents('php://input'), true);

// Validate input data
if (empty($data['username']) || empty($data['password'])) {
    echo json_encode(array('success' => false, 'message' => 'Username and password are required.'));
    exit();
}

// Hash the password
$hashedPassword = password_hash($data['password'], PASSWORD_BCRYPT);

// Insert the data into the database
$sql = "INSERT INTO users (username, password) VALUES (?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $data['username'], $hashedPassword);

if ($stmt->execute()) {
    echo json_encode(array('success' => true));
} else {
    echo json_encode(array('success' => false, 'message' => 'Error inserting data into database: ' . $stmt->error));
}

// Close the statement and database connection
$stmt->close();
$conn->close();
?>
