#Some time paying equally makes sense rather than going Dutch, 
#especially if you eat more than other people on the table :) 
#I got you covered in case you don't have a pencil and paper.

bill = input("Bill Total: $")
tip = input("Tip percentage: %")
people = input("How many people ate? ")

tip_amount = float(bill) * (int(tip) / 100)
bill_share = round((float(bill) + int(tip_amount)) / int(people))

print(f"Each person shuold pay ${bill_share}")
