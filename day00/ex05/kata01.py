languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

str = ["Python", "Ruby", "PHP"]

for item in str:
    print(item + " was created by " + languages[item])
