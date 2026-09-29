def pause():
    input("\nPress Enter to return to the main menu...")


def main():
    display_welcome_message()
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_student()
            pause()
        elif choice == "2":
            view_students()
            pause()
        elif choice == "3":
            search_student()
            pause()
        elif choice == "4":
            calculate_average()
            pause()
        elif choice == "5":
            highest_score()
            pause()
        elif choice == "6":
            lowest_score()
            pause()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 7.")
            pause()


if __name__ == "__main__":
    main()