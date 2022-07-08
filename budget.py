class Category:

  def __init__(self, category):
    self.ledger = []
    self.category = category
    self.balance = 0
  
  def deposit (self, amount, description = ''):
    x = {"amount": amount, "description": description}
    self.ledger.append(x)

  def withdraw(self, amount, description = ''):
    x = {"amount": amount , "description": description}
    if ( x["amount"] > self.get_balance()):
      return False
    else:
      x = {"amount": amount * (-1), "description": description}
      self.ledger.append(x)
      return True

  def get_balance(self):
    self.balance = 0
    for i in range(0, len(self.ledger)):
      self.balance = self.balance + self.ledger[i]["amount"]
    return (self.balance)

  def transfer(self, amount, recepient): 
    x = {"amount": amount, "description": "Transfer to " + str(recepient.category)}
    if (self.withdraw(amount) == True):
      self.ledger.pop()  #remove element added through running function in if statemen
      self.withdraw(amount, x["description"])
      recepient.deposit(amount, "Transfer from " + str(self.category))
      return True
      
    else:
      self.ledger.pop()  #remove element added through running function in if statemen
      recepient.deposit(amount)
      return False

  def check_funds(self, amount):
    if (self.get_balance() < amount):
      return False
    else:
      return True

  def __repr__(self):
    output = self.category.center(30,'*') + '\n'
    for i in range(0, len(self.ledger)):
      output = output + str(self.ledger[i]['description'])[0:23] + ' ' + str(format(self.ledger[i]['amount'], ".2f")).rjust(29-len(self.ledger[i]['description'])) + '\n' 
    output = output.strip('\n')
    total = 0
    for i in range(0, len(self.ledger)):
      total = total + self.ledger[i]['amount']
    output = output + '\n' + 'Total: ' + str(total)
    return output
     
def create_spend_chart(categories):
  
  #Create touple that takes first element as category name and second element as withdrawals aproximated to nearest 10
  chart = []
  for i in range(0, len(categories)):
    withdrawal = 0
    for j in range(0, len(categories[i].ledger)):
      if ( (categories[i].ledger[j]['amount']) < 0 ):
        withdrawal = withdrawal + (categories[i].ledger[j]['amount'])
    withdrawal = round(withdrawal, 2) 
    x = {"name": categories[i].category, "withdrawal": withdrawal}
    chart.append(x)
  total = 0 
  
  for i in range (0, len(chart)):
    total = total + chart[i]['withdrawal']
  
  for i in range (0, len(chart)):
    chart[i]['percentage'] = (chart[i]['withdrawal']*100)/total

  graph = 'Percentage spent by category\n'
  for i in range (10,-1,-1):
    if (i<=9):
      graph = graph + ' '
    if (i == 0):
      graph = graph + ' '
    graph = graph + str(i*10) + '| '
    for j in range (0, len(chart)):
      if chart[j]['percentage'] >= (i*10):
        graph = graph + 'o  '
      else:
        graph = graph + '   '
        
    graph = graph + '\n'

  graph = graph + 4*' '+ 4*'-' + 3*(len(chart)-1)*'-' + '\n'
  
  longestCategory = 0
  for i in range (0, len(chart)):
    if len(chart[i]['name'])>longestCategory:
      longestCategory = len(chart[i]['name'])
  
  listOfCategories = []
  for i in range (0, len(chart)):
    if len(chart[i]['name'])<longestCategory:
      chart[i]['name'] = chart[i]['name'] + ' '*(longestCategory-len(chart[i]['name']))
    listOfCategories.append(chart[i]['name'])

  for j in range (0, longestCategory):
    graph = graph + '     '
    for i in range(0, len(listOfCategories)):
      graph = graph + listOfCategories[i][j] + '  '
    graph = graph + '\n'

  graph = graph.rstrip('\n')
  return (graph)