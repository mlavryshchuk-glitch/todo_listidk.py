# todo_listidk.py
---

# Simple Python To-Do List Application

A lightweight, command-line interface (CLI) application that allows users to manage daily tasks. This project demonstrates basic Python concepts including **lists**, **functions**, **loops**, and **error handling**.

## 🚀 Features

* **View Tasks:** See all items currently in your list.
* **Add Tasks:** Quickly append new items.
* **Edit Tasks:** Update existing tasks if your plans change.
* **Delete Tasks:** Remove completed or unnecessary items by their index number.
* **Error Handling:** Prevents crashes if a user enters a non-numeric value or an invalid list index.

---

## 🛠️ How it Works

The application follows a simple logic flow. It uses a global list `to_do_list = []` to store data in memory while the script is running.

### Core Functions

| Function | Description |
| --- | --- |
| `add_task(task)` | Appends a string to the end of the list. |
| `view_tasks()` | Iterates through the list using `enumerate()` to show task numbers starting at 1. |
| `delete_task(num)` | Removes an item using `.pop()`. It subtracts 1 from the user's input to match Python's 0-based indexing. |
| `edit_task(num, new)` | Locates a specific index and overwrites the value with a new string. |

---

## 💻 Usage

1. **Prerequisites:** Ensure you have Python installed on your system.
2. **Run the script:**
```bash
python main.py

```


3. **Navigate the Menu:**
* Type `1` to see your tasks.
* Type `2` then type your task description (e.g., "Buy groceries") to save it.
* Type `5` to close the application.



---

## ⚠️ Error Handling

The application includes `try-except` blocks to handle common user errors:

* **ValueError:** Triggered if a user types letters when the program expects a task number.
* **Index Out of Range:** The code checks if the number entered exists within the current list length before attempting to delete or edit.

> **Note:** This version stores tasks in **RAM**. If you close the program, the list will be cleared. To save tasks permanently, you would need to implement file handling (e.g., saving to a `.txt` or `.json` file).

---


