'''
SecretSanta.py
Author: Andrew Gaylord

randomly generates list of secret santa targets while accounting for avoid list
'''
import random

class person:
    def __init__(self, name, avoids = None, got = None):
        self.name = name
        self.avoids = avoids
        self.got = got
    
    def check(self):
        # return true if person is finalized
        # check if they have someone
        if self.got == None:
            return False
        # check if they got someone they ought to avoid
        if self.avoids:
            for x in self.avoids:
                if x == self.got:
                    return False
        # check if they got themself
        if self.got == self.name:
            return False
        return True
    
    def checkOptions(self, options):
        # check all options left and see if person has any valid picks left
        for x in options:
            if self.avoids:
                if not x in self.avoids and x != self.name:
                    return True
            elif x != self.name:
                return True

        return False
    
    def reset(self):
        self.got = None


if __name__ == "main":

  # example people array
  # people = [person("sibling1", ["siblingTheyGotLastYear"]), person("sibling2", ["siblingTheyGotLastYear"]), ...]
  people = []
  
  flag = True
  while flag:
      flag = False
      print("RESET")
      options = [x.name for x in people]
      [x.reset() for x in people]
  
      for i in range(10):
  
          # if options left are invalid: reset whole thing
          if not people[i].checkOptions(options):
              flag = True
          else:
              # otherwise, randomly select from options until valid name is found
              selected = None
              while not people[i].check():
                  selected = random.choice(options)
                  people[i].got = selected
              # remove selected name from options
              options.pop(options.index(selected))
  
  for per in people:
      print("{} got {}".format(per.name, per.got))
