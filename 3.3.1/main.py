# Water Tracker

# goal for each day

Goal = 80

# list of days
week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
water_intake = [0, 0, 0, 0, 0, 0, 0]

# Function to add water intake
def add_water(day,amount):
    global water_intake
    water_intake[day] += int(amount)


# Function to check if goal is met
def check_goal(day):
    global water_intake, Goal
    if water_intake[day] >= Goal:
        print ("goal for" + week[day] + "is complete!")
    else:
        print ("at your Goal for" + week[day] +"yet.")


# function to check water intake
def check_intake():
    global water_intake
    return water_intake

# for day in days
for day in range(7):
    print("For" + week[day])
    water_intake = int(input("how many ounces of water did you drink today?"))
    add_water(day, water_intake)
    check_goal(day)
