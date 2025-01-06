# Without maintainability
def process_data(data):
    # Long, unclear logic
    for item in data:
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