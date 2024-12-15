def fibonacci_search(phonebook, name):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    while fib_m < len(phonebook):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m_minus_2, len(phonebook) - 1)

        if phonebook[i][0] < name:
            fib_m, fib_m_minus_1, fib_m_minus_2 = fib_m_minus_1, fib_m_minus_2, fib_m_minus_1
            offset = i

        elif phonebook[i][0] > name:
            fib_m, fib_m_minus_1, fib_m_minus_2 = fib_m_minus_2, fib_m_minus_1 - fib_m_minus_2, fib_m_minus_2 - fib_m_minus_1
        else:
            return phonebook[i]

    if (fib_m_minus_1 and phonebook[offset + 1][0] == name):
        return phonebook[offset + 1]

    return None

def insert_friend(phonebook, name, number):
    for i, entry in enumerate(phonebook):
        if entry[0] == name:
            print(f"{name} is already in the phonebook.")
            return
        elif entry[0] > name:
            phonebook.insert(i, (name, number))
            print(f"{name} has been added to the phonebook.")
            return
    phonebook.append((name, number))
    print(f"{name} has been added to the phonebook.")

def main():
    phonebook = []  

    while True:
        print("Made by Parth Kulkarni , 50 , SE-A , AI&DS")
        print("Phonebook Options:")
        print("1. Search for a friend (Fibonacci search)")
        print("2. Insert a friend")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name to search: ")
            result = fibonacci_search(phonebook, name)
            if result:
                print(f"Name: {result[0]}, Number: {result[1]}")
            else:
                print(f"{name} not found in the phonebook.")

        elif choice == 2:
            name = input("Enter the name to insert: ")
            number = input("Enter the number: ")
            insert_friend(phonebook, name, number)

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()