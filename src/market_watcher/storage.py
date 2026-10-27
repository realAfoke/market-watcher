import sqlite3
from .models import Observation

class Storage:
    def __init__(self,path) -> None:
        self.conn=sqlite3.connect(path)
        self.conn.execute(
                """CREATE TABLE IF NOT EXISTS observations(
                id INTEGER PRIMARY KEY,
                source TEXT NOT NULL,
                item TEXT NOT NULL,
                value REAL NOT NULL,
                observed_at TEXT NOT NULL
                )"""
                )

    def save(self,obs:Observation)-> None:
                self.conn.execute(
                "INSERT INTO observations(source,item,value,observed_at) VALUES (?,?,?,?)",
                (obs.source,obs.item,obs.value,obs.observed_at.isoformat())
                )
                self.conn.commit()
    def prev_value(self,source:str,item:str)-> float | None:
        row=self.conn.execute(
                "SELECT value FROM observations WHERE source= ? AND item = ? ORDER BY observed_at DESC LIMIT 1",
                (source,item)
                ).fetchone()
        return row[0] if row else None


