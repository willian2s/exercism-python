def response(hey_bob):
    if hey_bob.strip().endswith("?"):
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    else:
        return "Whatever."

