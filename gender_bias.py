# Ideas are taken from the book "Brain Games" by Richard B. Fisher.
# Created by MT Ekleel

while True:
    print("\t\t--: Gender bias: Masculine? Feminine? or Androgynous? ver 1.02 :--\n")
    print("""
    Made by:
    MT Ekleel
    E-mail: mtahsinekleel02@gmail.com
    Facebook: MT Ekleel
    GitHub: MTE1991
    """)
    print("""
    There will be sixty traits below that will judge how androgynous you are. Which means
    how much gender bias your personality has.\n
    Indicate on a scale of 1 to 7 how well each traits describe you. A 1 means it's never true
    for you, a 7 means it's always true.\n
    """)

    a_1 = str(input("Press any key to proceed..."))
    score = []
    traits = ["self-reliant","yielding","helpful","defends own beliefs","cheerful","moody","independent",
    "shy","conscientious","athletic","affectionate","theatrical","assertive","easily flattered","happy",
    "strong personality","loyal","unpredictable","forceful","feminine","reliable","analytical","sympathetic",
    "jealous","leadership ability","sensitive to others","truthful","willing to take risks","understanding",
    "secretive","decisive","compassionate","sincere","self-sufficient","eager to soothe hurt feelings",
    "conceited","dominant","soft-spoken","likable","masculine","warm","solemn","willing to take a stand",
    "tender","friendly","aggresive","gullible","inefficient","childlike","act as a leader","adaptative",
    "individualistic","do not use harsh language","unsystematic","competitive","love children","tactful",
    "ambitious","gentle","conventional"]
    i = 0

    while i <= 59:
        try:
            print(i+1,".",traits[i])
            i += 1
            rating = int(input(">> "))
            
            # this condition below is used to only check whether the input is between 1 and 7 or not
            if rating < 1 or rating > 7:
                print("You are supposed to enter an integer between 1 and 7")
                i -= 1
                continue

        #this exception bellow is used to only check whether the input is integer or not
        except:
            print("You are supposed to enter an integer between 1 and 7")
            i -= 1
            continue
            
        score.append(rating)

    # Masculinity score:
    m_score = (score[0]+score[3]+score[6]+score[9]+score[12]+score[15]+score[18]+
    score[21]+score[24]+score[27]+score[30]+score[33]+score[36]+score[39]+score[42]+
    score[45]+score[49]+score[51]+score[54]+score[59])

    # Feminity score:
    f_score = (score[1]+score[4]+score[7]+score[10]+score[13]+score[16]+score[19]+score[22]+
    score[25]+score[28]+score[31]+score[34]+score[37]+score[40]+score[43]+score[46]+score[48]+
    score[52]+score[55]+score[58])

    # Evaluation:
    # This is derived from some complex statistical procedure, which I am not aware of...
    result = (f_score - m_score) * 2.322

    if result == 0:
        print("""Result:
        You're androgynous.\n""")
    elif result > 0 and result <= 1:
        print("""Result:
        You're near feminine.\n""")
    elif result >= 2.025:
        print("""Result:
        You're feminine.\n""")
    elif result < 0 and result >= -1:
        print("""Result:
        You're near masculine.\n""")
    elif result < -1 and result <= -2.025:
        print("""Result:
        You're masculine.\n""")

    # Log file:
    with open('log.txt', 'w') as logf:
        logf.write("----Start----\n")
        logf.write("--Scores--\n")
        for i in score:
            logf.write('%s\n' % i)
        logf.write("--Scores--\n")
        logf.write("--Result--\n")
        logf.write("Result = {result:.2f}\n".format(result=result))
        logf.write("--Result--\n")
        logf.write("----Stop----\n\n")

    print("""
    Note:
    Results may be subject to doubt, even though it's a psycological game.
    It's because many of the qualities are subject to stereotypic bias. So the results
    may not be fully accurate.
    If you want to understand how the game works, please check the source code or
    contact with the developer.
    """)
    a_2 = str(input("Do you want to play again? (Y/N) >> "))

    if a_2 == "Y" or a_2 == "y":
        continue
    else:
        print("Thank you for participating in this game.")
        break
