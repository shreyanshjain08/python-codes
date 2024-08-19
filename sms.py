

from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Your Twilio account details
account_sid = '' 
auth_token = '' 
twilio_number = ''
client = Client(account_sid, auth_token)

def send_sms():
    # Get user input
    to_number = input("Enter the recipient's phone number (with country code): ")
    message = input("Enter your message: ")
    
    # Ask if user wants to send now or later
    choice = input("Send now (N) or later (L)? ").upper()
    
    if choice == 'N':
        # Send message immediately
        send_message(to_number, message)
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
        
        # Wait until the scheduled time
        wait_time = (send_time - now).total_seconds()
        print(f"Message scheduled for {send_time.strftime('%Y-%m-%d %H:%M')}")
        time.sleep(wait_time)
        
        # Send the message
        send_message(to_number, message)
        print("Scheduled message sent!")
    
    else:
        print("Invalid choice. Please run the program again.")

def send_message(to_number, message):
    message = client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )
    print(f"Message SID: {message.sid}")

# Run the function
send_sms()