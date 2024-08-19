import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

def get_user_input():
    email = input("Enter your email address: ")
    receiver_email = input("Enter the receiver's email address: ")
    password = input("Enter your email password (use an app-specific password if 2FA is enabled): ")
    return email, receiver_email, password

def send_email(email, password, receiver_email, subject, message):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    # Attach the message body to the email
    msg.attach(MIMEText(message, 'plain'))
    try:
        # Set up the server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        # Log in to the server
        server.login(email, password)
        # Send the email
        server.sendmail(email, receiver_email, msg.as_string())
        print("Email has been sent to", receiver_email)
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        # Close the server connection
        server.quit()

def schedule_email(email, password, receiver_email):
    subject = input("Enter the subject of the email: ")
    message = input("Enter the message body of the email: ")
    send_time = input("Enter the time to send the email (format: 'HH:MM' in 24-hour format): ")
    
    # Schedule the email
    schedule.every().day.at(send_time).do(send_email, email, password, receiver_email, subject, message)

    print(f"Email scheduled to be sent at {send_time}.")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for 1 minute

def main():
    email, receiver_email, password = get_user_input()
    
    choice = input("Do you want to send the email instantly or schedule it for later? (instant/schedule): ").strip().lower()
    if choice == 'instant':
        subject = input("Enter the subject of the email: ")
        message = input("Enter the message body of the email: ")
        send_email(email, password, receiver_email, subject, message)
    elif choice == 'schedule':
        schedule_email(email, password, receiver_email)
    else:
        print("Invalid choice. Please enter 'instant' or 'schedule'.")

if __name__ == '__main__':
    main()
