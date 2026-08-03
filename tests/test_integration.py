import sqlite3

import app as app_module


def test_home_page_response():
    client = app_module.app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_sql_injection_payload_is_treated_as_text(tmp_path, monkeypatch):
    test_database = tmp_path / "test_tasks.db"
    monkeypatch.setattr(app_module, "DATABASE", str(test_database))

    client = app_module.app.test_client()
    payload = "'; DROP TABLE tasks; --"

    response = client.post(
        "/add",
        data={"title": payload},
        follow_redirects=True,
    )

    assert response.status_code == 200

    connection = sqlite3.connect(test_database)

    stored_task = connection.execute("SELECT title FROM tasks WHERE id = 1").fetchone()

    table_exists = connection.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table' AND name = 'tasks'
        """
    ).fetchone()

    connection.close()

    assert stored_task is not None
    assert stored_task[0] == payload
    assert table_exists is not None

    homepage_response = client.get("/")
    assert homepage_response.status_code == 200
