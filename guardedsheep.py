from github import Github
import os
import json

ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')
config_file_name = 'config.json'

def searchCode():
    content_file = ""
    return content_file

def searchRepos():
    repos = ""
    return repos

def main():
    # Authenticate
    g = Github(ACCESS_TOKEN)

    # Test authentication success
    user = g.get_user()
    print(user.login)
    
    config_file = open(config_file_name)
    config_data = json.load(config_file)
    code_query = config_data['code_query']

    # Get repo info based on query
    repositories = g.search_code(query=code_query)
    for repo in repositories:
        owner = repo.repository.owner
        print(owner.name, owner.location, owner.bio, owner.role, )

if __name__ == "__main__":
    main()