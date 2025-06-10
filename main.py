import os
from datetime import datetime, timedelta
import random

def make_commits(year: int, days: int, max_commits: int = 10):
    """
    Create Git commits for the specified number of days in a specific year, with varying commit intensity.
    :param year: The target year for the commits.
    :param days: The number of days to go back from the end of the year.
    :param max_commits: The maximum number of commits for the most active days.
    """
    # Calculate the starting date for commits
    start_date = datetime(year, 1, 31) - timedelta(days=days - 1)

    for day in range(days):
        # Calculate the date for the commit
        commit_date = start_date + timedelta(days=day)
        commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')

        # Decide the number of commits for the day (random intensity)
        num_commits = random.randint(1, max_commits)

        for commit in range(num_commits):
            # Write to the file to simulate a change
            with open('data.txt', 'a') as file:
                file.write(f'{commit_date_str} <- Commit #{commit + 1} for this day!\n')

            # Stage the file
            os.system('git add data.txt')

            # Set environment variables for the commit
            os.environ['GIT_AUTHOR_DATE'] = commit_date_str
            os.environ['GIT_COMMITTER_DATE'] = commit_date_str

            # Commit with the specified date
            os.system(f'git commit -m "Commit #{commit + 1} for {commit_date_str}"')

    # Push all commits to the remote repository
    os.system('git push')

# Example usage: Commits for 2022, 365 days, up to 10 commits per day
make_commits(2025, 20, max_commits=10)
