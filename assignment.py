import requests
import html

# URL of the Time.com website
url = "https://time.com"

try:
    # Make a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print("Successfully fetched the Time.com website.")

        # Find the position of the starting tag for each story
        start_tag = '<h2 class="title"><a href="'
        start_indices = [pos+len(start_tag) for pos in range(response.text.count(start_tag))]

        # Extract the latest 6 stories
        latest_stories = []
        for start_index in start_indices[:6]:
            end_index = response.text.find('</a>', start_index)

            if end_index == -1:
                break

            story_html = response.text[start_index:end_index]
            title_start = story_html.find('>') + 1
            title_end = story_html.rfind('<')
            title = html.unescape(story_html[title_start:title_end].strip())  # Decode HTML entities

            link_start = story_html.find('href="') + 6
            link_end = story_html.find('"', link_start + 1)
            link = url + story_html[link_start:link_end].strip()

            latest_stories.append({"title": title, "link": link})

        print("Latest stories:")
        print(latest_stories)

    else:
        # Print an error message if the request was not successful
        print(f"Error: Unable to fetch Time.com, Status Code: {response.status_code}")

except Exception as e:
    # Print an error message if an exception occurs
    print(f"Error: {str(e)}")
