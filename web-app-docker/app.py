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
    print ("IP address stored!")
    return "IP address stored!"

if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0',port=8080)



