CREATE TABLE IF NOT EXISTS calendar (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task TEXT NOT NULL,
  status TEXT NOT NULL DEFAULT 'in progress',
  created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)