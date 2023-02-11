quantity = int(input("Enter the quantity of item sold:\t"))
cost_per_item = int(input("Enter the value of item:\t"))
discount_percentage = int(input("Enter the discount percentage:\t"))
tax = int(input("Enter the TAX:\t"))

total_cost = quantity * cost_per_item
discount_amount = total_cost * (discount_percentage/100)
price_after_discount = total_cost - discount_amount
tax_amount = price_after_discount * (tax/100)

print("*****************BILL*****************")
print("Quantity Sold:\t\t",quantity)
print("Price per item:\t\t{:.1f}".format(cost_per_item))
print("\t\t\t............")
print("Amount:\t\t\t{:.1f}".format(total_cost))
print("Discount:\t\t-{:.1f}".format(discount_amount))
print("\t\t\t............")
print("Discounted Total:\t{:.1f}".format(price_after_discount))
print("TAX:\t\t\t+{:.1f}".format(tax_amount))
print("\t\t\t............")
print("Total amount to be paid {:.1f}".format(price_after_discount-tax_amount))