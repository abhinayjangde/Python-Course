import os

NOTES_FILTE=r"D:\codebhaiya\courses\python-course\22-Projects\notes.txt"
# print(os.path.dirname(NOTES_FILTE))
# s = "   abhinay   "
# print(s.strip())
def load_notes():
    if os.path.exists(NOTES_FILTE):
        with open(NOTES_FILTE, "r") as f:
            notes = f.readlines()
        return [note.strip() for note in notes]
    else:
        return []

def save_notes(notes):
    with open(NOTES_FILTE,"w") as f:
        for note in notes:
            f.write(note + "\n")


def add_note():
    note = input("Enter your note: ")
    notes = load_notes()
    notes.append(note)
    save_notes(notes)
    print("Note added successfully.")

def view_notes():
    notes = load_notes()
    if notes:
        print("Your notes")
        for i, note in enumerate(notes,1):
            print(f"{i}. {note}")
    else:
        print("No notes found.")


def delete_note():
    notes = load_notes()
    if notes:
        try:
            note_index = int(input("Enter note number to delete: ")) - 1
            if 0<= note_index < len(notes):
                removed_note = notes.pop(note_index)
                save_notes(notes)
                print(f"Note {removed_note} is deleted.")
            else:
                print("Please, enter valid number.")
        except ValueError:
            print("Enter valid index from (1,2,3,4)")

def main():
    while True:
        print("\nNote Taking App")
        print("1. Add Note\n2. View Notes\n3. Delete Note\n4. Exit")

        choice = input("Enter your option (1/2/3/4): ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice=="4":
            print("Have a gooday, bye!")
            break
        else:
            print("Enter valid option")

if __name__ == "__main__":
    main()
    # pass