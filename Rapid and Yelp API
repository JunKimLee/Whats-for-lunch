import requests
import json
url = "https://ip-geo-location.p.rapidapi.com/ip/check"

# The headers to be sent with the API request
headers = {
    "X-RapidAPI-Key": "fb5ed9c457msh090d033a132f99dp1fcbecjsn1897941f76e3",
    "X-RapidAPI-Host": "ip-geo-location.p.rapidapi.com"
}

# Send the API request and get the response
response = requests.request("GET", url, headers=headers)
# Parse the response text as JSON data
data = json.loads(response.text)

def city_name():
    # Get the city name from the API response
    city = data["city"]
    city_name = city["name"]
    # Get the area information from the API response and extract the state name
    area = data["area"]
    state = area["name"]
    # Split the state name into a list of words
    words = state.split()
    # Extract the first letter of each word in the state name
    first_letters = [word[0] for word in words]
    # Join the first letters together to form a new string
    result = "".join(first_letters)  
    # Combine the city name and state abbreviation into a single string
    location_city = city_name + ", " + result
    # Return the final string
    return location_city

# Define a function that uses the Yelp API to search for restaurants
def yelp_api(search_term,location):
    # Set up the API endpoint URL and format the search parameters into it
    url = f"https://api.yelp.com/v3/businesses/search?location={location}&term={search_term}&sort_by=rating&limit=10"
    # Set up the required authorization header
    headers = {
        "Authorization": "Bearer k3jajIeJTAdWrU-noDIjQOCTnXyZ-YIH9wapnAn6yuxRrLAMlwNCyuzeSE-3LU9mAmF3YEOKP2XZ3x-FkBNeazPTU5AEMHBqvlqUv_g6fq28B2n7h4zjNIUhlwj9Y3Yx",
        "Host": "api.yelp.com"
    }

    # Send the GET request to the API endpoint URL with the authorization headers
    response = requests.get(url, headers=headers)

    # Load the response data as JSON format
    data = json.loads(response.text)

    # If the status code is 200 (success), create a dictionary of restaurant details
    if response.status_code == 200:
        businesses = data["businesses"]
        dict = {
            "id": [],
            "name": [],
            "url": [],
            "display_phone": [],
            "display_address": [],
            "rating": [],
            "image_url": []
        }
        # Iterate through each business and add its details to the dictionary
        for business in businesses:
            dict["id"].append(business["id"])
            dict["name"].append(business["name"])
            dict["url"].append(business["url"])
            dict["display_phone"].append(business["display_phone"])
            dict["display_address"].append(", ".join(business["location"]["display_address"]))
            dict["rating"].append(business["rating"])
            dict["image_url"].append(business['image_url'])
        # Return the dictionary of restaurant details
        return dict  
    # If the status code is not 200 (error), print the error message
    else:
        print(f"Error: {response.status_code}")
