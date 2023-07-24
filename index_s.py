import pandas as pd
import requests

def get_first_search_result_url(query, api_key, cse_id):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cse_id,
        "q": query,
        "num": 1
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            first_result = data["items"][0]
            return first_result["link"]
    return "No search results found."

def main():
    api_key = "AIzaSyCZcNaji73qOhXW-8I_ceS12gQh76lUYFM"  # Replace with your actual Google API key
    cse_id = "6415340cdb21b4915"  # Replace with your actual Custom Search Engine (CSE) ID

    file_path = "./filtered-t.csv"  # Replace with the correct path to your CSV file
    df = pd.read_csv(file_path)

    # Starting from row 52 in the "STRING" column
    for index, row in df.loc[0:,:].iterrows():
        search_query = row["STRING"]
        url = row["URLs"]
        
        # If the URL is empty, perform the search and update the URL
        if pd.isnull(url) or url.strip() == "":
            first_result_url = get_first_search_result_url(search_query, api_key, cse_id)
            if first_result_url == "No search results found.":
                print("Change API key")
                return
            df.at[index, "URLs"] = first_result_url
            print(f"{search_query} - {first_result_url}")
        else:
            print(f"URL already exists for: {search_query} - {url}")

    # Save the updated DataFrame back to the CSV file
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    main()
