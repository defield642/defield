<?php
// Assume user authentication and database connection are already established

// Function to send deposit request to admin
function sendDepositRequest($amount, $customerId, $conn) {
    // Prepare SQL statement to insert deposit request into a table (e.g., DepositRequests)
    $stmt = $conn->prepare("INSERT INTO DepositRequests (CustomerID, Amount, Status) VALUES (?, ?, 'Pending')");
    $stmt->bind_param("id", $customerId, $amount);
    
    // Execute SQL statement
    $stmt->execute();
    
    // Close statement
    $stmt->close();
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get amount from form submission
    $amount = $_POST["amount"];
    
    // Assuming you already have the customer ID from the authenticated session
    $customerId = 123; // Replace 123 with the actual customer ID
    
    // Send deposit request to admin
    sendDepositRequest($amount, $customerId, $conn);
    
    // Display success message to the user
    echo "Deposit request sent to admin for approval. Thank you!";
}
?>
