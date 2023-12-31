import mysql.connector

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="supermarket_host",
    user="supermarket_username",
    password="supermarket_password",
    database="supermarket_inventory"
)
#for this project I won't set the mysql server 

cursor = conn.cursor()

def check_product_availability(product_id, quantity):
    cursor.execute("SELECT current_quantity FROM products WHERE id = %s", (product_id,))
    current_quantity = cursor.fetchone()[0]
    if current_quantity >= quantity:
        return True
    else:
        return False

def sell_product(product_id, quantity):
    if check_product_availability(product_id, quantity):
        cursor.execute("UPDATE products SET current_quantity = current_quantity - %s WHERE id = %s", (quantity, product_id))
        conn.commit()
        print("Sale completed successfully.")
    else:
        print("Product is unavailable or insufficient quantity.")

def reorder_product(product_id, initial_quantity):
    cursor.execute("UPDATE products SET current_quantity = %s WHERE id = %s", (initial_quantity, product_id))
    conn.commit()
    print("Product reordered.")

conn.close()
