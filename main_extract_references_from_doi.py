import requests

def get_references_from_doi(doi):
    """
    Fetch references of a scientific article using its DOI via the CrossRef API.

    :param doi: str, DOI of the article.
    :return: list of references or error message.
    """
    base_url = "https://api.crossref.org/works/"

    try:
        # Make a GET request to the CrossRef API
        response = requests.get(f"{base_url}{doi}")
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract references if they exist
            references = data.get("message", {}).get("reference", [])

            if references:
                for ref in references:
                    print(ref)
                    raise Exception

                # Format references into a list of strings
                formatted_references = [
                    f"{ref.get('author', 'Unknown Author')} ({ref.get('year', 'Unknown Year')}): {ref.get('article-title', 'No Title')}"
                    for ref in references
                ]
                return formatted_references
            else:
                return ["No references found in the metadata."]
        else:
            return [f"Error: Unable to fetch data (Status Code: {response.status_code})."]
    except Exception as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    # Example DOI
    doi = "10.1016/j.cose.2015.11.007"  # Replace with your DOI

    # Fetch references
    references = get_references_from_doi(doi)

    # Display the references
    print("\nReferences:")
    for ref in references:
        print(ref)
