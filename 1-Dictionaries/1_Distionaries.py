thisdist = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}
print(thisdist)

x = thisdist["model"]
print(x)
# Same as uper
x = thisdist.get("model")
print(x)

#change values
thisdist["year"] = 2020
print(thisdist)

# Dic length
print(len(thisdist))
