# 📘 Assignment: Text Processing in Python

## 🎯 Objective

Students will practice string manipulation, parsing, and basic text analytics by implementing small utility functions to clean text, compute word frequencies, and report the most common words.

## 📝 Tasks

### 🛠️ Task 1 — Clean and normalize text

#### Description
Implement a function that takes a raw text string and returns a cleaned, normalized version. Normalization should include converting to lowercase and removing basic punctuation.

#### Requirements
Completed program should:

- Provide a `clean_text(text: str) -> str` function that lowercases and removes punctuation (keep whitespace and alphanumeric characters).
- Strip extra whitespace so words are separated by single spaces.

### 🛠️ Task 2 — Word frequency

#### Description
Implement a function to compute word frequencies from cleaned text and return a mapping of word -> count.

#### Requirements

- Provide a `word_frequencies(text: str) -> dict` function that returns a dictionary with words as keys and integer counts as values.
- Ignore empty tokens.

### 🛠️ Task 3 — Top N words and file input (optional)

#### Description
Add a helper that returns the top N most frequent words and an optional mode to read text from a file.

#### Requirements

- Provide `top_n_words(freqs: dict, n: int) -> list[tuple[str, int]]` which returns a list of (word, count) tuples ordered by count descending.
- (Optional) Add a command-line mode to read a file path and print the top 10 words.

## Deliverables

- `starter-code.py` in this folder with the function stubs and a small example in `if __name__ == "__main__":` demonstrating usage.
- A short write-up in this `README.md` describing any assumptions and decisions.

## Hints

- Use Python's `str` methods and `re` for simple cleaning.
- `collections.Counter` can simplify frequency counting but you may implement it manually.
- Make sure your functions handle empty strings gracefully.

## Evaluation

- Correctness of the `clean_text`, `word_frequencies`, and `top_n_words` functions.
- Reasonable handling of edge cases (empty input, punctuation-only input).
- Clear, documented code in `starter-code.py`.
