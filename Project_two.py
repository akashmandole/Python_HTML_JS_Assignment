import sqlite3

#Note : For the sake of simplicity i have included all functions in one file. These can be seggregated across multiple files to test individual component separately.

# Function creates table
def createTable(databaseConnection):
    cursor = databaseConnection.cursor()

    cursor.execute("create table data(first_name text, last_name text, home text)")
    cursor.execute("insert into data values ('Rose', 'Tyler', 'Earth')");
    cursor.execute("insert into data values ('Zoe', 'Heriot', 'Space Station W3')");
    cursor.execute("insert into data values ('Jo', 'Grant', 'Earth')");
    cursor.execute("insert into data values ('Leela', null, 'Unspecified')");
    cursor.execute("insert into data values ('Romana', null, 'Gallifrey')");
    cursor.execute("insert into data values ('Clara', 'Oswald', 'Earth')");
    cursor.execute("insert into data values ('Adric', null, 'Alzarius')");
    cursor.execute("insert into data values ('Susan', 'Foreman', 'Earth')");

    #Manually commit any dml operation
    databaseConnection.commit()
    return;

# Function deletes table
def deleteTable(databaseConnection):
    cursor = databaseConnection.cursor()
    cursor.execute("drop table data")
    return;

def displayTable(databaseConnection):
    cursor = databaseConnection.cursor()
    cursor.execute('Select * from data')
    # This will fetch all rows
    all_rows = cursor.fetchall()
    for row in all_rows:
        print("First Name : {0} \tSecond Name : {1} \tHome : {2}".format(row[0], row[1], row[2]))
    return;

print("\nProject two\n")

# This will create in memory db users
databaseConnection = sqlite3.connect('users.db')

# This will create table data in users
createTable(databaseConnection)

# This will display table data from users
displayTable(databaseConnection)

# This will delete table data from users (to persist the data remove this line)
deleteTable(databaseConnection)

# Close the database connection once done
databaseConnection.close()