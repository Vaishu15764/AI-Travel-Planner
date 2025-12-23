import resend
import os
from dotenv import load_dotenv

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY", "")

def send_email(to, subject, html):
    params = {
        "from": "AI Travel Planner <onboarding@resend.dev>",
        "to": ['vp4@gmail.com'],
        "subject": subject,
        "html": html
    }
    return resend.Emails.send(params)

