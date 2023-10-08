from language import English, Hindi

english = English()
hindi = Hindi()

def Translate(order):
    if order.get('from_lang') == "English":
        text = order.get('text')
        language = order.get('to_lang')
        return english.TranslateTo(text, language)
    elif order == "Hindi":
        return hindi.TranslateTo(order.get('text'), order.get('to_lang'))
    else:
        return None