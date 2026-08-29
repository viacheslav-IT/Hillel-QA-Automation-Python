import os
import allure
import psycopg2
import pytest
from db_page import UserDatabasePage

DB_HOST = os.getenv("DB_HOST", "postgres_db")
DB_NAME = os.getenv("POSTGRES_DB", "testdb")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "secret")


@pytest.fixture(scope="function")
def db_connection():
  conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
  yield conn
  conn.close()

@allure.feature("Database Operations")
@allure.story("CRUD Operations for Users")
@allure.title("Test User CRUD operations in Database")
def test_user_crud_operations(db_connection):
  db_page = UserDatabasePage(db_connection)

  # 1. Create table
  db_page.create_table()

  # 2. Add a record
  user_id = db_page.add_user("Alice", "User")
  assert user_id is not None, "Failed to add record"

  # 3. Select data
  user = db_page.get_user(user_id)
  assert user == ("Alice", "User"), "Failed to select data correctly"

  # 4. Update records
  db_page.update_user_role(user_id, "Admin")
  updated_user = db_page.get_user(user_id)
  assert updated_user[1] == "Admin", "Failed to update record role"

  # 5. Delete records
  db_page.delete_user(user_id)
  count = db_page.count_user(user_id)
  assert count == 0, "Failed to delete record"

  db_page.close()