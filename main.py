from datetime import datetime
from storage import save_numbers, load_numbers

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

def collect_and_analyze():
    #This function collects a series of numbers from the user and stores them in a list
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
        # Save the analysis report to report.txt with a timestamp
        # Overwrite the file each time this analysis runs
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_lines = [
            f"Analysis Report - {timestamp}",
            f"Numbers: {numbers}",
            f"Count: {count}",
            f"Sum: {total}",
            f"Average: {average}",
            f"Maximum: {maximum}",
            f"Minimum: {minimum}",
        ]
        with open("report.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines) + "\n")
        print("Analysis saved to report.txt")
    else:
        print("No numbers were entered.")
    return numbers

def menu_options():
    #show menu options
    #1) Enter numbers and analyze
    #2) Exit the program
    #3) Ask user to choose an option
    numbers = []
    while True:
        print("\n--- Menu ---")
        print("1) Enter numbers and analyze")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Exit the program")
        
        choice = input("Choose an option (1, 2, 3, or 4): ")
        
        if choice == "1":
            numbers = collect_and_analyze()
        elif choice == "2":
            try:
                save_numbers(numbers)
            except Exception as e:
                print(f"Error saving numbers: {e}")
            print("Numbers saved to data.json")
        elif choice == "3":
            try:
                loaded_numbers = load_numbers()
                print(f"Loaded numbers: {loaded_numbers}")
            except Exception as e:
                print(f"Error loading numbers: {e}")
            else:
                print("Numbers saved to data.json")
        elif choice == "4":
            print("Exiting the program.Goodbye")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")
         

def main():
    menu_options()

if __name__ == "__main__":
     main()

