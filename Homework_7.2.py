# Модифікувати рядок

def correct_sentence(text):
    text = text[0].upper() + text[1:] # не используем capitalize потому что может сломать предложение по типу *My name is Alex*
    #text = text.capitalize()
    if not text.endswith("."):
        text += "."
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'

print('ОК')
