import sqlite3

class Memory:
    def __init__(self, db_name="assistant.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_text TEXT,
            ai_text TEXT
        )
        """)
        self.conn.commit()

    def save(self, user_text, ai_text):
        self.cursor.execute(
            "INSERT INTO memory (user_text, ai_text) VALUES (?, ?)",
            (user_text, ai_text)
        )
        self.conn.commit()

    def load_recent(self, limit=5):
        self.cursor.execute(
            "SELECT user_text, ai_text FROM memory ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        return self.cursor.fetchall()