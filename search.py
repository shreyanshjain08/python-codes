from googlesearch import search

def main():
    # Ask the user for the search query
    query = input("Enter the search query: ")
    num_results = 5  # Number of results you want

    # Perform the search
    search_results = search(query, num=num_results, stop=num_results, pause=2.0)

    # Print the results
    print(f"Top {num_results} search results for '{query}':")
    for idx, result in enumerate(search_results, start=1):
        print(f"{idx}: {result}")

if __name__ == '__main__':
    main()
