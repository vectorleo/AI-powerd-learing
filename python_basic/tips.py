# this calculate the bill and tip precentages 

def tip_cal():
  bill = int(input('enter the bill: '))
  tip_percentage = int(input('enter the tip percentage: '))

  tip = (bill * tip_percentage) / 100
  total_bill = tip + bill 

  return total_bill


split = int(input('How many people would you like to split the bill: '))

if split == split:
  print(f'{tip_cal() / split} per person')