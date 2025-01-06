# With maintainability
def process_data(data):
    for item in data:
        categorize_and_print(item)

def categorize_and_print(item):
    if item['value'] > 10:
        print(f"High value: {item['value']}")
    else:
        print(f"Low value: {item['value']}")
        
# Sample data to test the function
sample_data = [
    {'value': 5},
    {'value': 15},
    {'value': 8},
    {'value': 20}
]

# Call the function with the sample data
process_data(sample_data)

# Explanation:
# Breaking down functionality into smaller functions improves readability and reusability.
