# LLM Story Generator Readme

## Introduction

Welcome to the LLM Story Generator! This Python Flask application leverages the power of Large language model to generate stories based on user input. Users can create a base story, and the app will use the OpenAI API to generate a complete story with title and twists. The generated story can then be reviewed and modified before being submitted to Story3.com.

## Prerequisites

- Python 3.10 or higher
- Ensure you have the required dependencies installed by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a file named `.env` in the project root directory to store your OpenAI and Story3 API keys.
2. Add your API keys to the `.env` file in the following format:

```env
openai_api_key="sk-6KEL0YRHPL4AFSGGFJ7f5tcUKXLAdWuvq50mu6"
story3_api_key="RE9sfasfbsa4shsglNzRlMjseggiZDNlNjFiNTA2NmE0YjdjNDkxMzExZmY2YjZhNTJm"
```

## Running the Application

Execute the following command in your terminal to start the Flask application:

```bash
python app.py
```

Visit the link provided in the terminal (open in your browser) to access the application.

## Usage

### Page 1: Input Base Story

![Page 1 Image](https://i.ibb.co/tQX71t0/Screenshot-616.png)

- Users can write a base story on this page.
- The language model will then generate the story's title and twists.

### Page 2: Review Story

![Page 2 Image](https://i.ibb.co/KbQQdGr/Screenshot-619.png)

- Users will see the complete story with title and twists.
- Modifications can be made if necessary.
- Users can put ranks of each twist like '0' if twist comes under story, '2' if twist comes under twist 2 etc
- Users have the option to either approve or reject the story.

### Approval and Submission

- If the user approves the story, it will be submitted to Story3.com.
- The story will now be available on Story3.com for further engagement.
  
### Page 3: Dashboard

![Page 3 Image](https://i.ibb.co/sVkPgmm/dashboard.png)
- User can view stats of all stories here

## Note

- Please keep your API keys secure and do not share them publicly.
- For any issues or inquiries, feel free to contact the project maintainers.

Thank you for using LLM Story Generator!
