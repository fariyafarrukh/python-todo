


import streamlit as st
import json
import os

TODO_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

st.title("✅ Simple Todo List")

# Load tasks
tasks = load_tasks()

# Add new task
new_task = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if new_task:
        tasks.append({"task": new_task, "done": False})
        save_tasks(tasks)
        st.success(f"Task added: {new_task}")
        st.experimental_rerun()

# Display tasks
st.subheader("Your Tasks")
for i, task in enumerate(tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"{i+1}. {task['task']}")
    if col2.button("✅ Done", key=i):
        tasks.pop(i)
        save_tasks(tasks)
        st.experimental_rerun()

