# Name: Susie Odneal
# COSC1336, Lab 2, part 3: Stock Transaction Program
#
# Compute gain (or loss) on security transaction
#
# Note: Format dollar amounts to appear like: $1,234.56

print ("This program computes the result of a stock transaction.")

#Get how many shares were purchased and price per share plus Commission
shares = int(input('How many shares were purchased?'))
originalPricePerShare = float(input('How much did each share cost?'))
originalCommission = float(input('What percent commission did your stock broker\
take for this transaction?'))

#Get how many shares were sold and price per share plus Commission
sharesSold = int(input('How many shares were sold?'))
newPricePerShare = float(input('How much were the stocks sold for?'))
newCommission = float(input('How much commission did your stock broker take\
for this transaction? \n'))

#convert commissions from percent to decimal
originalCommissionDecimal = originalCommission * 0.01
newCommissionDecimal = newCommission * 0.01

#Calculate total paid prices
pricePaid = shares * originalPricePerShare
priceSold = sharesSold * newPricePerShare

#Calculate commissions
originalCommissionPaid = pricePaid * originalCommissionDecimal
newCommissionPaid = priceSold * newCommissionDecimal

#Output first transaction information
print('You bought your stocks for $'+ format(pricePaid, ',.2f'))
print('You paid your broker $'+ format(originalCommissionPaid, ',.2f')+ ' for the first transaction. \n')


#output second transaction information
print('You sold your stocks for $'+ format(priceSold, ',.2f'))
print('You paid your broker $'+ format(newCommissionPaid, ',.2f') +' for the second transaction. \n')

#Calculate how much money is left over
totalCommission = originalCommissionPaid + newCommissionPaid
leftOver = (- pricePaid - totalCommission) + priceSold

#output amount of money left after selling stock and paying broker.
print('You had $' + format(leftOver, ',.2f')+ ' left over after selling your stock. \n')

#flavor!
if leftOver > 0:
    print('Congratulations on your profit!')
else:
    print('Sorry about your loss. Better luck next time.')

#print ("Thank you. Spend wisely.")

# Paste your output below:
# This program computes the result of a stock transaction.
# How many shares were purchased?1000
# How much did each share cost?32.87
# What percent commission did your stock brokertake for this transaction?2
# How many shares were sold?1000
# How much were the stocks sold for?33.92
# How much commission did your stock broker takefor this transaction?
# 2
# You bought your stocks for $32,870.00
# You paid your broker $657.40 for the first transaction.
#
# You sold your stocks for $33,920.00
# You paid your broker $678.40 for the second transaction.
#
# You had $-285.80 left over after selling your stock.
#
# Sorry about your loss. Better luck next time.