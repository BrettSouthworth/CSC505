
print("Welcome to Bretts Restaurant Calculator. This calculator will calculate an 18% tip and 7% sales tax.")
print("To begin, Please enter the charge for the food: ")
OriginalValue = float(input())
AdditionalCharges = [OriginalValue * 0.18, OriginalValue * 0.07]
print("~~~~~")
print("Tip: {:0.2f}".format(AdditionalCharges[0]))
print("Sales Tax: {:0.2f}".format(AdditionalCharges[1]))
print("Total cost: {:0.2f}".format(OriginalValue + sum(AdditionalCharges)))
print("~~~~~")
print("Press enter to close...") 
input()