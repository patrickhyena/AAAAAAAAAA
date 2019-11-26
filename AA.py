#number two

def translation(text:str):
    vowels:list = ["a","e","i","o","u"," "]
    final_text:str = ""
    for char in text:
        if not vowels.__contains__(char):
            final_text+=char+"o"+char
        else:
            final_text+=char
    return final_text

print(translation("this is fun"))