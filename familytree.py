class Family:
    def __init__(self):   
        self.males = {}
        self.females = {}
        self.children = {}
        self.parents = {}
        
    def male(self,name):
        if name in self.males or name in self.females:
            return False
        if name in self.parents:
            child = self.parents.get(name)
            parents = self.children[child[0]]
            if name == parents[0]:
                self.gender = "Male"
                self.males.update({parents[0]:self.gender})
                self.gender = "Female"
                self.females.update({parents[1]:self.gender})
            else:
                self.gender = "Male"
                self.males.update({parents[1]:self.gender})
                self.gender = "Female"
                self.females.update({parents[0]:self.gender})
        self.name = name
        self.gender = "Male"
        self.males.update({self.name:self.gender})
        return True
    
    def female(self,name):
        if name in self.males or name in self.females:
            return False
        if name in self.parents:
            child = self.parents.get(name)
            parents = self.children[child[0]]
            if name == parents[0]:
                self.gender = "Female"
                self.females.update({parents[0]:self.gender})
                self.gender = "Male"
                self.males.update({parents[1]:self.gender})
            else:
                self.gender = "Female"
                self.females.update({parents[1]:self.gender})
                self.gender = "Male"
                self.males.update({parents[0]:self.gender})
        self.name = name
        self.gender = "Female"
        self.females.update({self.name:self.gender})
        return True
    
    def isMale(self,name):
        if name in self.males:
            return True
        else:
            return False
        
    def isFemale(self,name):
        if name in self.females:
            return True
        else:
            return False
        
    def setParent(self,child,parent):
        if child in self.parents.keys() and parent in self.children.keys(): # It is impossible to be the parent of your parent
            return False
        if child not in self.males or self.females:
            self.children.setdefault(child,[parent])
        if len(self.children[child]) == 2:                                  # It is impossible to have 3 parents
            return False
        if parent not in self.males or self.females:
            self.parents.setdefault(parent,[child])
        if parent in self.parents.keys() and child not in self.parents[parent]:
            self.parents[parent].append(child)
        if child in self.children.keys() and parent not in self.children[child]:
            self.children[child].append(parent)
        return True
        
    def getParents(self,name):
        if name in self.children:
            return sorted(self.children.get(name))
        
    def getChildren(self,name):
        if name in self.parents:
            return sorted(self.parents.get(name))
        
        
fam = Family()
fam.male("Yiannis")
fam.female("Marina")
fam.male("Marina")                    # Test duplicate
print(fam.males)
print(fam.females)
print(fam.isMale("Marina"))           # Test gender methods 
print(fam.isFemale("Marina"))         # Test gender methods
fam.setParent("Yiannis","Eleftheria")
fam.setParent("Yiannis","George")
fam.setParent("Marina","Eleftheria")
fam.setParent("Marina","George")
fam.setParent("Marina","Michael")     # Test child having 3 parents
fam.setParent("Eleftheria","Yiannis") # Test being child of your parent
print(fam.children)
print(fam.parents)
print(fam.getParents("Yiannis"))
print(fam.getChildren("George"))
fam.male("George")                    # Test deducing mother as female since dad is George
fam.male("Eleftheria")                # Test setting mother as male even though father is George
print(fam.males)
print(fam.females)
print(fam.getParents("Paul"))         # Test non-existing people
print(fam.getChildren("Maria"))       # Test non-existing people