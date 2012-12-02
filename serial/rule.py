class Rule:
  # guard symbol to mark beginning and end of rule.
  theGuard = guard()
  # counter for number of times rule is used
  count = 0
  # total number of rules, this should always be static
  numRules = 0
  
  # rule number
  number = None
  # index used for printing
  index = None

  def __init__(self):
    self.number = Rule.numRules
    Rule.numRules += 1
    theGuard = guard(self)
    self.count = 0
    index = 0

  def first(self):
    return theGuard.n

  def last(self):
    return theGuard.p

  def getRules(self):
    rules = []
    currentRule, referedToRule = None, None
    sym = None
    index = 0
    processedRules = 0
    text = ""
    charCounter = 0

    text = text + "Usage\tRule\n"
    rules.append(self)
    while (processedRules < Rule.numRules):
      currentRule = (rule)rules[processedRules]
      text = text + " " + currentRule.count + "\tR" + processedRules + " -> "
      sym = currentRule.first()
      # modified original for loop; need to do rule tracing with while loop
      while((sym is not None) or (not sym.isGuard())):
        if(sym.isNonTerminal()):
          referedToRule = ((nonTerminal)sym).r
          if ((Rule.numRules > referedToRule.index) and ((rule)rules[referedToRule.index] == referedToRule)):
            index = referedToRule.index
          else:
            index = Rule.numRules
            referedToRule.index = index
            rules.append(referedToRule)
          text = text + "R" + index
        else:
          if(sym.value == " "):
            text = text + "_"
          else:
            if sym.value == "\n":
              text = text + "\\n"
            else:
              text = text + sym.value
        text = text + " "
        sym = sym.n
      text = text + "\n"
      processedRules += 1
    return text