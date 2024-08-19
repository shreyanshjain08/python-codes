import pywhatkit
from datetime import datetime, timedelta

def send_whatsapp_message():
    # Get user input
    phone_number = input("Enter the phone number (with country code): ")
    message = input("Enter your message: ")
    
    # Ask if user wants to send now or later
    choice = input("Send now (N) or later (L)? ").upper()
    
    if choice == 'N':
        # Send message immediately
        pywhatkit.sendwhatmsg_instantly(phone_number, message)
        print("Message sent!")
    
    elif choice == 'L':
        # Get time for scheduled message
        hour = int(input("Enter hour to send (0-23): "))
        minute = int(input("Enter minute to send (0-59): "))
        
        # Calculate send time
        now = datetime.now()
        send_time = now.replace(hour=hour, minute=minute, second=0)
        
        # If the time is in the past, schedule for tomorrow
        if send_time <= now:
            send_time += timedelta(days=1)
        
        # Schedule the message
        pywhatkit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)
        print(f"Message scheduled for {send_time.strftime('%Y-%m-%d %H:%M')}")
    
    else:
        print("Invalid choice. Please run the program again.")

# Run the function
send_whatsapp_message()