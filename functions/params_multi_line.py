def output_welcome_text(first_name, 
                        last_name, 
                        age, 
                        location, 
                        returing_user=False):
    """output welcome text with users details"""
    if returing_user:
        msg_start= f'Welcome back {first_name} {last_name}'
    else:
        msg_start= f'Welcome {first_name} {last_name}'
    msg = f'{msg_start} You are {age} and from {location}.'   
    print(msg)
    
output_welcome_text('Mayur', 
                    'Sangani', 
                    age=44, 
                    location='London',
                    returing_user=True)
       

    
    