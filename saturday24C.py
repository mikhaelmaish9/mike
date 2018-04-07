#conditional statement
weight = 90
height = 1.88
bmi = weight /(height*height)
print("your Bmi is ",bmi)
if bmi < 15:
    print("you are very severely underweight ")
elif bmi >=15 and bmi <16:
    print("you are severely underweight ")
elif bmi>=16 and bmi <18.5:
  print(" you are underweight")
elif bmi>=18.5 and bmi <25:
    print("you are normal")
elif bmi>25 and bmi<30:
    print ("you are overweight")
elif bmi>30 and bmi <35:
    print ("you are obese class")
elif bmi>35 and bmi<40:
    print("you are obese class2")
elif bmi>40:
    print("print you are obese class3")