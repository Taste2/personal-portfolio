import MySQLdb

# Establish a connection to the MySQL database
db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="St10285515",
    port = 3006,
    db="test_orm"
)

# Create a cursor object
cursor = db.cursor()

# Define the data to be inserted
data_to_insert = {
    'column1': 'value1',
    'column2': 'value2',
    # Add more columns and values as needed
}

cursor.execute("CREATE TABLE IF NOT EXISTS your_table (ID INT AUTO_INCREMENT, column1 VARCHAR(255), column2 VARCHAR(255))")

# Define the SQL INSERT statement
insert_query = "INSERT INTO your_table (ID, column1, column2) VALUES (%s, %s)"

try:
    # Execute the INSERT statement with data
    cursor.execute(insert_query, (data_to_insert['column1'], data_to_insert['column2']))
    
    # Commit the changes to the database
    db.commit()
    print("Data inserted successfully!")

except Exception as e:
    # If an error occurs, roll back the transaction
    db.rollback()
    print("Error:", str(e))

finally:
    # Close the cursor and the database connection
    cursor.close()
    db.close()
