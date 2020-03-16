import pandas as pd
super=list()#Used to prevent repetition of players

#Home ground : cities, teams and venues

info=pd.read_csv("matches.csv")
c=list()#city
t=list()#team
v=list()#venue
info=pd.DataFrame(info,columns=["city","team1","team2","venue"])
for i in range(1,636):
    if info["city"][i] not in c:
        if str(info["city"][i]) in str(info["team1"][i]):
            c.append(info["city"][i])
            v.append(info["venue"][i])
            t.append(info["team1"][i])
        elif str(info["city"][i]) in str(info["team2"][i]):
            c.append(info["city"][i])
            v.append(info["venue"][i])
            t.append(info["team2"][i])
            
#To find appropriate bowlers

info2=pd.read_csv("deliveries.csv")
info2=pd.DataFrame(info2,columns=["bowler","player_dismissed"])
bow=list()
wic=list()
k=list()
sum=0
bowlers=list()#Bowlers for individual teams 

for i in range(0,10000):
    if info2["bowler"][i] not in bow:
        bow.append(info2["bowler"][i])
        for j in range(i,10000):
            if str(info2["player_dismissed"][j]) !="nan":
                sum=sum+1
        wic.append(sum)#To find the wickets of each bowler
        sum=0
        
k=list(zip(bow,wic))
sk=sorted(k,key=lambda x:x[1])
for i in range(0,24,3):
    bowlers.append([ele[0] for ele in sk[58+i:i+3+58]])#Selecting average bowlers

#SUPER LIST
for ele in bowlers:
    for i in range(0,3):
        super.append(ele[i])

#To find the best batsmen

df=pd.read_csv('deliveries.csv')
df = pd.DataFrame(df, columns= ['batsman','batsman_runs'])
total_runs=list()
batsman_name=list()
q=list()
batters=list()#Batsmen for individual teams

for i in range(0,1000):
    if(df['batsman'][i] not in batsman_name):
        if(df['batsman'][i] not in super):
            max_runs=0
            batsman_name.append(df['batsman'][i])
            for j in range(0,1000):
                if(df['batsman'][i]==df['batsman'][j]):
                    max_runs=max_runs+df['batsman_runs'][j]#To find the total runs of each batsman
                total_runs.append(max_runs)

q=list(zip(batsman_name,total_runs))
sq=sorted(q,key=lambda x:x[1],reverse=True)
for i in range(0,40,5):
    batters.append([ele[0] for ele in sq[i:i+5]])#Selecting the best batsmen

#SUPER LIST
for ele in batters:
    for i in range(0,5):
        super.append(ele[i])

#To find wicket keepres

df=pd.read_csv('deliveries.csv')
df = pd.DataFrame(df, columns= ['fielder','dismissal_kind','batsman'])
wicket_keeper=list()
wicketkep=list()#Wicket keeper for individual team

for i in range(0,50000):
    if(df["fielder"][i] not in super and df["fielder"][i] not in wicket_keeper):
        if(df['dismissal_kind'][i]=='stumped'):
            wicket_keeper.append(df['fielder'][i])
wicketkep=[ele for ele in wicket_keeper[1:9]]#Selecting wicket keeper

#SUPER LIST
for ele in wicketkep:
    super.append(ele)

#To find all rounders
            
all_rounder=list()
all_round=list()#All rounders for individual teams
for i in range(0,10000):
    if(df['batsman'][i]not in super and df['batsman'][i] not in all_rounder):
        all_rounder.append(df['batsman'][i])    
for i in range(0,18,2):
    all_round.append([ele for ele in all_rounder[i:i+2]])#Selecting all rounders

#TO DISPLAY ALL THE 8 NEWLY GENERATED TEAMS

print("The newly  generated teams are:-")
print()
for i in range(0,8):
    print("Team: ",i+1)
    print("City: ",c[i]," | Team: ",t[i]," | Venue: ",v[i])
    print()
    print("Bowlers")
    print()
    for ele in bowlers[i]:
        print(ele)
    print()
    print("Batsmen")
    print()
    for ele in batters[i]:
        print(ele)
    print()
    print("Wicket keeper")
    print()
    print(wicketkep[i])
    print()
    print("Allrounder")
    print()
    for ele in all_round[i-1]:
         print(ele)
    print()
