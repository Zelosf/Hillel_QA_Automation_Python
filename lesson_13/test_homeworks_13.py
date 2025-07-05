import os, time, subprocess
from homeworks_13 import log_event

LOG_FILE = "login_system.log"


def clear_log_file():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)


def read_log_file():
    assert os.path.exists(LOG_FILE), "Файл логування не створено"
    with open(LOG_FILE, "r") as f:
        return f.read()


def log_event_for_test(username, status):
    subprocess.run(
        ["python", "-c", f"from homeworks_13 import log_event; log_event('{username}', '{status}')"]
    )


def test_log_success():
    clear_log_file()
    log_event_for_test("Alice", "success")
    time.sleep(0.1)
    content = read_log_file()
    assert "Status: success" in content


def test_log_expired():
    clear_log_file()
    log_event_for_test("Bob", "expired")
    content = read_log_file()
    assert "Status: expired" in content


def test_log_failed():
    clear_log_file()
    log_event_for_test("Dilan", "failed")
    content = read_log_file()
    assert "Status: failed" in content


def test_log_unknown():
    clear_log_file()
    log_event_for_test("dave", "unknown")
    content = read_log_file()
    assert "Status: unknown" in content


def test_log_username():
    clear_log_file()
    log_event_for_test("Alex", "success")
    content = read_log_file()
    assert "Username: Alex" in content

