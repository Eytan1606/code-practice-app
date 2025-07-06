# Code Practice App (Java OOP & Persistence)

A console-based Java application showcasing core Object-Oriented Programming concepts, custom data structures, exception handling, and simple file persistence.

---

## 🎯 Overview

This project functions as a lightweight college/admin management system with support for multiple entity types (students, lecturers, professors, doctors, researchers). It demonstrates:

* **Inheritance & Interfaces**: Shared behaviors via `IEmployable`, abstract classes, and concrete subclasses.
* **Custom Collections**: `CustomArray<T>` for dynamic storage.
* **Exception Handling**: Domain-specific exceptions (`ValidationException`, `NullInputException`, `DuplicateEntityException`, `EntityNotFoundException`, `AppException`).
* **Persistence Layer**: Serialize/deserialize `College` object graph to `.dat` files with `Persistence` utility.
* **Modular Design**: Separation of concerns across packages (`app`, `models`, `utils`).

---

## 🛠️ Features

* **Add / Remove / Search Entities**
* **Type-safe storage** using a generic array wrapper
* **Custom input validation** with clear error messages
* **File-based persistence** via Java Serialization
* **Extensible architecture** for future entity types

---

## 📁 Project Structure

```
CodePracticeApp/
├── src/
│   └── app/
│       ├── Main.java                # Entry point & menu handling
│       ├── Persistence.java         # Load/save utilities
│       └── exceptions/              # Custom exception classes
│           ├── AppException.java
│           ├── DuplicateEntityException.java
│           ├── EntityNotFoundException.java
│           ├── NullInputException.java
│           └── ValidationException.java
│   └── models/
│       ├── College.java             # Root domain container
│       ├── Person.java              # Abstract base class
│       ├── IEmployable.java         # Interface for employable entities
│       ├── Lecturer.java            # Implements IEmployable
│       ├── Professor.java
│       ├── Doctor.java
│       ├── Researcher.java
│       ├── Department.java
│       ├── Degree.java
│       └── Committee.java
│   └── utils/
│       └── CustomArray.java         # Generic dynamic array
└── README.md                         # Project documentation
```

---

## ⚙️ Build & Run

1. **Compile sources**

   ```bash
   javac -d out src/app/*.java src/models/*.java src/utils/*.java
   ```
2. **Run application**

   ```bash
   java -cp out app.Main
   ```
3. **Follow the console menu** to add, list, delete, or search entities. Data is saved to `<CollegeName>.dat` files in the working directory.

---

## 🧪 Usage Example

```
1) Create New College
2) Add Lecturer
3) Add Student
4) View All Entities
5) Save & Exit
Enter choice: 2
> Enter Lecturer ID: L001
> Enter Name: Dr. Smith
> Enter Department: Computer Science
Lecturer added successfully.
```

---

## 👨‍💻 Author

**Eytan Cabalero** (GitHub: [@Eytan1606](https://github.com/Eytan1606))

---

## 📄 License

This project is licensed under the MIT License © 2025 Eytan Cabalero
