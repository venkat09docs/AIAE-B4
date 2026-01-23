# JSON HANDLING FOR STRUCTURED DATA

import json # import the json module

with open('./config.json', 'r') as jsonfile:
    data = json.load(jsonfile)  # Load JSON data from the file
    print(data)  # Print the entire JSON data
    print(type(data))  # Print the type of the data (should be dict)

    # Accessing specific fields in the JSON data
    print(data["default_parameters"]["top_p"])  # Access nested field
print(data["user_prompts"]["farewell_message"])

pretty_json = json.dumps(data, indent=8)  # Convert Python object back to JSON string with indentation
# print(pretty_json)

# API -


# PARSING JSON DATA FROM API RESPONSES

import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')  # Make a GET request to the API
print(response)  # Print the status code of the response

# Status Codes
# 2xx Successful responses
# 3xx Redirection messages
# 4xx Client error responses
# 5xx Server error responses

# data = response.json()  # Parse the JSON data from the response
data = json.loads(response.text)
print(data)

# print(data[10]["id"])

# for post in data:
#     print(f"Title: {post['title']}")

# print(data[49]["title"])

# Example of a JSON response containing API usage details and choices
response = {
    "usage": {
        "total_tokens": 1000,
        "details": {"prompt_tokens": 300, "completion_tokens": 700}
    },
    "choices": [
        {"text": "The capital of France is Paris.", "index": 0},
        {"text": "France's capital is Paris.", "index": 1}
    ]
}

# print(type(response))
# print(response.keys())
# print(response.values())
# print(response.items())

print(response["usage"]["total_tokens"])  # Access total tokens used

for choice in response["choices"]:
    print(choice["text"])  # Access text of each choice
# print(response["choices"][0]["text"])  # Access text of the first choice


