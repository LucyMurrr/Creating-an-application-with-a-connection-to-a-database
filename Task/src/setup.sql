CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    task_name TEXT NOT NULL,
    difficulty_level INTEGER CHECK (difficulty_level BETWEEN 1 AND 5),
    created_by TEXT NOT NULL,
    comnt TEXT NOT NULL
);
