import smtplib
from email.message import EmailMessage
from datetime import datetime
import os
import base64
import traceback

from PIL import ImageGrab

def send_error_screenshot(to_adress:str | list[str], exception:Exception):
    # Create message
    msg = EmailMessage()
    msg['to'] = to_adress
    msg['from'] = 'robot@friend.dk'
    msg['subject'] = f"Error screenshot {datetime.now()}"

    # Take screenshot
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')

    # Encode the screenshot as base64
    with open("screenshot.png", "rb") as img_file:
        screenshot_data = img_file.read()
        screenshot_base64 = base64.b64encode(screenshot_data).decode('utf-8')

    # Create an HTML message with the embedded image
    html_message = f"""
    <html>
    <body>
    <p>Error type: {type(exception).__name__}</p>
    <p>Error message: {exception}</p>
    <p>{traceback.format_exc()}</p>
    <img src="data:image/png;base64,{screenshot_base64}" alt="Screenshot">
    </body>
    </html>
    """

    msg.set_content("Please enable HTML to view this message.")
    msg.add_alternative(html_message, subtype='html')
    
    # Delete screenshot
    os.remove('screenshot.png')

    # Send message
    with smtplib.SMTP("smtp.aarhuskommune.local", 25) as smtp:
        smtp.starttls()
        smtp.send_message(msg)


if __name__ == '__main__':
    try:
        raise ValueError("Du har lavet en fejl")
    except Exception as e:
        send_error_screenshot("ghbm@aarhus.dk", e)