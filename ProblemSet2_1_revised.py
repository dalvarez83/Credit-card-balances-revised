echo "# Credit-card-balances" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/dalvarez83/Credit-card-balances.git
git push -u origin master

# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.
# balance - the outstanding balance on the credit card
#annualInterestRate - annual interest rate as a decimal
#monthlyPaymentRate - minimum monthly payment rate as a decimal

balance = 4213
annualInterestRate = 0.2 
monthlyPaymentRate = 0.04
numMonths =0

monthlyInterestRate = annualInterestRate / 12.0
minimumMonthlyPayment = balance * monthlyPaymentRate
updatedBalanceEachMonth = balance + (monthlyInterestRate * balance)
monthlyUnpaidBalance = balance - minimumMonthlyPayment
totalPaid = 0
#monthly Interest Rate = annual Interest Rate / minumum Monthly Payment Rate
#minimum Monthly Payment = minimum Monthly Payment Rate x previous Balance
#monthly Unpaid Balance = previous Balance - minimum Monthly Payment
#updated Balance Each Month = monthly unpaid balance + (monthly interest rate x monthly unpaid balance)
 
for i in range(1,13):
   numMonths +=1   
   updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
   monthlyUnpaidBalance = updatedBalanceEachMonth - minimumMonthlyPayment
   minimumMonthlyPayment = monthlyUnpaidBalance * monthlyPaymentRate
   totalPaid += minimumMonthlyPayment
   print('Month:' + str(numMonths))
   print('Minumum monthly payment: ' + str(round(minimumMonthlyPayment,2)))
   print('Remaining balance: ' + str(round(updatedBalanceEachMonth,2)))
print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(updatedBalanceEachMonth,2)))
