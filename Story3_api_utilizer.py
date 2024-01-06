import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("story3_api_key")

def create_story(api_key, title, body):
    # API endpoint URL for creating a new story
    api_url = "https://story3.com/api/v2/stories"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": api_key
    }

    # Request body
    request_body = {
        "title": title,
        "body": body,
    }

    try:
        # Make the POST request
        response = requests.post(api_url, json=request_body, headers=headers)

        # Check if the request was successful (status code 201)
        if response.status_code == 201:
            print("Story created successfully!")
            story_data = response.json()
            # publish_story(api_key, story_data['hashId'])
            return story_data
        else:
            print(f"Failed to create story. Status code: {response.status_code}")
            print("Error response:", response.text)

    except requests.RequestException as e:
        print("Error making API request:", e)


def publish(api_key, twist_hash_id):
    # API endpoint URL for publishing a twist
    api_url = f"https://story3.com/api/v2/twists/{twist_hash_id}/publish"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": api_key
    }
    # An empty JSON object as the request body
    request_body = {}

    try:
        # Make the POST request
        response = requests.post(api_url, json=request_body, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 201:
            print("Published successfully!")
            # Access the response JSON if needed
            published_twist_data = response.json()
            # print("Published Details:", published_twist_data)
        else:
            print(f"Failed to publish. Status code: {response.status_code}")
            print("Error response:", response.text)

    except requests.RequestException as e:
        print("Error making API request:", e)


def create_twist(api_key, hash_parent_id, title, body, is_extra_twist=True):
    # API endpoint URL for creating a new twist
    api_url = "https://story3.com/api/v2/twists"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-auth-token": api_key
    }

    # Request body
    request_body = {
        "hashParentId": hash_parent_id,
        "isExtraTwist": is_extra_twist,
        "title": title,
        "body": body
    }

    try:
        # Make the POST request
        response = requests.post(api_url, json=request_body, headers=headers)

        # Check if the request was successful (status code 201)
        if response.status_code == 201:
            print("Twist created successfully!")
            # Access the response JSON if needed
            twist_data = response.json()
            # print("Twist Details:", twist_data)
            # publish_twist(api_key, twist_data['hashId'])
            return twist_data
        else:
            print(f"Failed to create twist. Status code: {response.status_code}")
            print("Error response:", response.text)

    except requests.RequestException as e:
        print("Error making API request:", e)



def publish_story(story_title, story, twists_data):
    """Input
        Story_title
        Story,
        Twist_data: [('Twist 1 Title modified ', 'sT w ist 1', 0), ...]
    """
    hash_id_records = []

    story_data = create_story(api_key, story_title, story)

    if story_data:
        story_hashid = story_data['hashId']
        hash_id_records.append(story_hashid)

        for twist in twists_data:

            twist_title = twist[0]
            twist_body = twist[1]
            parent_hashid = hash_id_records[twist[2]]

            twist_data = create_twist(api_key, parent_hashid, twist_title, twist_body)

            if twist_data:
                twist_hashid = twist_data['hashId']
                hash_id_records.append(twist_hashid)

        for hash_id in hash_id_records:
            publish(api_key, hash_id)

