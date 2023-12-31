import sqlite3
import json

class Database:
    def __init__(self, ticker: str):
        self.conn = sqlite3.connect("database.sqlite")
        self.cursor = self.conn.cursor()
        self.ticker = ticker

    def createTable(self):
        query = f"""CREATE TABLE IF NOT EXISTS {self.ticker}_news (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text TEXT)"""
        try:
            self.cursor.execute(query)
            # Commit changes
            self.conn.commit()
        except Exception as e:
            print(f"Ada kesalahan saat mencoba Membuat table: {e}")
        
            

    def insertTable(self, data: list):
        try:
            for text in data:
                # Check data apakah data sudah ada apa belum.
                self.cursor.execute(f'SELECT * FROM {self.ticker}_news WHERE text = ?', (text,))
                existing_data = self.cursor.fetchone()

                if not existing_data:
                    self.cursor.execute(f'INSERT INTO {self.ticker}_news (text) VALUES (?)', (text,))
                else:
                    print("Data already exist!")

            # Commit changes
            self.conn.commit()
        except Exception as e:
            print(f"Something wrong when we try to Insert Data: {e}")

    def get_data(self):
        try:
            query = f"SELECT * FROM {self.ticker}_news"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()

            result = []
            for row in rows:
                result.append({
                    "id": row[0],
                    "text": row[1]
                })
            
            return json.dumps(result, indent=2)
        
        except Exception as e:
            print(f"Terjadi kesalahan (SELECT) : ", e)
        
    def close(self):
        # CLOSE CONNECTION
        self.conn.commit()
        self.conn.close()
    