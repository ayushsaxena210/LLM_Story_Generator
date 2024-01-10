import os
import openai
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("openai_api_key")

def create_story(base_story_prompt):
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=base_story_prompt,
        temperature=0,
        max_tokens=350,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response["choices"][0]["text"]
    return result


def get_fullstory(base_story, categories):
    prompt = f"""
    #You have to create a story using 'BaseStory' and 'categories' and end the story in suspense.
    #Story should be of length between 200 to 600 charachter. 
    #Begin with a clear concept or theme for your story.
    #Most import Story should have good engagement and interesting.
    #Return only Story, No need to give story title or any heading in output.
    BaseStory: ###{base_story}###
    categories: ###{' '.join(categories)}###
    """
    full_story = create_story(prompt)
    return full_story


def generate_storytitle(story):
    prompt = f"""
    Generate a title for the below story, and only return the title without heading.
    Story: {story}
    """
    storytitle = create_story(prompt)
    return storytitle


def generate_storytwist(story):
    prompt = f"""
        # Generate 5 twists for the below story and return output separated by '\n'
        # Reveal the suspense of the story in twists.
        # Twist should be of length Upto 200 charaters long.
        # Make each twist interesting, and some twist can be related to each other.

        ######         
        Story: {story}
        ######
        """
    storytwists = create_story(prompt)
    return storytwists


def generate_twisttitle(twist):
    prompt = f"""
            Generate a title for below sentence. title should be of max 4 words.
            #{twist}#
            """
    twist_title = create_story(prompt)
    return twist_title


def generate_story(story, catg):
    storyfull = get_fullstory(story, catg)
    story_title = generate_storytitle(storyfull)
    story_twists = generate_storytwist(storyfull).split('\n')[1:]
    story_twists_titles = [generate_twisttitle(twist) for twist in story_twists]
    """
    print('title', story_title)
    print('Story', storyfull)
    print("Twists", story_twists)
    print("Twists titles", story_twists_titles)
    """
    return [story_title, storyfull, story_twists_titles, story_twists]
