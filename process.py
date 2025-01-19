import json

# Function to extract the relevant fields from each book in the JSON file
def extract_book_info(input_file, output_file):
    # Open the existing JSON file and load data
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Extracting the relevant information (title, author, and review) from each book
    books_info = []
    for book in data['books']:
        book_info = {
            'title': book.get('title', ''),
            'author': book.get('author', '').strip(),  # Remove extra spaces from author
            'review': book.get('review', '')
        }
        books_info.append(book_info)
    
    # Save the processed data into a new JSON file
    with open(output_file, 'w') as file:
        json.dump(books_info, file, indent=4)

    print(f"Processed data has been saved to {output_file}")

# Example usage
input_file = 'dataset1.json'  # Replace with the path to your input JSON file
output_file = 'processed_1.json'  # Replace with the desired output file name
extract_book_info(input_file, output_file)
