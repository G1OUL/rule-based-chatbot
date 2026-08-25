```markdown
# 🤖 Deterministic Logic Engine & Rule-Based Response System

A lightweight, efficient deterministic rule-based response system built to process user commands via strict input sanitization, instant $O(1)$ dictionary lookups, and structured control flow loop logic[cite: 1].

---

## 🚀 Project Overview

The **Deterministic Logic Engine** is a browser and terminal-compatible processing platform built to match predefined user intents and commands deterministically[cite: 1]. 

The application allows a user to input control commands or queries such as:
- Standard greetings (`hello`)[cite: 1]
- System status commands (`status`)[cite: 1]
- Feature inquiries (`features`, `help`)[cite: 1]
- Session termination (`exit`)[cite: 1]

The system processes the text, applies rigorous input cleansing, and instantly returns the mapped response or a controlled fallback prompt[cite: 1].

---

## ✨ Key Features

- 🔍 **Real-Time Command Processor**: Instantly validates and maps user text inputs to corresponding system dictionary keys[cite: 1].
- ⚡ **$O(1)$ Intent Matching**: Utilizes optimized dictionary data structures for immediate command retrieval without nested search logic[cite: 1].
- 🛡️ **Strict Input Sanitization**: Automatically normalizes raw inputs using `.toLowerCase()` and `.trim()` (or Python equivalents) to handle trailing spaces and casing variations seamlessly[cite: 1].
- 🔄 **Stable Control Flow Loop**: Implements predictable execution logic adhering to the Input-Process-Output (IPO) model with safe exit procedures[cite: 1].
- 🌐 **Interactive Web Interface**: Complete with a clean front-end client (`index.html`) so users can test commands directly in their browser[cite: 1].

---

## 🛠️ Tech Stack

- **Languages Used**: HTML5, CSS3, JavaScript (Vanilla JS), Python[cite: 1]
- **Concepts Used**: DOM manipulation, dictionary mapping, $O(1)$ lookups, input sanitization, and structured control loops[cite: 1].

---

## 📂 Project Structure

```text
rule-based-chatbot/
│
├── index.html       # Interactive web-based browser interface
├── main.py          # Core Python terminal engine script
└── README.md        # Project documentation

```

---

## 🏃 How to Run the Project

### Option 1: Run via Web Browser (Live Demo)

1. Open the `index.html` file in any modern web browser.


2. Type commands into the input interface and click **Send** to view instant engine outputs.



### Option 2: Run via Python Terminal

1. Clone the repository:


```bash
git clone [https://github.com/G1OUL/rule-based-chatbot.git](https://github.com/G1OUL/rule-based-chatbot.git)
cd rule-based-chatbot

```


2. Execute the engine script:


```bash
python main.py

```



---

## 🎯 Use Cases

* Portfolio demonstration of core algorithm and logic design


* Lightweight command-line routing simulator


* Foundational prototype for deterministic automated responders and text triage tools



---

## ⚠️ Important Note

This project is built for educational, portfolio, and logic demonstration purposes. It highlights efficient data structuring and software engineering patterns in a lightweight environment.
