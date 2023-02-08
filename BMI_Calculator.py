#BMI Calculator

Wt = float(input())       #Weight in kilograms
Ht = float(input())       #Height in meters
BMI = float(Wt/(Ht*Ht))
if BMI < float(18.5):       #Condition if BMI is underweight
    print("Your Body Mass Index is: " + str(BMI))
    print("You are UNDERWEIGHT - consider increasing daily caloric intake.")
elif BMI <= float(25):      #Condition if BMI is normal
    print("Your Body Mass Index is: " + str(BMI))
    print("You have a NORMAL BMI.")
elif BMI <= float(30):      #Condition statement if BMI is overweight
    print("Your Body Mass Index is: " + str(BMI))
    print("You are OVERWEIGHT - either you have a larger than normal muscle mass or you should consider a change in diet along with increased daily activity.")
else:                       #Condition satement if BMI is obese
    print("Your Body Mass Index is: " + str(BMI))
    print("You are OBESE - either you are an elite bodybuilder or you need to see your PCP to initiate a personal weight loss plan. Obesity increases the risk of cardiovascular disease which is the leading cause of death in the US.")