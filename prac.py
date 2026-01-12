#   prices = ["45.50", "30", "25.75", "50"]
#   print(prices)

#   bill=[float(x) for x in prices]
#   print(bill)
#   addition=sum(bill)
#   print(f"Total bill:{addition:.2f}")

Horizon = {"45.50", "30", "25.75", "50"}
explicit_cast=set(map(float, Horizon))
print(explicit_cast)
total=sum(explicit_cast)
print(total)
print(f"Maximum :{total:.5f}")





