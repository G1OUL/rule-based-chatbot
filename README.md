# rule-based-chatbot
This project is a Deterministic Logic Engine developed as part of the Industrial Training Kit. It serves as a foundational "control layer" by implementing the IPO (Input-Process-Output) Model.
Features:-
Input/Sanitization: Normalizes user input using .lower() and .strip() to ensure consistent processing regardless of formatting.
Logic Skeleton: Utilizes a dictionary-based lookup for $O(1)$ efficiency, ensuring 100% predictable, "white-box" behavior.
Control Flow: Operates in a continuous while loop with a defined exit strategy to maintain system stability.
Architecture (IPO Model)
Input: Raw data is sanitized and normalized.
Process: The system matches intents against a pre-defined knowledge base.
Output: A clean, deterministic response is generated.
