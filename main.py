import requests
# make an api call and store

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:",r.status_code)

response_dict = r.json()
print("Total repositories:",response_dict['total_count'])
print(response_dict.keys())

repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

repo_dicts =repo_dicts[0]
print("\nKeys:", len(repo_dicts))

for key in sorted(repo_dicts.keys()):
    print(key)