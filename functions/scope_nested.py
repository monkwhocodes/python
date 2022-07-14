def output_greeting(name):
    """Out put a greeting for a givein name"""
    message = f'Hello {name}'
    
    def output_greeting_to_screen():
        """Set greeting message"""
        print(message)
        
    output_greeting_to_screen()
    
output_greeting('Mayur')
    
    
        