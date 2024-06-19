-- creates database and table named cities 
-- id is primary key making it unique and auto increments.
-- state_id is foreign key and refrences states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL
    FOREIGN KEY (state_id) REFERENCES states(id)
    name VARCHAR(256) NOT NULL
);