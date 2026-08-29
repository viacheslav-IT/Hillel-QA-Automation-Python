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
@allure.story("User Management")
@allure.title("Verify Complete User CRUD in Database")
@allure.description("This test validates CRUD operations for users in the database.")
@allure.issue("AUTH-1234", name="Jira Issue")
@allure.link("https://wiki.example.com/db-testing", name="Database verification documents")
def test_user_crud_operations(db_connection):
  db_page = UserDatabasePage(db_connection)

  @allure.step("Create table")
  def step_create_table():
    db_page.create_table()

  @allure.step("Add new user")
  def step_add_user(name, surname):
    uid = db_page.add_user(name, surname)
    assert uid is not None, "Failed to add record"
    return uid

  @allure.step("Retrieve user with ID")
  def step_get_user(user_id):
    user = db_page.get_user(user_id)
    assert user == ("Alice", "User"), "Failed to select data"
    return user

  @allure.step("Update user role")
  def step_update_user(user_id, new_role):
    db_page.update_user_role(user_id, new_role)
    updated_user = db_page.get_user(user_id)
    assert updated_user[1] == new_role, "Failed to update record role"

  @allure.step("Delete user")
  def step_delete_user(user_id):
    db_page.delete_user(user_id)
    count = db_page.count_user(user_id)
    assert count == 0, "Failed to delete record"

  # Execute test steps
  step_create_table()
  user_id = step_add_user("Alice", "User")
  step_get_user(user_id)
  step_update_user(user_id, "Admin")
  step_delete_user(user_id)

  db_page.close()