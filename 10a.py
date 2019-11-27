import string

check_pangram = lambda text : sorted(set(text.lower().replace(" ",""))) == sorted(set(string.ascii_lowercase))

print(check_pangram("The quick brown fox jumps over the lazy dog"))