# Note to self
# - assigning type float and int
# + calculations have to be done in the try loop, as a line of algbra eqn #
# + Exceptiom as e means except can be assigned to e
# + Format document by using cltr + shift + T #
total = 0.0
count = 0
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    else:
        try:
            number = float(number)
            total = total+number
            count = count+1
        except Exception as e:
            # print(e)
            print("Invalid number")
    # print(total)

print("ALL DONE")
print(total, count, total/count)
