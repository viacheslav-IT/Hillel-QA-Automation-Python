import os
import time
import psycopg2

DB_HOST = os.getenv("DB_HOST", "postgres_db")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "secret")

def wait_for_db():
    for _ in range(10):
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            print("Waiting DB connection...")
            time.sleep(2)
    raise Exception("DB connection failed")

def run_tests():
    conn = wait_for_db()
    cursor = conn.cursor()
    print("1. DB success connection")

    # Table creation
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            role VARCHAR(50)
        );
    """)
    conn.commit()

    # Adding the records to the table
    cursor.execute("INSERT INTO users (name, role) VALUES (%s, %s) RETURNING id;", ("Alice", "User"))
    user_id = cursor.fetchone()[0]
    conn.commit()
    print(f"2. Success adding the records to the table (ID: {user_id})")

    # Select data
    cursor.execute("SELECT name, role FROM users WHERE id = %s;", (user_id,))
    user = cursor.fetchone()
    assert user == ("Alice", "User"), "Select data rror"
    print(f"3. Select data is success: {user}")

    # Records updating
    cursor.execute("UPDATE users SET role = %s WHERE id = %s;", ("Admin", user_id))
    conn.commit()
    cursor.execute("SELECT role FROM users WHERE id = %s;", (user_id,))
    assert cursor.fetchone()[0] == "Admin", "Records updating error"
    print("4. Records updating is success")

    # Delete records
    cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cursor.execute("SELECT COUNT(*) FROM users WHERE id = %s;", (user_id,))
    assert cursor.fetchone()[0] == 0, "Delete records error"
    print("5. Delete records is success")

    cursor.close()
    conn.close()
    print("\n All tests passed!")

if __name__ == "__main__":
    run_tests()