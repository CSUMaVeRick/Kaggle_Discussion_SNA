with open('kaggle_comment_user.csv','r',encoding='utf-8') as kp:
    ka=kp.readlines()
with open('kaggle_competition_comment.csv','r',encoding='utf-8')as kp:
    text=kp.read()
for k in range(1,len(ka)):
    o,r=ka[k].split(',')[0],ka[k].split(',')[1].rstrip('\n')
    text=text.replace(o,r)
with open('kaggle_edge.txt','w',encoding='utf-8') as kp:
    kp.write(text)