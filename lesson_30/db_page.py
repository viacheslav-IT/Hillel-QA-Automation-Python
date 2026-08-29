import allure


class UserDatabasePage:

  def __init__(self, conn):
    self.conn = conn
    self.cursor = conn.cursor()

  @allure.step("Create 'users' table")
  def create_table(self):
    self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                role VARCHAR(50)
            );
        """)
    self.conn.commit()

  @allure.step("Add a new user")
  def add_user(self, name, role):
    self.cursor.execute(
        "INSERT INTO users (name, role) VALUES (%s, %s) RETURNING id;",
        (name, role),
    )
    user_id = self.cursor.fetchone()[0]
    self.conn.commit()
    return user_id

  @allure.step("Get user data by ID")
  def get_user(self, user_id):
    self.cursor.execute(
        "SELECT name, role FROM users WHERE id = %s;", (user_id,)
    )
    return self.cursor.fetchone()

  @allure.step("Update role for user ID")
  def update_user_role(self, user_id, new_role):
    self.cursor.execute(
        "UPDATE users SET role = %s WHERE id = %s;", (new_role, user_id)
    )
    self.conn.commit()

  @allure.step("Delete user by ID")
  def delete_user(self, user_id):
    self.cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    self.conn.commit()

  @allure.step("Count users with ID")
  def count_user(self, user_id):
    self.cursor.execute("SELECT COUNT(*) FROM users WHERE id = %s;", (user_id,))
    return self.cursor.fetchone()[0]

  def close(self):
    self.cursor.close()