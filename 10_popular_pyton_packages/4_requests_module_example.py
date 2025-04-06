""" Running of this API will require a run of https://github.com/dneprokos/node-rest-services project as test server """
import requests
import config

base_url = "http://localhost:5000/api"


# user_name = 'testadmin'
# password = 'testadminpassword'


def send_post_authorization(user_name, password):
    url = f"{base_url}/authorization"
    query_params = {f'username': user_name, 'password': password}
    headers = {
        "Accept": "application/json"
    }

    response = requests.post(url, params=query_params, headers=headers)
    status_code = response.status_code
    json = response.json()
    access_token = json["accessToken"]
    print("Status code is: ", status_code)
    print("json response is: ", json)
    print("Access token value is: ", access_token)
    return access_token


def send_get_movies(auth_key, query_params={}):
    url = f"{base_url}/movies"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {auth_key}"
    }

    response = requests.get(url, params=query_params, headers=headers)
    status_code = response.status_code
    json = response.json()
    print("Status code is: ", status_code)
    print("json response is: ", json)
    return json


access_token = send_post_authorization(config.user_name, config.password)
movies_response = send_get_movies(auth_key=access_token)

# get all movers released after 2000
data = movies_response["data"]
print(data)

# Classic languages implementation
# filtered_movies = []

# for movie in data:
#     if movie['release_date'] > 1999:
#         filtered_movies.append([movie['name']])

# List comprehansion
filtered_movies = [[movie['name']]
                   for movie in data if movie['release_date'] > 1999]
print(filtered_movies)
