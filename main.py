def main():
    # Knowledge Base: Dictionary with intents and clean responses
    responses = {
        'hello': 'Hi! I am AI assistant.',
        'help': 'I can respond to keywords like: hello, status, project, mission, or exit.',
        'status': 'System is online and running in a deterministic state.',
        'project': 'Project 1: Rule-Based AI Chatbot.',
        'mission': 'Mastering logic before generative AI.'
    }
    
    print("--- DecodeLabs Logic Engine Initialized ---")
    print("Type 'help' for options or 'exit' to quit.\n")
    
    # Infinite Cycle
    while True:
        try:
            # Input & Sanitization
            raw_input = input('You: ')
            clean_input = raw_input.lower().strip()
            
            # Skip empty inputs to prevent redundant prompt loops
            if not clean_input:
                continue
            
            # Kill Command
            if clean_input == 'exit':
                print("Bot: Shutting down. Goodbye!")
                break
                
            # Atomic Lookup & Fallback ($O(1) dictionary retrieval)
            reply = responses.get(clean_input, 'I do not understand that command. Type "help" for valid options.')
            print(f"Bot: {reply}\n")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Force shutdown detected. Goodbye!")
            break

if __name__ == "__main__":
    main()
