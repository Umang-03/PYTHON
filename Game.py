import csv
from tabulate import tabulate

# Function to search for games based on a field
def search_games(field, value):
    results = []
    with open('games.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[field].lower() == value.lower():
                results.append(row)
    return results

# Function to display the search results as a table
def display_results(results):
    if len(results) == 0:
        print("No results found.")
    else:
        headers = results[0].keys()
        data = [list(row.values()) for row in results]
        table = tabulate(data, headers=headers, tablefmt='fancy_grid')
        print(table)

# Main program
while True:
    print("Search for games:")
    print("1. Search by Title")
    print("2. Search by Genre")
    print("3. Search by Publisher")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        title = input("Enter the title: ")
        results = search_games('Title', title)
        display_results(results)
    elif choice == '2':
        genre = input("Enter the genre: ")
        results = search_games('Metadata.Genres', genre)
        display_results(results)
    elif choice == '3':
        publisher = input("Enter the publisher: ")
        results = search_games('Metadata.Publishers', publisher)
        display_results(results)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
