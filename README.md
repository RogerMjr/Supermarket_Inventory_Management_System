
# Supermarket Inventory Management System

## Overview

This project is an inventory management system for a supermarket, developed in Python and using a MySQL database. The system allows tracking the quantity of products in the inventory, automatically decreasing the quantity upon sales, and initiating reorders when the product quantity falls below 80% of the initial amount. It also provides feedback when a product is out of stock.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Requirements
Python 3. x
- MySQL Database
MySQL-connector-python` library (install using `pip install mysql-connector-python`

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/your-username/supermarket-inventory.git
   cd supermarket-inventory
   ```

2. Create a MySQL database and update the database connection details in the Python script.

3. Create the necessary database table using the SQL script provided in the "Database" section below.

## Usage

- To sell a product, call the `sell_product(product_id, quantity)` function with the product ID and the quantity to sell.

- To check if a product is available in sufficient quantity, use the `check_product_availability(product_id, quantity)` function.

- When the quantity falls below 80% of the initial amount, call the `reorder_product(product_id, initial_quantity)` function to reorder the product.

- Integrate this Python script with your sales system by calling the appropriate functions when a sale is made.

## Database

1. Create a MySQL database named `supermarket_inventory`.

2. Use the following SQL script to create the `products` table:

   ```sql
   CREATE TABLE products (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       initial_quantity INT NOT NULL,
       current_quantity INT NOT NULL
   );
   ```



---
