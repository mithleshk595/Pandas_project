import pandas
mydataset = {
    "cars": ["BMW", "Volve", "Ford"],
    "passing": [3 ,7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)