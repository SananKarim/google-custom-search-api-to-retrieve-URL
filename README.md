# google-custom-search-api-to-retrieve-URL
This code is a Python script that utilizes the Google Custom Search API to retrieve the first search result URL for a list of search queries stored in a CSV file. The script reads the CSV file, performs Google searches for each search query, and updates the CSV file with the obtained URLs.

Here's a breakdown of how the code works:

The script imports the necessary libraries, pandas for data manipulation and requests for making HTTP requests.

The get_first_search_result_url function is defined to perform a Google Custom Search using the Google Search API. It takes a search query, API key, and Custom Search Engine (CSE) ID as input, and it returns the URL of the first search result, or "No search results found." if no results are found.

The main function is the entry point of the script.

It sets the Google API key and Custom Search Engine (CSE) ID to be used for the Google searches.

The script reads data from a CSV file named "filtered-t.csv" into a pandas DataFrame (df).

It iterates over the DataFrame rows, starting from row 0, for the "STRING" and "URLs" columns.

For each row, it checks if the URL is empty or null. If the URL is empty, it calls the get_first_search_result_url function with the search query from the "STRING" column to retrieve the first search result URL.

If a valid search result URL is obtained, it updates the corresponding "URLs" cell in the DataFrame.

The script prints messages indicating whether a URL is found for each search query or if the URL already exists in the DataFrame.

After processing all the rows, the updated DataFrame is saved back to the CSV file.

Note: The code assumes that the CSV file "filtered-t.csv" contains two columns named "STRING" for search queries and "URLs" for storing search result URLs. Additionally, it uses the Google Custom Search API with the provided API key and CSE ID to retrieve the first search result URL for each search query. Make sure to replace the API key and CSE ID with valid values before running the script.
