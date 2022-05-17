import sys
file = open("scores_random.txt",'r')
all_scores = file.readlines()
nombe_scores = 0
score_total = 0
for line in all_scores:
    if (line[:9] == "Fireworks") :
        # print(line[10:])
        nombe_scores +=1
        score = line[11:]
        score_total += int(score[1]) + int(score[4]) + int(score[7]) + int(score[10]) + int(score[13])
        # print(score_total)
print("le nombre de parties est {}".format(nombe_scores))
print("the average is {}".format(score_total/nombe_scores))

