# app.py
from flask import Flask, render_template, request, redirect, url_for
from Story3_api_utilizer import publish_story, Analytics
from generate_story import generate_story
app = Flask(__name__)

# Mockup data for story categories
story_categories = ["Adventure", "Mystery", "Fantasy",
                    "Science Fiction", "Romance", "Historical Fiction",
                    "Thriller", "Horror", "Dystopian",
                    "Comedy", "Slice of Life", "Superhero"]

@app.route('/')
def index():
    return render_template('index.html', story_categories=story_categories)

@app.route('/create_story', methods=['POST'])
def create_story():

    base_story = request.form['base_story']
    selected_categories = request.form.getlist('categories')
    storydata = generate_story(base_story, selected_categories)
    #[story_title, storyfull, story_twists_titles, story_twists]
    # Call your create_story() function here with story_title, base_story, and selected_categories
    # full_story, twists = create_story(story_title, base_story, selected_categories)

    # Mock data for demonstration purposes
    full_story = storydata[1]
    twists = []

    for i in range(len(storydata[2])):
        twists.append((storydata[2][i],storydata[3][i],i))

    story_title = storydata[0]

    return render_template('edit_story.html', story_title=story_title, full_story=full_story, twists=twists)

@app.route('/publish', methods=['POST'])
def publish():
    if request.form['action'] == 'approve':

        # Get the approved story, twist titles, and ranks from the form
        story_title = request.form['story_title']
        full_story = request.form['full_story']
        twist_titles = request.form.getlist('twist_titles[]')
        twists_content = request.form.getlist('twists_content[]')
        ranks = request.form.getlist('ranks[]')

        twists_data = list(zip(twist_titles, twists_content, map(int, ranks)))

        """print("Story Title:", story_title)
        print("Full Story:", full_story)
        print("Twist Titles:", twist_titles)
        print("Twists Data:", twists_data)
        """

        publish_story(story_title, full_story, twists_data)

        return redirect(url_for('index'))
    elif request.form['action'] == 'reject':
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    dashboard_data = Analytics()
    unique_viewers = sum(int(item['viewers']) for item in dashboard_data)
    freeConversion = sum(float(item['freeConversion']) for item in dashboard_data)
    paidConversion = sum(float(item['paidConversion']) for item in dashboard_data)
    column_sums = {
        'views': sum(int(item['views']) for item in dashboard_data),
        'revenue': sum(float(item['revenue']) for item in dashboard_data),
        'freeTwistUnlockers': sum(int(item['freeTwistUnlockers']) for item in dashboard_data),
        'paidTwistUnlockers': sum(int(item['paidTwistUnlockers']) for item in dashboard_data),
        'freeConversion': freeConversion,
        'paidConversion': paidConversion,
        'viewers': unique_viewers,
        'CRFree': freeConversion/len(dashboard_data),
        'CRPaid': paidConversion/len(dashboard_data),
    }

    return render_template('dashboard.html', data=dashboard_data, column_sums=column_sums)

if __name__ == '__main__':
    app.run(debug=True)
