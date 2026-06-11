from datetime import datetime

def run_command(text):
    text = text.lower()

    if "time" in text:
        return f"Current time: {datetime.now().strftime('%H:%M:%S')}"

    if "date" in text:
        return f"Today's date: {datetime.now().strftime('%d-%m-%Y')}"

    return None