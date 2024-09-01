import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId

load_dotenv()
DB_URL=os.getenv("DB_URL")

client = pymongo.MongoClient(DB_URL)

db = client["noteapp"]
notes_col = db["notes"]
# note = {
#     "title":"This is the title of note",
#     "desc":"This is descriptiong of note"
# }
# res = notes_col.insert_one(note)
# print(res)
def show_notes():
    notes = notes_col.find()
    if notes:
        for note in notes:
            print(f"id : {note["_id"]}")
            print(f"title : {note["title"]}")
            print(f"desc : {note["desc"]}")
    else:
        print("No notes found.")

def add_note():
    title = input("Enter title of note: ")
    desc = input("Enter description of note: ")
    notes_col.insert_one({"title": title,"desc": desc})
    print("Note added successfully.")

def update_note():
    id = input("Enter the id of note: ")
    new_title = input("Enter new title of note: ")
    new_desc = input("Enter new description of note: ")
    notes_col.update_one({"_id":ObjectId(id)},{"$set": {"title": new_title, "desc": new_desc}})
    print("Note updated successfully.")

def delete_note():
    id = input("Enter the id of note: ")
    notes_col.delete_one({"_id":ObjectId(id)})
    print("Note deleted successfully.")

def main():
    while True:
        print("\nNote Taking App with Database\n")
        print("1. Show Notes")
        print("2. Add Note")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")

        choice = input("select options (1/2/3/4/5): ")
        if choice == "1":
            show_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            update_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            print("Thanks for using this app")
            break
        else:
            print("Please select valid option.")
if __name__ == "__main__":
    main()