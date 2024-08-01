import pandas as pd
import random as rd

def already_started():
    total_episodes = len(unwatched)
    random_index = rd.randint(0, total_episodes - 1)
    choice = unwatched.iloc[random_index]

    episode_title = choice['Title']
    episode_season = choice['Season']
    
    # Create a DataFrame for the new row
    new_row = pd.DataFrame([{'Season': episode_season, 'Episode': random_index, 'Title': episode_title}])
    # Append the new row to the existing DataFrame
    combined = pd.concat([watched, new_row], ignore_index=True)
    # Save the combined DataFrame back to the CSV file
    combined.to_csv('episode_list/watched_episodes.csv', index=False)
    
    # Optionally, remove the selected episode from unwatched list
    unwatched.drop(random_index, inplace=True)
    unwatched.to_csv('episode_list/unwatched_episodes.csv', index=False)

    return f"Watch {episode_season}, Episode {random_index}: {episode_title}"


def not_started():
    total_episodes = len(unwatched)
    
    random_index = rd.randint(0, total_episodes - 1)
    choice = unwatched.iloc[random_index]

    episode_title = choice['Title']
    episode_season = choice['Season']

    # Create a DataFrame for the new row
    new_row = pd.DataFrame([{'Season': episode_season, 'Episode': random_index, 'Title': episode_title}])
    # Append the new row to the existing DataFrame
    combined = pd.concat([watched, new_row], ignore_index=True)
    # Save the combined DataFrame back to the CSV file
    combined.to_csv('episode_list/watched_episodes.csv', index=False)
    
    # Optionally, remove the selected episode from unwatched list
    unwatched.drop(random_index, inplace=True)
    unwatched.to_csv('episode_list/unwatched_episodes.csv', index=False)

    return f"Watch {episode_season}, Episode {random_index}: {episode_title}"


# Main logic to check and call functions
unwatched = pd.read_csv('episode_list/unwatched_episodes.csv')
watched = pd.read_csv('episode_list/watched_episodes.csv')

if unwatched.empty:
    print("You have watched all episodes.")
else:
    if watched.empty:
        print("You haven't started yet. Don't miss out on this incredible opportunity.")
        print(not_started())
    else:
        print(already_started())
