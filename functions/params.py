def output_welcom_text(name, returning_user=True):
    """output welcome text with provided name"""
    if returning_user:
        message = f'Welcome back {name}'
    else:
        message = f'Welcom {name}'
    print(message)


    
output_welcom_text(name='Mayur')
output_welcom_text('parth', False)
output_welcom_text('Simran', returning_user=True) 

  