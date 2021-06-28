text = input()
word = input()


def search(a, b):
    if b in a:
        result = "Word found"
        return result
    else:
        result = "Word not found"
        return result


print(search(text, word))
