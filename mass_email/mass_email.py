import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mass_email(sender_name, sender_email, sender_password, recipients, emails_per_recipient):
    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)  
        server.starttls()  
        server.login(sender_email, sender_password)

        for recipient in recipients:
            for i in range(emails_per_recipient): 
                # Create the email
                message = MIMEMultipart()
                message['From'] = f"{sender_name}"
                message['To'] = recipient['email']
                message['Subject'] = f"Personalized Greetings (Email {i+1})"

                # HTML email content
                body = f"""
                <html>
                <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
                    <div style="max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
                        <h2 style="color: #4CAF50;">Hello {recipient['name']},</h2>
                        <p>This is email <strong>#{i+1}</strong> of {emails_per_recipient}. We are thrilled to connect with you!</p>
                        <p style="margin-top: 20px;">
                            Thank you for being part of our community. If you have any questions, feel free to reach out at <a href="mailto:support@example.com">support@example.com</a>.
                        </p>
                        <hr style="border: none; border-top: 1px solid #eee; margin: 20px 0;">
                        <p style="text-align: center; font-size: 0.9em; color: #999;">
                            &copy; {2024}. All Rights Reserved. | Company Name
                        </p>
                    </div>
                </body>
                </html>
                """
                message.attach(MIMEText(body, 'html'))

                # Send the email
                server.sendmail(sender_email, recipient['email'], message.as_string())
                print(f"Email {i+1} sent to {recipient['name']} at {recipient['email']}")

        server.quit()
        print("All emails sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# User input for number of emails per recipient
try:
    emails_per_recipient = int(input("Enter the number of emails to send per recipient: "))
    if emails_per_recipient < 1:
        raise ValueError("The number of emails must be at least 1.")
except ValueError as ve:
    print(f"Invalid input: {ve}")
    exit(1)

# Sender's email credentials
SENDER_NAME = "Support Team"
SENDER_EMAIL = "enter hacked email id "
SENDER_PASSWORD = ""  # app password 

# Recipient list
RECIPIENTS = [
    {"name": "Recipient", "email": "recipient@gmail.com"}
]

send_mass_email(SENDER_NAME, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENTS, emails_per_recipient)

