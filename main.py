import os
from datetime import datetime, timedelta
import random

def make_commits(year: int, days: int, max_commits: int = 10):
    # Set your GitHub name and email here
    GITHUB_NAME = "ishitapatil088"
    GITHUB_EMAIL = "ishitapatil088@gmail.com"  # Use the email associated with your GitHub account

    start_date = datetime.now() - timedelta(days=days - 1)

    for day in range(days):
        commit_date = start_date + timedelta(days=day)
        commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        num_commits = random.randint(1, max_commits)

        for commit in range(num_commits):
            with open('data.txt', 'a') as file:
                file.write(f'{commit_date_str} <- Commit #{commit + 1} for this day!\n')
            os.system('git add data.txt')

            # Set environment variables for the commit
            os.environ['GIT_AUTHOR_DATE'] = commit_date_str
            os.environ['GIT_COMMITTER_DATE'] = commit_date_str
            os.environ['GIT_AUTHOR_NAME'] = GITHUB_NAME
            os.environ['GIT_AUTHOR_EMAIL'] = GITHUB_EMAIL
            os.environ['GIT_COMMITTER_NAME'] = GITHUB_NAME
            os.environ['GIT_COMMITTER_EMAIL'] = GITHUB_EMAIL

            os.system(f'git commit -m "Commit #{commit + 1} for {commit_date_str}"')

    os.system('git push')

# Example usage
make_commits(datetime.now().year, 20, max_commits=10)
