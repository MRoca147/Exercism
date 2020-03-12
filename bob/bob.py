def response(hey_bob):
    sentence = " ".join(hey_bob.split())
    if sentence.endswith("?") and sentence.isupper():
        return "Calm down, I know what I'm doing!"
    elif sentence.isupper():
        return "Whoa, chill out!"
    elif sentence.endswith("?"):
        return "Sure."
    elif sentence.isspace() or sentence == "":
        return "Fine. Be that way!"
    else:
        return "Whatever."
