-- Create a users table with these attributes: id, email, name amd country
CREATE TABLE IF NOT EXISTS users (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    email     VARCHAR(255) NOT NULL UNIQUE,
    name      VARCHAR(255),
    country   ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
