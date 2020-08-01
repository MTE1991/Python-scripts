from numpy import array

print("--: Gender Game 1.0 :--")

score = []

no_traits = array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60])

traits = array(["self-reliant","yielding","helpful","defends own beliefs","cheerful","moody","independent",
"shy","conscientious","athletic","affectionate","theatrical","assertive","easily flattered","happy",
"strong personality","loyal","unpredictable","forceful","feminine","reliable","analytical","sympathetic",
"jealous","leadership ability","sensitive to others","truthful","willing to take risks","understanding",
"secretive","decisive","compassionate","sincere","self-sufficient","eager to soothe hurt feelings",
"conceited","dominant","soft-spoken","likable","masculine","warm","solemn","willing to take a stand",
"tender","friendly","aggresive","gullible","inefficient","childlike","act as a leader","adaptative",
"individualistic","do not use harsh language","unsystematic","competitive","love children","tactful",
"ambitious","gentle","conventional"])

for i in range(0,50):
    print(no_traits[i],traits[i])
    rating = int(input(">> "))

    if rating < 1 or rating > 7:
        raise ValueError("Please enter a number between 1 to 7.")

    score.append(rating)

score_np = array(score)

m_rating = (score_np[0]+score_np[3]+score_np[6]+score_np[9]+score_np[12]+score_np[15]+score_np[18]+
score_np[21]+score_np[24]+score_np[27]+score_np[30]+score_np[33]+score_np[36]+score_np[39]+score_np[42]+
score_np[45])

# still wip...
