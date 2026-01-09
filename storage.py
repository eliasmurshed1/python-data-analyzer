# Create a function save_numbers(numbers, filename="data.json")
# It should save the list of numbers to a JSON file as adictionary with key "numbers"
# Use indent = 2
# Overwrite the file if it already exists
# Do not print anything in this function
import json
def save_numbers(numbers, filename="data.json"):
    data = {"numbers": numbers}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

#create a function load_numbers(filename="data.json")
#it should load the list of numbers from a JSON file and return the list under the "numbers" key
#if the file does not exist or is invalid, return an empty list
#do not print anything in this function
def load_numbers(filename="data.json"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("numbers", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
    def save_report(numbers, results, filename="report.txt"):
        total, average, maximum, minimum = results
        report_lines = [
            f"Analysis Report",
            f"Numbers: {numbers}",
            f"Count: {len(numbers)}",
            f"Sum: {total}",
            f"Average: {average}",
            f"Maximum: {maximum}",
            f"Minimum: {minimum}",
        ]
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines) + "\n") 
        print("Analysis saved to report.txt")