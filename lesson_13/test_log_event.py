import unittest
from homework_13 import log_event


class TestLogEventFunc(unittest.TestCase):
    LOG_FILE = 'login_system.log'

    def test_log_event_success(self):
        username = "viacheslav"
        status = "success"
        log_event(username=username, status=status)
        expected_result = f"Login event - Username: {username}, Status: {status}"
        with open(self.LOG_FILE, 'r') as log:
            self.assertIn(expected_result, log.read())

    def test_log_event_expired(self):
        username = "viacheslav"
        status = "expired"
        log_event(username=username, status=status)
        expected_result = f"Login event - Username: {username}, Status: {status}"
        with open(self.LOG_FILE, 'r') as log:
            self.assertIn(expected_result, log.read())

    def test_log_event_failed(self):
        username = "viacheslav"
        status = "failed"
        log_event(username=username, status=status)
        expected_result = f"Login event - Username: {username}, Status: {status}"
        with open(self.LOG_FILE, 'r') as log:
            self.assertIn(expected_result, log.read())


if __name__ == '__main__':
    unittest.main(verbosity=3)
