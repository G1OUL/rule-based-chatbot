def main():
    # Knowledge Base: Dictionary with 5+ intents
    responses = {
        'hello': 'Hi! I am your DecodeLabs AI assistant.',
        'help': 'I can respond to keywords like: hello, status, project, mission, or exit.',
        'status': 'System is online and running in a deterministic state.',
        'project': 'Project 1: Rule-Based AI Chatbot.',
        'mission': 'Mastering logic before generative AI.'
    }
    
    print("--- DecodeLabs Logic Engine Initialized ---")
    
    # Infinite Cycle
    while True:
        # Input & Sanitization
        raw_input = input('You: ')
        clean_input = raw_input.lower().strip()
        
        # Kill Command
        if clean_input == 'exit':
            print("Bot: Shutting down. Goodbye!")
            break
            
        # Atomic Lookup & Fallback
        reply = responses.get(clean_input, 'I do not understand that command.')
        print(f"Bot: {reply}")

if __name__ == "__main__":
    main()