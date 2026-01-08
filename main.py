def analyze_numbers(numbers):
    #This function takes a list of numbers and returns their sum, average, maximum, and minimum
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum


def main():
    #this function collects a series of numbers from the user and stores them in a list
    while True:
        try:
            count = int(input("How many numbers would you like to enter?: "))
            if count <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")
    print(count)
    numbers = []
    for i in range(count):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Please enter a valid integer.")
    print(numbers)


    results = analyze_numbers(numbers)
    if results:
        total, average, maximum, minimum = results
        print(f"Sum: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
     main()

