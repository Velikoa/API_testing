#import the requests module
import requests

from plotly.graph_objs import Bar
from plotly import offline

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
# Process results.
response_dict = r.json()

#Process the results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories.
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualisation.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')






