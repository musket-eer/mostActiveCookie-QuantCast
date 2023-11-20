Most Active Cookie
Overview
This simple Python program, most_active_cookie.py, is designed to analyze a time-stamped sorted list of cookies and retrieve the most active cookie for a given date. The associated test suite is contained in the tests.py file.

Usage
Running the Program
To use the program, execute the following command in the terminal:

./most_active_cookie.py filename -d date

filename: The name of the file containing the time-stamped sorted list of cookies.
-d date: The target date for which you want to find the most active cookie.

Example:
./most_active_cookie.py cookie_data.txt -d 2023-01-01
Running Tests
To run the test suite, execute the following command in the terminal:


./tests.py
This will run a series of tests to ensure the correctness of the program.

File Structure
most_active_cookie.py: Contains the main program for retrieving the most active cookie for a given date.
tests.py: Includes a set of tests to verify the functionality of the program.
cookiedata.csv: An example file containing a time-stamped sorted list of cookies for testing purposes.
Input Format
The input file (cookiedata.csv) is expected to have the following format:

cookie1, 2018-12-09T14:19:00+00:00

Each line represents a cookie and its corresponding timestamp. 

Output Format
When the program is executed, it will output the most active cookie(s) for the specified date.

Example output:
cookie1
cookie2


Dependencies
This program does not require any external dependencies.

Notes
Ensure that the input file is correctly formatted and contains valid timestamped data.
The program assumes the input file is sorted by timestamp.
If multiple cookies have the same activity count for the specified date, all will be included in the output.