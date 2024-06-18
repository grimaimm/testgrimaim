import requests
from flask import jsonify
from app import app
from datetime import datetime, timedelta

GITHUB_TOKEN = ''
GITHUB_USERNAME = 'grimaimm'
username = 'grimaimm'

@app.route('/api/contributions')
def get_contributions_api():
    contributions_data = get_contributions_from_github()
    contribution_graph=get_github_contributions()
    return jsonify(contributions_data, contribution_graph)

def get_contributions_from_github():
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/events'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}

    try:
        response = requests.get(url, headers=headers)
        events = response.json()

        while 'next' in response.links:
            url = response.links['next']['url']
            response = requests.get(url, headers=headers)
            events.extend(response.json())

        total_contributions = len(events)
        best_day = find_best_day(events)
        average_per_day = total_contributions / len(events) if len(events) > 0 else 0

        repo_url = "https://api.github.com/user/repos"
        repo_response = requests.get(repo_url, headers=headers)
        repositories = repo_response.json()

        total_repositories = len(repositories)

        average_per_day_formatted = "{:.0f}".format(average_per_day)

        return {
            'total_contributions': total_contributions,
            'best_day': best_day,
            'average_per_day': average_per_day_formatted,
            'total_repositories': total_repositories
        }
    
    except requests.RequestException as e:
        print(f'Error fetching contributions from GitHub: {e}')
        return {}

def get_github_contributions(username, token):
    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'Bearer {token}'}
    
    query = """
    query {
        user(login: "%s") {
            contributionsCollection(from: "%s") {
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            contributionCount
                            date
                        }
                    }
                }
            }
        }
    }
    """ % (username, (datetime.utcnow() - timedelta(days=365)).isoformat())

    response = requests.post(url, json={'query': query}, headers=headers)
    data = response.json()

    contributions_last_year = data['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
    weekly_contributions = {}

    for week in data['data']['user']['contributionsCollection']['contributionCalendar']['weeks']:
        for day in week['contributionDays']:
            date = datetime.strptime(day['date'], "%Y-%m-%d").strftime("%B %Y")
            weekly_contributions[date] = weekly_contributions.get(date, 0) + day['contributionCount']

    return contributions_last_year, weekly_contributions


def find_best_day(events):
    contributions_per_day = {}

    for event in events:
        day = event['created_at'][:10]
        if day not in contributions_per_day:
            contributions_per_day[day] = 1
        else:
            contributions_per_day[day] += 1

    if not contributions_per_day:
        return None

    best_day = max(contributions_per_day, key=contributions_per_day.get)
    return contributions_per_day[best_day]


def generate_github_data():
    last_year_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%dT%H:%M:%SZ')
    url = f'https://api.github.com/users/{GITHUB_USERNAME}/events?since={last_year_date}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        contributions = parse_github_data(response.json())
        return contributions
    else:
        return []


def parse_github_data(events):
    contributions = [0] * 365

    for event in events:
        if event['type'] == 'PushEvent':
            date = datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ')
            day_of_year = (date - datetime(date.year, 1, 1)).days
            contributions[day_of_year] += len(event['payload']['commits'])

    return contributions

    # try:
    #     response = requests.get(url, headers=headers)
    #     events = response.json()

    #     # Cek apakah ada tautan paginasi
    #     while 'next' in response.links:
    #         url = response.links['next']['url']
    #         response = requests.get(url, headers=headers)
    #         events.extend(response.json())

    #     total_contributions = len(events)
    #     best_day = find_best_day(events)
    #     average_per_day = total_contributions / len(events) if len(events) > 0 else 0

    #     # Mendapatkan informasi repository
    #     repo_url = "https://api.github.com/user/repos"
    #     repo_response = requests.get(repo_url, headers=headers)
    #     repositories = repo_response.json()

    #     total_repositories = len(repositories)

    #     # Menggunakan format string untuk menampilkan nilai rata-rata per hari tanpa desimal jika nol
    #     average_per_day_formatted = "{:.0f}".format(average_per_day)

    #     return {
    #         'total_contributions': total_contributions,
    #         'best_day': best_day,
    #         'average_per_day': average_per_day_formatted,
    #         'total_repositories': total_repositories
    #     }
    
    # except requests.RequestException as e:
    #     print(f'Error fetching contributions from GitHub: {e}')
    #     return {}


    # try:
    #     # Mendapatkan informasi kontribusi
    #     response = requests.get(url, headers=headers)
    #     events = response.json()

    #     # Mendapatkan informasi repository
    #     repo_url = "https://api.github.com/user/repos"
    #     repo_response = requests.get(repo_url, headers=headers)
    #     repositories = repo_response.json()

    #     total_contributions = len(events)
    #     best_day = find_best_day(events)
    #     average_per_day = total_contributions / len(events) if len(events) > 0 else 0

    #     total_repositories = len(repositories)

    #     # Menggunakan format string untuk menampilkan nilai rata-rata per hari tanpa desimal jika nol
    #     average_per_day_formatted = "{:.0f}".format(average_per_day)

    #     return {
    #         'total_contributions': total_contributions,
    #         'best_day': best_day,
    #         'average_per_day': average_per_day_formatted,
    #         'total_repositories': total_repositories
    #     }
    # except requests.RequestException as e:
    #     print(f'Error fetching contributions from GitHub: {e}')
    #     return {}