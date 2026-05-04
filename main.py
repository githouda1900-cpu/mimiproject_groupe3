import json, os
from datetime import datetime

FILE = "todos.json"


def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_next_id(data):
    return max([i["id"] for i in data], default=0) + 1


def add(data):
    t = input("Task: ")
    p = input("Priority (high/medium/low): ") or "medium"

    data.append({
        "id": get_next_id(data),
        "title": t,
        "priority": p,
        "done": False,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M")
    })

    save(data)
    print("✔ Task added")


def show(data):
    print("\n--- TODO LIST ---")
    if not data:
        print("No tasks yet.")
        return

    for i in data:
        status = "✔" if i["done"] else "✗"
        print(f"{i['id']} [{status}] {i['title']} ({i['priority']})")


def mark_done(data):
    show(data)

    try:
        x = int(input("ID: "))
        for i in data:
            if i["id"] == x:
                i["done"] = True
                save(data)
                print("✔ Marked as done")
                return

        print("❌ ID not found")

    except ValueError:
        print("❌ Invalid input")


def delete(data):
    show(data)

    try:
        x = int(input("ID: "))
        new_data = [i for i in data if i["id"] != x]

        if len(new_data) == len(data):
            print("❌ ID not found")
            return

        save(new_data)
        data[:] = new_data
        print("✔ Deleted")

    except ValueError:
        print("❌ Invalid input")


def menu():
    data = load()

    while True:
        print("\n1-Add  2-Show  3-Done  4-Delete  5-Exit")
        c = input("> ")

        if c == "1":
            add(data)
        elif c == "2":
            show(data)
        elif c == "3":
            mark_done(data)
        elif c == "4":
            delete(data)
        elif c == "5":
            break
        else:
            print("Invalid choice")


menu()
