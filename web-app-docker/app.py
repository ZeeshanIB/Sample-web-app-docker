from flask import Flask, request
from psycopg2 import connect

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to the Postgres container
    conn = connect(
        host="a",
        port=5432,
        user="b",
        password="c",
        dbname="d"
    )

    # Create the table to store IP addresses
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE IF NOT EXISTS ip_addresses (id SERIAL PRIMARY KEY, address VARCHAR(15));")

    # Store the incoming IP address
    with conn.cursor() as cur:
        cur.execute("INSERT INTO ip_addresses (address) VALUES (%s);", (request.remote_addr,))

    conn.commit()
    conn.close()
    return "IP address stored!"
@app.route('/print-table')
def print_table():
    conn = connect(
        host="hostname",
        user="username",
        password="password",
        dbname="database_name"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM ip_addresses")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return "Table printed to console"

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0',port=8080)



