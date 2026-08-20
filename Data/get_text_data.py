import json
import os
import time
import requests

# initialise API key
rapidapi_key = "YOUR_API_KEY" # replace with your Rapid API key

# initialise base url
base_url = "https://instagram-scraper21.p.rapidapi.com"

# initialise headers
headers = {
    "x-rapidapi-key": rapidapi_key,
    "x-rapidapi-host": "instagram-scraper21.p.rapidapi.com",
    "Content-Type": "application/json",
}

# list of union Instagram handles to search
union_usernames = [
    "awunion",
    "cfmeunational",
    "etu_australia",
    "theamwu",
    "rtbuaustralia",
    "twuaus",
    "sdaunion",
    "unitedworkersoz",
    "asunion",
    "professionals.australia",
    "cpsunion",
    "anmf_nursing_midwifery_union",
    "fsu_australia",
    "withmeaa",
]

# list of union body Instagram handles to search
body_usernames = [
    "ausunions",
    "unionsnsw",
    "weare.union",
    "queenslandunions",
    "unionswa",
    "sa_unions",
    "unionsnt",
    "tasunions",
    "unionsact",
]

# initialise output directories
union_dir = "Data/text_data_raw/unions"
body_dir = "Data/text_data_raw/bodies"

# make directories if necessary
os.makedirs(union_dir, exist_ok=True)
os.makedirs(body_dir, exist_ok=True)


def get_posts(username, limit=100):
    """Getter for Instagram posts using Rapid API."""

    url = f"{base_url}/api/v1/posts"

    response = requests.get(
        url,
        headers=headers,
        params={
            "username": username,
            "include_captions": "true",
            "limit": limit,
        },
        timeout=60,
    )

    response.raise_for_status()
    return response.json()


def save_json(data, filepath):
    """Saves retrieved JSON in specified file path"""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def scrape_accounts(usernames, output_dir):
    """Gets posts for given Instagram handle and saves to given output directory"""
    for username in usernames:

        print(f"Downloading {username}...")

        try:
            # get posts using get_posts function
            posts = get_posts(username)

            # create output file
            outfile = os.path.join(output_dir, f"{username}.json")
            save_json(posts, outfile)

            n_posts = len(posts.get("data", {}).get("posts", []))

            # print success message
            print(f"  ✓ {n_posts} posts saved to {outfile}")

        # handle exceptions    
        except Exception as e:
            print(f"  ✗ Failed: {e}")

        # moderate request volume (avoid getting blocked)
        time.sleep(1)

# main workflow
if __name__ == "__main__":
    # get union posts and save to union directory
    print("Unions:")
    scrape_accounts(union_usernames, union_dir)

    # get union body posts and save to union body directory
    print("\nPeak bodies:")
    scrape_accounts(body_usernames, body_dir)