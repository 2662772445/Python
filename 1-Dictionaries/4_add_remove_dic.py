thisdist = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : '1964'
}

# Add
thisdist["color"] = "Red"
print(thisdist)

# Remove
thisdist.pop("model")
print(thisdist)

thisdist.popitem()
print(thisdist)

# Delete
del thisdist["brand"]
print(thisdist)
"""
del thisdist
print(thisdist)
"""
thisdist.clear()
print(thisdist)
