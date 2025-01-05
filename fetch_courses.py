import requests
from bs4 import BeautifulSoup
import json
import csv

def load_config(config_file):
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def fetch_courses(url, cookie, target_courses):
    """Fetch and filter course data from the specified URL."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
    }
    cookies = {
        "ci_session": cookie
    }

    # Send the request
    response = requests.get(url, headers=headers, cookies=cookies)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'offeredCourseTbl'})

    # Filter and collect target course data
    courses = []
    if table:
        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            course_code = cells[1].text.strip()
            if course_code in target_courses:
                course = {
                    'Course Code': course_code,
                    'Section': cells[2].text.strip(),
                    'Faculty': cells[3].text.strip(),
                    'Time': cells[4].text.strip(),
                    'Room': cells[5].text.strip(),
                    'Seats Available': cells[6].text.strip(),
                }
                courses.append(course)
    else:
        print("Course table not found. Please check your cookie or URL.")

    return courses

def save_to_csv(data, output_file):
    """Save the course data to a CSV file."""
    if data:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"Data has been saved to {output_file}")
    else:
        print("No data to save.")

def main():
    # Load configuration
    config = load_config('config.json')
    cookie = config['cookie']
    target_courses = config['courses']

    # Define URL
    url = "https://rds2.northsouth.edu/index.php/common/showofferedcourses"

    # Fetch and save courses
    print("Fetching courses...")
    courses = fetch_courses(url, cookie, target_courses)
    if courses:
        print("Filtered Courses:")
        for course in courses:
            print(course)
        save_to_csv(courses, 'filtered_courses.csv')
    else:
        print("No matching courses found.")

if __name__ == "__main__":
    main()
