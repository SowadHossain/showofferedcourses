# Fetch Courses from NSU Offered Course List

This project is a Python script to scrape and filter course data from the North South University's "Offered Course List" page. It allows users to input their desired courses and session cookies via a configuration file, making the process highly customizable and modular.

---

## Features
- Fetches all available courses from the NSU course offerings page.
- Filters courses based on user-specified course codes.
- Uses a configuration file (`config.json`) for easy updates to cookie and target courses.
- Saves the filtered course data to a CSV file for further use.

---

## Requirements
To run the script, you need the following:

1. Python 3.6 or later
2. Required Python libraries:
   - `requests`
   - `beautifulsoup4`
   - `csv`

---

## Installation

### Step 1: Clone or Download the Repository
Download the project files or clone the repository:
```bash
https://github.com/your-username/fetch-courses.git
```

### Step 2: Install Required Libraries
Install the required libraries using `pip`:
```bash
pip install requests beautifulsoup4
```

---

## Usage

### Step 1: Update the Configuration File

Create or update the `config.json` file with the following structure:
```json
{
    "cookie": "your_cookie_here",
    "courses": ["BIO103L", "CSE231", "CSE231L", "EEE141", "EEE141L", "MAT250", "PHY107"]
}
```
- **`cookie`**: The session cookie required to access the course data. Obtain it from your browser after logging into the website.
- **`courses`**: List of course codes you want to fetch.

### Step 2: Run the Script
Execute the script using Python:
```bash
python fetch_courses.py
```

### Step 3: View the Output
- The script will print the filtered courses in the terminal.
- The filtered data will be saved in `filtered_courses.csv` in the same directory.

---

## Directory Structure
```plaintext
fetch-courses/
|-- fetch_courses.py      # Main script to fetch and filter courses
|-- config.json           # Configuration file with cookie and course codes
|-- filtered_courses.csv  # Output file with filtered courses
```

---

## Example Output

### Terminal Output
```plaintext
Fetching courses...
Filtered Courses:
{'Course Code': 'BIO103L', 'Section': '1', 'Faculty': 'TBA', 'Time': 'RA 01:00 PM - 02:30 PM', 'Room': 'NAC207', 'Seats Available': '33'}
{'Course Code': 'CSE231', 'Section': '2', 'Faculty': 'TBA', 'Time': 'RA 04:20 PM - 05:50 PM', 'Room': 'NAC206', 'Seats Available': '34'}
...
Data has been saved to filtered_courses.csv
```

### CSV File Output (`filtered_courses.csv`)
| Course Code | Section | Faculty | Time                   | Room   | Seats Available |
|-------------|---------|---------|------------------------|--------|-----------------|
| BIO103L     | 1       | TBA     | RA 01:00 PM - 02:30 PM | NAC207 | 33              |
| CSE231      | 2       | TBA     | RA 04:20 PM - 05:50 PM | NAC206 | 34              |

---

## Troubleshooting

1. **No Table Found**:
   - Ensure the `cookie` in `config.json` is valid and not expired.
   - Check if the CAPTCHA is blocking access; solve it manually if necessary.

2. **Empty Output**:
   - Verify that the course codes in `config.json` match those available on the website.

3. **Errors with Libraries**:
   - Ensure all required libraries are installed with the correct versions.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- **BeautifulSoup** for HTML parsing.
- **Requests** for handling HTTP requests.

For further assistance, feel free to raise an issue or contact the project maintainer.

