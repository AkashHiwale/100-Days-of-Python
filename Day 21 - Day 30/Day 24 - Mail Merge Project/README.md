# Day 24 - Mail Merge Project

This project reads a letter template and a list of names, then creates personalized invitation files for each name. It turns a single template into multiple completed letters using simple file processing.

## What This Project Shows

* Reads text from input files and uses the content in the program.
* Processes a list of names to produce unique output for each entry.
* Replaces placeholder text in a template with actual values.
* Writes new text files to an output folder.

## How to Run

### Prerequisites

* Python 3.8 or newer
* A terminal or command prompt

### Steps

1. Open the project folder in your editor or terminal.
2. Make sure the `Input/Letters/starting_letter.txt` file and `Input/Names/invited_names.txt` file exist.
3. Open a terminal in the `Day 24 - Mail Merge Project` folder.
4. Run the application.

### Run Command

```bash
python main.py
```

### Dependencies

> Note: This project uses only the standard library and does not require additional packages.

## Concepts Learnt

* **File input/output** – Opens files to read template text and names, then writes new output files.
* **String replacement** – Replaces a placeholder value (`[name]`) in the letter template with each invited name.
* **Looping through data** – Uses a loop to generate a separate invitation for every name in the list.
* **Formatted file paths** – Creates output file names dynamically using the current name value.
