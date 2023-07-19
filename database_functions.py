import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('rap_battle.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rappers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        score INTEGER DEFAULT 0
    )
''')

def update_rapper_score(rapper):
    # Check if the rapper already exists in the database
    cursor.execute('SELECT * FROM rappers WHERE name = ?', (rapper,))
    result = cursor.fetchone()

    if result:
        # Increment the score if the rapper already exists
        new_score = result[2] + 1
        cursor.execute('UPDATE rappers SET score = ? WHERE name = ?', (new_score, rapper))
    else:
        # Create a new entry for the rapper if they don't exist
        cursor.execute('INSERT INTO rappers (name, score) VALUES (?, 1)', (rapper,))

    # Commit the changes to the database
    conn.commit()


