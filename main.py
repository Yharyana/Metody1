"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self,itemek):
        self.items.append(itemek)

    def getClassiness(self):
        classys=0
        for item in self.items:
            if item=="tophat":
                classys+=2
            elif item=="bowtie":
                classys+=4
            elif item=="monocle":
                classys+=5
            else:
                classys+=0
        return classys


# Test cases
me = Classy()

# Should be 0
print
me.getClassiness()

me.addItem("tophat")
# Should be 2
print (me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print (me.getClassiness())

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())

# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

class robot:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(self.name)
class person:
    def __init__(self,robot):
        self.robot=robot
r1=robot("Grześ")
p1=person(r1)
r1.introduce()
p1.robot.introduce()

