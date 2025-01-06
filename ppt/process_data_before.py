# Without maintainability
def process_data(data):
    # Long, unclear logic
    for item in data:
        if item['value'] > 10:
            print(f"High value: {item['value']}")
        else:
            print(f"Low value: {item['value']}")

