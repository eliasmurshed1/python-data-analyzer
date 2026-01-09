from datetime import datetime
from unittest import result
from unittest.util import safe_repr
from storage import save_numbers, load_numbers
from analyzer import analyze_numbers
from save_report import save_report
def collect_numbers():
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
    # # if results:
    # #     total, average, maximum, minimum = results
    # #     print(f"Sum: {total}")
    # #     print(f"Count: {count}")
    # #     print(f"Average: {average}")
    # #     print(f"Maximum: {maximum}")
    # #     print(f"Minimum: {minimum}")
    #     # Save the analysis report to report.txt with a timestamp
    #     # Overwrite the file each time this analysis runs
    #     #overwrite the file each time this analysis runs
    #     #do not create a function for this part
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     report_lines = [
    #         f"Analysis Report - {timestamp}",
    #         f"Numbers: {numbers}",
    #         f"Count: {count}",
    #         f"Sum: {total}",
    #         f"Average: {average}",
    #         f"Maximum: {maximum}",
    #         f"Minimum: {minimum}",
    #     ]
    #     with open("report.txt", "w", encoding="utf-8") as f:
    #         f.write("\n".join(report_lines) + "\n")
    #     print("Analysis saved to report.txt")
    # else:
    #     print("No numbers were entered.")
    return numbers

def menu_options():
    #show menu options
    #1) Enter numbers and analyze
    #2) Exit the program
    #3) Ask user to choose an option
    numbers = []
    last_results = None
    while True:
        print("\n--- Menu ---")
        print("1) Enter numbers")
        print("2) Save numbers to JSON file")
        print("3) Load numbers from JSON file")
        print("4) Analyze current numbers")
        print("5) Save analysis report to report.txt")
        print("6) Exit the program")
        choice = input("Choose an option (1, 2, 3, 4, 5, or 6): ")
        
        if choice == "1":
            numbers = collect_numbers()
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
            if not numbers:
                print("No numbers to analyze. Please enter or load numbers first.")
                continue
            last_results = analyze_numbers(numbers)
            if last_results is None:
                print("No numbers to analyze.")
            else:
                from analyzer import print_report
                print_report(numbers, last_results)
        elif choice == "5":
            if not numbers or last_results is None:
                print("No analysis results to save. Please analyze numbers first.")
                continue
            try:
                save_report(numbers, last_results)
            except Exception as e:
                print(f"Error saving report: {e}")

        elif choice == "6":
            print("Exiting the program.Goodbye")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")
         


def main():
    menu_options()
    analyze_numbers([])

if __name__ == "__main__":
     main()

