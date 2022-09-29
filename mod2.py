import mod3
import mod4

def text_analyze(text):
    if text.isdigit():
        return mod4.write_number(text)
    else:
        return mod3.write_text(text)
