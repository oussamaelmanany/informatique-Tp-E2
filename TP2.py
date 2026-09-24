import copy
#EXERCICE 01 : 
a = ['A']
b = a
b[0] =1 
print(a,b)
#EXERCICE 02 :
classDict = { "class" : {
               "student" : {
                   "name" : "Mike",
                     "marks" : {
                          "physics" : 70,
                          "history" : 80
                     }
                }
            }
        }
# 1 : 
print(classDict["class"]["student"]["name"])
# 2 :
classDict["class"]["student"]["marks"]["physics"] = 89
print(classDict)
# 3 :
marks = sum(classDict["class"]["student"]["marks"].values())
taille =len(classDict["class"]["student"]["marks"].items())
classDict["class"]["student"]["average"] = marks/taille
print(classDict)
# 4 :
mike = classDict["class"]["student"]
classDict["class"]["student"]= [mike]
print(classDict)
# 5 :
ted = "name" : "ted",
                     "marks" : {
                          "physics" : 34,
                          "history" : 99
                                            }
classDict["class"]["student"].append(ted)
print(classDict)
#7 :
classDict["class"]["student"]["marks"]["average"] = len(sum(classDict["class"]["student"]["marks"])/len(classDict["class"]["student"]["marks"]))
#8 :
print(classDict)

#EXERCICE 03 :
import random
n = random.randint(3, 99)
tab = [random.randint(0, 500) for _ in range(n)]
print(tab)
def arediff(tab):
    liste_vue = []
    for num in tab:
        if num in liste_vue:
            return False 
        else:
            liste_vue.append(num)
     return True
print("Tous différents ?", arediff(tab))
#EXERCICE 04:
p = ["10", "2", "C", "D", "+"]
def calculScore(operations):
    pile = []
    for op in operations:
        if op == "C":
            pile.pop()
        elif op == "D":
            pile.append(pile[-1] * 2)
        elif op == "+":
            pile.append(pile[-1] + pile[-2]) 
        else:
            pile.append(int(op))
    return sum(pile)

print(calculScore(p))

#EXERCICE 05 : 
# 1 :
import collections
def ajtcoeff(polynome, coef):
    poly = collections.deque(polynome)
    if len(poly) >= 3 :
        print("polynome invalide")
     else :
        poly.append(coef)
     return poly
# 2 :
def saisiepoly():
    coef = -1
    n=0
    polynome = collections.deque(coef)
    while n < 3:
        coef = int(input("saisir le coef"))
        polynome.append(coef)
        n +=1
     return polynome


        