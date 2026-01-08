def main():
    #Ask the user how many numbers they would like to enter
    #loop to get that many numbers from the user
    #validate that the user enters only numbers
    #store the numbers in a list
    #print the list of numbers

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

if __name__ == "__main__":
     main()

