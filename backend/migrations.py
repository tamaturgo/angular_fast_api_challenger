from app.database import con, create_database, execute_query_no_response

connection = con

create_database_query = "CREATE DATABASE IF NOT EXISTS fastapi_db"
create_database(connection, create_database_query)

create_categories_table = "CREATE TABLE IF NOT EXISTS fastapi_db.categories (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(128) not null)"
execute_query_no_response(connection, create_categories_table)

create_products_table = "CREATE TABLE IF NOT EXISTS fastapi_db.products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(60), price FLOAT(10,2), serie INT(10), category_id INT, FOREIGN KEY (category_id) REFERENCES categories(id))"
execute_query_no_response(connection, create_products_table)