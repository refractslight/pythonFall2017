# Name:
# COSC1336, Lab 5a, part 2: Use a tip function to create a tip table

# First, modify the display total due function so that when it is called with the values
# 10.82, 0.15, and 0.0825, it displays the result formatted just like this:
# Total due with 15% tip: $12.32
# You may have to fix a "bug" in the display_total_due function.
# Hint: Look at the sections in Chapter 2 on the end and sep arguments to print (pp. 65-67) on
# formatting numbers (pp. 68-69) and on formatting numbers as a percentage (p. 72)
#
# Second, complete the program so that it reads in the bill for a meal, and then displays
# the total due with a tip rate of 10%, 15%, 20%, and 25%, using the display total due function.
# Since the tax rate should be the same for all of the function calls, you should declare a constant
# variable called TAX RATE to hold the tax rate of 8.25%. Here is a sample interaction with the
# program:
# Enter the bill with tax: $16.24
# Total due with 10% tip: $17.74
# Total due with 15% tip: $18.49
# Total due with 20% tip: $19.24
# Total due with 25% tip: $19.99

# Your program should read in the amount due for a meal (with tax),
# and then use the provided function to display the total due with
# a tip rate of 10%, 15%, 20% and 25%.  The tax rate should be the
# same in each case (8.25%), so it should be stored in a constant
# called TAX_RATE.

# display_total_due function
#   inputs: the original bill (with tax), the tip rate, and the tax rate
#   output: displays the total due, with tip and tax
#   processing: calculates the total due by computing the tip
#               based on the pre-tax amount and then adding both
#               the tip and the tax to the original bill
def display_total_due(bill_with_tax, tip_rate, tax_rate):
    bill_without_tax = bill_with_tax / (1 + tax_rate)
    tip = bill_without_tax * tip_rate
    total_due = bill_with_tax + tip
    print("Total due with ", tax_rate, "% tip: ", total_due)


# Add a main function here
# Your main function will ask the user for total bill amount, including tax.
# Your main function will then call the display_total_due function 4 times.

def main():
    billWithTax = float(input("How much what the total bill with tax?\n"))
    taxRate = float(input("What is the tax rate?"))
    tipRate = float(input("What is the tip rate?"))
    display_total_due(billWithTax, taxRate, tipRate)
    # display_total_due()
    # display_total_due()
    # display_total_due()

# Call the main function here.
main()

# Paste your output below:
