# NATO-Alphabet-Identifier-Classifier

This program reads a NATO alphabet mapping from `alphabet.txt` and a list of identifiers from `identifiers.txt`.  
Each identifier is classified as a **TAG**, **VIN**, or **INVALID** based solely on its length.  

For all valid identifiers, the program outputs the NATO phonetic spelling using the alphabet mapping file.  
At completion, a summary of valid and invalid identifiers is displayed.

---

## ✨ Features

- 📖 Reads NATO phonetic alphabet word mappings from `alphabet.txt`
- 📄 Reads identifiers from `identifiers.txt`
- 🔢 Classifies each identifier by length:
  - **TAG** – valid short identifier
  - **VIN** – valid long identifier
  - **INVALID** – any length outside valid ranges
- 🔊 Spells out valid identifiers using NATO alphabet words
- 📊 Prints totals for:
  - Valid identifiers
  - Invalid identifiers

---

## 🛠️ Built With

- **Python** (no external dependencies)
 
---
## 📁 Project Structure
nato-identifier/
│
├── main.py
├── alphabet.txt
├── identifiers.txt
└── README.md

