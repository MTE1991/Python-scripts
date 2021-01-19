# Ideas are taken from the book "Brain Games" by Richard B. Fisher.
# Created by MT Ekleel

from numpy import array

while True:

    print("\t\t--: Gender bias: Masculine? Feminine? or Androgynous? ver 1.01 :--\n")
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
    traits = array(["self-reliant","yielding","helpful","defends own beliefs","cheerful","moody","independent",
    "shy","conscientious","athletic","affectionate","theatrical","assertive","easily flattered","happy",
    "strong personality","loyal","unpredictable","forceful","feminine","reliable","analytical","sympathetic",
    "jealous","leadership ability","sensitive to others","truthful","willing to take risks","understanding",
    "secretive","decisive","compassionate","sincere","self-sufficient","eager to soothe hurt feelings",
    "conceited","dominant","soft-spoken","likable","masculine","warm","solemn","willing to take a stand",
    "tender","friendly","aggresive","gullible","inefficient","childlike","act as a leader","adaptative",
    "individualistic","do not use harsh language","unsystematic","competitive","love children","tactful",
    "ambitious","gentle","conventional"])
    i = 0

    while i <= 59:
        print(i+1,".",traits[i])
        i += 1
        rating = int(input(">> "))
        score.append(rating)
        if rating < 1 or rating > 7:
            raise ValueError("Please enter a number between 1 to 7.")

    score_np = array(score)

    # Masculinity score:
    m_score = (score_np[0]+score_np[3]+score_np[6]+score_np[9]+score_np[12]+score_np[15]+score_np[18]+
    score_np[21]+score_np[24]+score_np[27]+score_np[30]+score_np[33]+score_np[36]+score_np[39]+score_np[42]+
    score_np[45]+score_np[49]+score_np[51]+score_np[54]+score_np[59])

    # Feminity score:
    f_score = (score_np[1]+score_np[4]+score_np[7]+score_np[10]+score_np[13]+score_np[16]+score_np[19]+score_np[22]+
    score_np[25]+score_np[28]+score_np[31]+score_np[34]+score_np[37]+score_np[40]+score_np[43]+score_np[46]+score_np[48]+
    score_np[52]+score_np[55]+score_np[58])

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
        for i in score_np:
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

    if a_2 == "Y" or a_2 == "y": game_main()
    else:
        print("Thank you for participating in this game.")
        break
