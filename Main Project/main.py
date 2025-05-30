# main.py

from library import Library


def main():
    library = Library()
    print("📚 Welcome to the Community Library System!")

    while True:
        print("\nSelect your role:")
        print("1. Member")
        print("2. Librarian")
        print("3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            member_name = input("Enter your name: ")
            while True:
                print("\nMember Menu:")
                print("1. View available books")
                print("2. Borrow book")
                print("3. Return book")
                print("4. Back to main menu")
                action = input("Choice: ")

                if action == "1":
                    library.view_available_books()
                elif action == "2":
                    title = input("Enter book title to borrow: ")
                    library.borrow_book(member_name, title)
                elif action == "3":
                    title = input("Enter book title to return: ")
                    library.return_book(member_name, title)
                elif action == "4":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "2":
            while True:
                print("\nLibrarian Menu:")
                print("1. Add book (fetches details from Google Books API)")
                print("2. Remove book")
                print("3. View borrowed books")
                print("4. View most popular books")
                print("5. Back to main menu")
                action = input("Choice: ")

                if action == "1":
                    title = input("Enter book title to add: ")
                    library.add_book(title)
                elif action == "2":
                    title = input("Enter book title to remove: ")
                    library.remove_book(title)
                elif action == "3":
                    library.view_borrowed_books()
                elif action == "4":
                    library.view_most_popular_books()
                elif action == "5":
                    break
                else:
                    print("Invalid choice.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
