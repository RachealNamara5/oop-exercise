#object oriented programing is a style characterised by the identificationb of classes of objects closely linked with the functions.
# an object is an entity that has attributes and behaviours.eg person ,has attributesof name,age and behaviour -dancing eating
class parrot:
    # class attributes 
    name=""
    age = 0
    location= ""
     # create parrot A object
parrotA=parrot()
parrotA.name = "woo"
parrotA.age =10
parrotA.location="Amazon"
# create another object parrot B
parrotB = parrot()
parrotB.name="kasuku"
parrotB.age=15
parrotB.location="Kidepo valley"
#asses attributes
print(f"{parrotA.name} is {parrotA.age} years old and lives in {parrotA.location}")
print (f"{parrotB.name} is {parrotB.age} years old and lives in {parrotB.location}")
# in the above example i created a class with the name parrot with attributes :name and age
#Then we create instances of the parrot class .hee parrotA and parrotB are the objects
#we use  the objects name and the  dot(.)notation to asses
