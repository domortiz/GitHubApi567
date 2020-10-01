import requests
import json


def check_repo(username):

    if len(username) == 0:
        print("No username entered")
        return False

    else:
        r = requests.get('https://api.github.com/users/' + username + '/repos')

        data = r.json()

        for d in data:

            commits_page = requests.get('https://api.github.com/repos/' + username + '/' + d['name'] + '/commits')
            commits_page = commits_page.json()
            commits = len(commits_page)
            print('Repository: ' + d['name'] + '\t\t\t commits: ' + str(commits))
    return True


if __name__ == "__main__":
    user_id = input("Enter Github ID you want to look at ")
    check_repo(user_id)
