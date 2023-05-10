from github import Github
import os
import json

ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')
config_file_name = 'config.json'
# Authenticate
g = Github(ACCESS_TOKEN)

def searchCode(query):
    results = []
    code_results = g.search_code(query=query)
    for content_file in code_results:
        results.append({"name":content_file.name,"repo":content_file.repository.url})
    return results

def searchRepos(query):
    repos = ""
    return repos

def searchUsers(query):
    results = []
    findings = {}
    user_results = g.search_users(query=query)
    for user in user_results:
        if user.get_repos().totalCount > 0:
            results.append({"user":user})
    return results

def main():    
    config_file = open(config_file_name)
    config_data = json.load(config_file)

    # Get repo info based on query
    code_findings = searchCode(config_data['code_query'])
    user_findings = searchUsers(config_data['user_query'])

if __name__ == "__main__":
    main()