#analyzer.py - analysis logic for the CLI Data Analyzer
def analyze_numbers(numbers):
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

def print_report(numbers, results):
    if results:
        total, average, maximum, minimum = results
        print(f"Numbers: {numbers}")
        print(f"Count: {len(numbers)}")
        print(f"Sum: {total}")
        print(f"Average: {average}")
        print(f"Maximum: {maximum}")
        print(f"Minimum: {minimum}")
    else:
        print("No numbers were entered.")