#import the requests module
import requests
#Store the URL of the API call.
#The info followed after the ':' represents a variable which can be replaced by whatever info you need to search for on the site.
#The '?' after repositories indicates that you are about to pass an arguement. The 'q' stands for 'query' and the '=' lets us start specifying the query.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
#Use the 3rd version of the Github API and define headers for it.
headers = {'Accept': 'application/vnd.github.v3+json'}
#Actually use requests to make the call to the API.
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store the API response in a variable.
#The API returns the information in JSON format so use the .json() method to convert the info to a Python dictionary.
response_dict = r.json()

#Process the results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories.
repo_dicts = response_dict['items']

print(f'Repositories returned: {len(repo_dicts)}')

#Examine the first repository.
repo_dict = repo_dicts[0]
print(f'\nKeys: {len(repo_dict)}')
#for key in sorted(repo_dict.keys()):
    #print(key)

print('\nSelected information about first repository:')
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")      #Use 'owner' to access te dictionary representing the project's owner and 'login' for his login name.
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

# Print the chosen information about every single Python repository.
print(f'\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")






