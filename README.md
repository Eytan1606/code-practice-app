# Code Practice App

A simple command-line application for practicing coding challenges and tracking your progress.

## 🎯 Overview

The Code Practice App helps developers sharpen their algorithmic and problem-solving skills in a familiar CLI environment. It provides:

* A collection of coding challenges across various categories (e.g., arrays, strings, sorting).
* An interactive interface to select and run challenges.
* Progress tracking to record completed problems and timestamps.
* A modular design for easy extension and addition of new challenges.

---

## 🚀 Features

* **Interactive CLI**: Navigate menus and select problems to solve.
* **Multiple Categories**: Algorithms grouped by topic (Arrays, Linked Lists, Recursion, etc.).
* **Automated Testing**: Built-in test cases to verify your solutions.
* **Progress Tracking**: Records solved challenges in a local JSON file.
* **Extensible Architecture**: Easily add new problems by following a template.

---

## 🏗️ Project Structure

```bash
code-practice-app/
├── challenges/           # Challenge modules (one file per problem)
│   ├── array_sum.py
│   ├── binary_search.py
│   └── ...
├── data/                 # Local storage for progress tracking
│   └── progress.json
├── tests/                # Unit tests for each challenge
│   └── test_array_sum.py
├── cli.py                # Main entry point and menu logic
├── utils.py              # Helper functions and common utilities
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Eytan1606/code-practice-app.git
   cd code-practice-app
   ```

2. **Set up a virtual environment (optional but recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Usage

* **Start the CLI**

  ```bash
  python cli.py
  ```

* Follow the on-screen menu to:

  1. Select a challenge category.
  2. Choose a specific problem.
  3. Edit the solution template and run tests.
  4. View your progress and solved problems.

* **Run all tests**

  ```bash
  pytest
  ```

---

## ✨ Adding New Challenges

1. Create a new Python file in `challenges/`, e.g. `unique_paths.py`.
2. Implement your function with a clear docstring.
3. Add corresponding unit tests in `tests/`, e.g. `test_unique_paths.py`.
4. Register the challenge in `cli.py` menu structure.

---

## 👨‍💻 Author

**Eytan Cabalero**
GitHub: [@Eytan1606](https://github.com/Eytan1606)

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

