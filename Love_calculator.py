
def calculate_love_score(name1,name2):
    print(f"First name: {name1}")
    print(f"Second name: {name2}")
    word1 = "TRUE"
    word1 = list(word1)
    word2 = "LOVE"
    word2 = list(word2)
    score1 = 0
    score2 = 0

    for char in name1:
        if char.upper() in word1:
            score1 += 1
        else:
            pass
    for char in name2:
        if char.upper() in word1:
            score1 += 1
        else:
            pass
    print(f'The "TRUE" word score: {score1}')
    for char in name1:
        if char.upper() in word2:
            score2 += 1
        else:
            pass
    for char in name2:
        if char.upper() in word2:
            score2 += 1
        else:
            pass
    print(f'The "LOVE" word score: {score2}')
    return print(f"Your total love score: {str(score1) + str(score2)}")
calculate_love_score("Romeo","Juliet")


