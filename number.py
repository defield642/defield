from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send SMS
def send_sms(to_number, from_number, message):
    message = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    return message.sid

# Make a call
def make_call(to_number, from_number, twiml_url):
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url=twiml_url  # URL pointing to TwiML instructions for the call
    )
    return call.sid

# Example usage
if __name__ == "__main__":
    to_number = '+1234567890'  # The recipient's phone number
    from_number = '+0987654321'  # Your Twilio phone number

    # Send an SMS
    sms_sid = send_sms(to_number, from_number, "Hello, this is a test message!")
    print(f"SMS sent with SID: {sms_sid}")

    # Make a call
    twiml_url = 'http://demo.twilio.com/docs/voice.xml'  # Example TwiML URL
    call_sid = make_call(to_number, from_number, twiml_url)
    print(f"Call initiated with SID: {call_sid}")
