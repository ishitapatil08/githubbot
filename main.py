# <<<<<<< SEARCH
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

import os
from datetime import datetime, timedelta

def make_commits_by_pattern(pattern):
    """
    pattern: 2D list (weeks x days), each value is number of commits for that day.
    """
    GITHUB_NAME = "ishitapatil088"
    GITHUB_EMAIL = "ishitapatil088@gmail.com"

    today = datetime.now()
    # Find the most recent Sunday
    start_date = today - timedelta(days=today.weekday() + 1 if today.weekday() != 6 else 0)
    start_date = start_date - timedelta(weeks=len(pattern)-1)

    for week_idx, week in enumerate(pattern):
        for day_idx, num_commits in enumerate(week):
            commit_date = start_date + timedelta(weeks=week_idx, days=day_idx)
            commit_date_str = commit_date.strftime('%Y-%m-%d 12:00:00')
            for commit_num in range(num_commits):
                with open('data.txt', 'a') as file:
                    file.write(f'{commit_date_str} <- Commit #{commit_num + 1} for this day!\n')
                os.system('git add data.txt')
                os.system(
                    f'git -c user.name="{GITHUB_NAME}" '
                    f'-c user.email="{GITHUB_EMAIL}" '
                    f'commit --date="{commit_date_str}" '
                    f'-m "Commit #{commit_num + 1} for {commit_date_str}"'
                )
    os.system('git push')

# Example pattern: 4 weeks, 7 days each (Sunday to Saturday)
# 0 = no commit (lightest), 1 = 1 commit, 4 = 4 commits (darkest)
pattern = [
    [0, 1, 2, 3, 4, 2, 1],  # Week 1
    [1, 2, 4, 4, 3, 2, 1],  # Week 2
    [0, 1, 2, 3, 4, 2, 1],  # Week 3
    [1, 2, 4, 4, 3, 2, 1],  # Week 4
]

make_commits_by_pattern(pattern)

