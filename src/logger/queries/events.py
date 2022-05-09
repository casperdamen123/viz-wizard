schema_query = """
CREATE TABLE events (
    id INTEGER PRIMARY KEY IDENTITY,
    created DATETIME,
    event_name TEXT NOT NULL,
    event_info TEXT NOT NULL
);
"""

events_query = """
INSERT INTO events (created, event_name, event_info) 
VALUES (CURRENT_TIMESTAMP, ?, ?)
"""
