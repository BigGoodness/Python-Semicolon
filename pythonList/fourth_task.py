def list_with_words():
    words = ["lamb", "kit", "yam", "king", "dogs", "man"]

    for letters in words:
        if len(letters) > 3:
            print([letters])

list_with_words()
