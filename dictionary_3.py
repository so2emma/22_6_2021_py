favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n\n")
for name, language in favorite_languages.items():
    print(name.title() + ' you love ' + language.title())

taken = ['phil', 'sarah', 'edward']
for name in favorite_languages.keys():
    print(name.title())
    if name in taken:
        print("Congratulations " + name.title() + "you hav taken the course")
    else:
        print(name.title() + " You need to take programming seriously")
