myDict={
    "Fast": "I am quick",
    "Adesh": "Learner",
    "Marks": [1,2,3,4,5],
    "anotherdict": {'Adesh':'Player'}
}
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)

updateDict = {
    "Lavish":"Friend",
    "Diya":"Friend",
    "Shubham":"Friend",
    "Adesh":"Dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Adesh"))
print(myDict["Adesh"])

print(myDict.get("Adesh2"))
print(myDict["Adesh2"])