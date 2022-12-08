"""Imports for main"""
from assistant import (
    add_contact,
    change_contact,
    del_contact,
    find_contact,
    get_birthdays,
    add_note,
    change_note,
    delete_note,
    find_note_by_name,
    add_tags,
)
from sorter import sort
from db_queries import get_all_contacts_from_db, get_all_notes


def main():
    """Main function which calls all functions"""
    commands_list = [
        "add_contact\n",
        "show_contacts\n",
        "find_contact\n",
        "change_contact\n",
        "delete_contact\n",
        "get_birthdays\n",
        "add_note\n",
        "show_notes\n",
        "find_note\n",
        "change_note\n",
        "delete_note\n",
        "add_tags\n",
        "sort_folder\n",
    ]
    user_commands = {
        "add_contact": add_contact,
        "change_contact": change_contact,
        "del_contact": del_contact,
        "find_contact": find_contact,
        "get_birthdays": get_birthdays,
        "show_contacts": get_all_contacts_from_db,
        "add_note": add_note,
        "show_notes": get_all_notes,
        "change_note": change_note,
        "delete_note": delete_note,
        "find_note": find_note_by_name,
        "add_tags": add_tags,
        "sort_folder": sort,
    }
    user_input = input("Write your command or type 'help' to get info: ")
    while user_input != 'exit':
        if user_input == "help":
            print(
                f'Hello, i am your virtual assistant.\n'
                f'I support these commands:\n  {"  ".join(commands_list)}'
            )
            print("Write 'exit' if you want to leave")
        elif user_input in user_commands:
            print(user_commands[user_input]())
            print("Write 'exit' if you want to leave")
        else:
            print(f"I do not support this command {user_input}")
            print("Write 'exit' if you want to leave")
        user_input = input("Command: ")
        if user_input != 'exit':
            print("write 'exit' if you want to leave")
    print("Thanks for using this application")


if __name__ == "__main__":
    main()
