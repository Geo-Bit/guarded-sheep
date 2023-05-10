from github import Github
import os
import json

ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')
config_file_name = 'config.json'
# Authenticate
g = Github(ACCESS_TOKEN)

def searchCode(query):
    results = []
    findings = {}
    code_results = g.search_code(query=query)
    for content_file in code_results:
        results.append({"name":content_file.name,"repo":content_file.repository.url})
    return results

def searchRepos(query):
    repos = ""
    return repos

def searchUsers(query):
    results = []
    return results

def main():    
    config_file = open(config_file_name)
    config_data = json.load(config_file)

    # Get repo info based on query
    code_findings = searchCode(config_data['code_query'])
    print(code_findings)

if __name__ == "__main__":
    main()