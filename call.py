from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from datetime import datetime, timedelta
import time

# Your Twilio account details
account_sid = 'your_account_sid_detail' 
auth_token = 'your_auth_token' 
twilio_number = 'your_twilio_number'

client = Client(account_sid, auth_token)

def make_call():
    # Get user input
    to_number = input("Enter the recipient's phone number (with country code): ")
    message = input("Enter the message to be spoken in the call: ")
    
    # Create TwiML response
    twiml = VoiceResponse()
    twiml.say(message)
    
    # Ask if user wants to call now or later
    choice = input("Call now (N) or later (L)? ").upper()
    
    if choice == 'N':
        # Make call immediately
        make_actual_call(to_number, str(twiml))
        print("Call initiated!")
    
    elif choice == 'L':
        # Get time for scheduled call
        hour = int(input("Enter hour to call (0-23): "))
        minute = int(input("Enter minute to call (0-59): "))
        
        # Calculate call time
        now = datetime.now()
        call_time = now.replace(hour=hour, minute=minute, second=0)
        
        # If the time is in the past, schedule for tomorrow
        if call_time <= now:
            call_time += timedelta(days=1)
        
        # Wait until the scheduled time
        wait_time = (call_time - now).total_seconds()
        print(f"Call scheduled for {call_time.strftime('%Y-%m-%d %H:%M')}")
        time.sleep(wait_time)
        
        # Make the call
        make_actual_call(to_number, str(twiml))
        print("Scheduled call initiated!")
    
    else:
        print("Invalid choice. Please run the program again.")

def make_actual_call(to_number, twiml):
    call = client.calls.create(
        twiml=twiml,
        to=to_number,
        from_=twilio_number
    )
    print(f"Call SID: {call.sid}")

# Run the function
make_call()