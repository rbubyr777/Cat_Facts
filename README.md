# Cat Facts API Test Framework

This test framework uses **pytest** and **requests** to test the functionality of the [Cat Facts API](https://alexwohlbruck.github.io/cat-facts/), which provides random cat facts. The tests validate the API's responses to ensure it returns the expected data.

## Features

The tests perform the following steps:
1. Retrieve a single random cat fact.
2. Retrieve multiple random cat facts with a specified limit (from 0 to 10).
3. Validate that the responses contain the expected fields.

## Test Cases

| Test Case                        | Description                                                     | Input Parameter    | Expected Outcome                                                                                      |
|----------------------------------|-----------------------------------------------------------------|--------------------|-------------------------------------------------------------------------------------------------------|
| `test_get_random_fact`           | Retrieves a single random cat fact.                             | None               | Status code `200`; JSON data with `"text"` and `"type"` fields; `"type"` should be `"cat"`.           |
| `test_get_multiple_random_facts` | Retrieves multiple random cat facts for a given count (1-10).   | `num_facts` (1-10)| Status code `200`; JSON data is a list of `num_facts` dictionaries, each containing `"text"` and `"type"` fields.|

### Prerequisites

- **Python 3.7+**
- **pytest** and **requests** modules

## Installation

1. Clone this repository and navigate to the project directory.

   ```bash
   git clone <repository-url>
   cd cat_facts_tests
