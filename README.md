# Fetch Courses from NSU Offered Course List

This project is a Python script to scrape and filter course data from the North South University's "Offered Course List" page. It allows users to input their desired courses and session cookies via a configuration file, making the process highly customizable and modular.

---

## Features
- Fetches all available courses from the NSU course offerings page.
- Filters courses based on user-specified course codes.
- Ensures that only courses with available seats are included in the output.
- Uses a configuration file (`config.json`) for easy updates to cookies and target courses.
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
- **`cookie`**: The session cookie required to access the course data. See [How to Obtain the Cookie](#how-to-obtain-the-cookie) below for instructions.
- **`courses`**: List of course codes you want to fetch.

### Step 2: Run the Script
Execute the script using Python:
```bash
python fetch_courses.py
```

### Step 3: View the Output
- The script will print the filtered courses with available seats in the terminal.
- The filtered data will be saved in `filtered_courses.csv` in the same directory.

---

## How to Obtain the Cookie

The script requires a valid session cookie to access the course data. Follow these steps to obtain the `ci_session` cookie:

1. **Open Developer Tools**:
   - Open the course offerings page in your browser (e.g., Chrome or Firefox).
   - Right-click on the page and select **"Inspect"** or press `Ctrl + Shift + I`.

2. **Navigate to the Network Tab**:
   - Go to the **"Network"** tab in Developer Tools.
   - Reload the page (`F5` or `Ctrl + R`).
   - Look for the request associated with the URL `https://rds2.northsouth.edu/index.php/common/showofferedcourses`.

3. **View Request Headers**:
   - Click on the request for `showofferedcourses`.
   - In the right panel, go to the **"Headers"** tab.
   - Find the `Cookie:` field in the **Request Headers** section.

4. **Copy the Cookie**:
   - Copy the entire value of the `ci_session` cookie.

5. **Paste the Cookie**:
   - Replace the `cookie` value in `config.json` with the copied `ci_session` value.

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
Filtered Courses with Available Seats:
{'Course Code': 'BIO103L', 'Section': '1', 'Faculty': 'TBA', 'Time': 'RA 01:00 PM - 02:30 PM', 'Room': 'NAC207', 'Seats Available': 33}
{'Course Code': 'CSE231', 'Section': '2', 'Faculty': 'TBA', 'Time': 'RA 04:20 PM - 05:50 PM', 'Room': 'NAC206', 'Seats Available': 34}
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

### No Table Found
- Ensure the `cookie` in `config.json` is valid and not expired.
- If CAPTCHA blocks access, solve it manually in your browser before obtaining the cookie.

### Empty Output
- Verify that the course codes in `config.json` match those available on the website.
- Ensure there are available seats for the specified courses.

### Errors with Libraries
- Ensure all required libraries are installed with the correct versions.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- **BeautifulSoup** for HTML parsing.
- **Requests** for handling HTTP requests.

For further assistance, feel free to raise an issue or contact the project maintainer.

