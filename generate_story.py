import os
import openai
import pandas as pd
openai.api_key = "sk-6KEdgdgdRGoDQSaFHT3BlbkFJ7f5tcUKXLAdWuvq50mu6"

def create_story(base_story_prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=base_story_prompt,
        temperature=0.2,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    result = response["choices"][0]["text"]
    return result

def get_fullstory(base_story, categories):
    prompt = f"""
    #You have to create a story using 'BaseStory' and 'categories'.
    #Story should be of length between 100 to 400 charachter. 
    #Begin with a clear concept or theme for your story.
    #It could be a unique situation, a compelling character, or a thought-provoking question.
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
        Generate 5 twists for the below story.
        Each twists will be seperated by '^' 
        Twist should be of length Upto 200 charaters long.
        Make each twist interesting, and twist can be related to each other.
         
        Output Example:
        twist_1 ^ twist_2 ^ twist_3 ^ twist_4 ^ twist_5
        
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
    story_twists = generate_storytwist(storyfull).split('^')
    story_twists_titles = [generate_twisttitle(twist) for twist in story_twists]
    """
    print('title', story_title)
    print('Story', storyfull)
    print("Twists", story_twists)
    print("Twists titles", story_twists_titles)
    """
    return [story_title, storyfull, story_twists_titles, story_twists]

#story = "there was a boy who live in village, every night he hear some strange sound"
#catg = ['Horror', 'Trill']
