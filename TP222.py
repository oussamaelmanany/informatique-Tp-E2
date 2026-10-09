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
classDict["class"]["student"] = [ted]
print(classDict)