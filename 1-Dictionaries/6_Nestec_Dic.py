
myfamily = {
    "child1" : {
        "name" : "Salman",
        "year" : "2004"
    },

    "child2" : {
        "name" : "Sharukh",
        "year" : "2007"
    },

    "child3" : {
        "name" : "Juhi",
        "year" : "2010"
    },
}
print(myfamily)
print(' ')

# Another way of 
child1 = {
    "name" : "Salman",
    "year" : "2004"
}
child2 = {
    "name" : "Sharukh",
    "year" : "2007"
}
child3 = {
    "name" : "Juhi",
    "year" : "2010"
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
