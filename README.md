# Most Active Cookie

## Overview

This straightforward Python program, `most_active_cookie.py`, is crafted to analyze a time-stamped, sorted list of cookies and pinpoint the most active cookie for a specified date. The accompanying test suite resides in the `tests.py` file.

## Usage

### Running the Program

Execute the following command in the terminal:

./most_active_cookie.py filename -d date

- **filename:** The file containing the time-stamped, sorted list of cookies.
- **-d date:** The target date to identify the most active cookie.

**Example:**

./most_active_cookie.py cookiedata.csv -d 2023-01-01

### Running Tests

To validate the program's accuracy, run the test suite using the following command:

./tests.py

This command initiates a series of tests ensuring the program's correctness.

## File Structure

- **most_active_cookie.py:** The main program for extracting the most active cookie for a specified date.
- **tests.py:** A suite of tests to verify program functionality.
- **cookiedata.csv:** An example file with a time-stamped, sorted list of cookies for testing purposes.

## Input Format

The input file (`cookiedata.csv`) should adhere to the following format:


cookie1, 2018-12-09T14:19:00+00:00

Each line signifies a cookie along with its corresponding timestamp.

## Output Format

Upon execution, the program outputs the most active cookie(s) for the specified date.

**Example output:**

cookie1

cookie2


## Dependencies

This program operates independently without relying on external dependencies.

## Notes

- Validate that the input file is correctly formatted and contains valid timestamped data.
- The program assumes the input file is sorted by timestamp.
- If multiple cookies share the same activity count for the specified date, all will be included in the output.

