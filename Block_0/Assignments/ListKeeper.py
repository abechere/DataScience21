class ListKeeper:
    """ ListKeeper stores named lists """
    
    def __init__(self, key='example', value=[1,2,3,4,5]):
        """ initialization with a list named example """ 
        self.dict = {}
        self.dict[key] = value
        
    def show(self):
        """ returns all list names """
        return list(self.dict.keys())
        
    def add(self, name, list):
        """ adds the given list with the given name """
        self.dict[name] = list
        
    def delete(self, name):
        """ removes the list referenced by the passed name """
        self.dict.pop(name)
           
    def sort(self, name):
        """ returns the sorted list referenced by the passed name """
        self.dict[name].sort()
        return self.dict[name]
    
    def append(self, name, list):
        """ appends the passed list to the existing list, which is referenced by name """
        self.dict[name].extend(list)
 
        