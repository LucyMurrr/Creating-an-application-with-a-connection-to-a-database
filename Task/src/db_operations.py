
import psycopg2
from config import DB_CONFIG

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)

def get_all_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT task_id, task_name, difficulty_level, created_by, comnt FROM tasks")
    tasks = cursor.fetchall()
    cursor.close()
    conn.close()
    return tasks

def add_task(name, difficulty, created_by="", comnt=""):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (task_name, difficulty_level, created_by, comnt) VALUES (%s, %s, %s, %s)",
        (name, difficulty, created_by, comnt)
    )
    conn.commit()
    cursor.close()
    conn.close()
