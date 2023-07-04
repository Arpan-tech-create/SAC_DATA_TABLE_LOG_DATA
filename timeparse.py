import sqlite3

# Connect to the database
conn = sqlite3.connect('vedas.db')
cursor = conn.cursor()

# Execute the query to fetch the desired dates
cursor.execute("SELECT TIMESTAMP FROM threat WHERE TIMESTAMP LIKE '%Nov/2022%' AND (TIMESTAMP LIKE '%09%' OR TIMESTAMP LIKE '%10%' OR TIMESTAMP LIKE '%11%') order by TIMESTAMP asc")

# Fetch the results
results = cursor.fetchall()

# Process and print the fetched results
unique_dates = set()
for row in results:
    timestamp = row[0]
    date = timestamp.split(':')[0]
    unique_dates.add(date)

# Print the unique dates
for date in unique_dates:
    print(date)

# Close the cursor and the connection
cursor.close()
conn.close()
