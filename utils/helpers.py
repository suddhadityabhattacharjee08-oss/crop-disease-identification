def choose_from_list(items, title):
    print(f"\n{title}")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:
        choice = input("Enter number: ").strip()
        try:
            index = int(choice) - 1
            if 0 <= index < len(items):
                return items[index]
        except ValueError:
            pass
        print("Please enter a valid number.")


def pause():
    input("\nPress Enter to continue...")
