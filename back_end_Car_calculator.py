import pandas as pd

car_type = ""
while True:
    main_answer = input("Do you want to buy a new car(yes/no)? ")
    if main_answer == "no":
        continue
    elif main_answer == "yes":
        income = float(input("What is your yearly gross income: "))
        value_of_car = income / 10
        print("The value of your car/cars must be: ", value_of_car)
        another_car = input("Do you have another car/cars(yes/no)? ")
        if another_car == "no":
            work_status = input("Are you worker/executive/businessman(women)")
            if work_status == "worker":
                family_status = input("What is your family status(single/married/parent/grandparent)? ")
                if family_status == "single" or family_status == "married":
                    car_type = "Subcompact crossover SUV (B-segment)"
                elif family_status == "parent":
                    car_type = "Compact crossover SUV (C-segment)"
                elif family_status == "grandparent":
                    car_type = "Mid-size crossover SUV (D/E-segment)"
                else:
                    print("Please enter a valid answer: (single/married/parent/grandparent) ")
                    continue
            elif work_status == "executive":
                car_type = "Mid-size crossover SUV (D/E-segment)"
            elif work_status == "businessman":
                car_type = "Full-size crossover SUV"
            else:
                print("Please enter a valid answer: (yes) or (no) ")
                continue
        elif another_car == "yes":
            value_of_owned_car = float(input("What is the value of the car/cars you have: "))
            value_of_car = value_of_car - value_of_owned_car
            type_of_owned_car = input("Is the car that you have SUV(yes/no)? ")
            if type_of_owned_car == "yes":
                work_status = input("Are you worker/executive/businessman(women)")
                if work_status == "worker":
                    family_status = input("What is your family status(single/married/parent/grandparent)? ")
                    if family_status == "single" or family_status == "married":
                        car_type = "Subcompact(B-segment)"
                    elif family_status == "parent":
                        car_type = "Small family car(C-segment)"
                    elif family_status == "grandparent":
                        car_type = "Large family car(D-segment)"
                    else:
                        print("Please enter a valid answer: (single/married/parent/grandparent) ")
                elif work_status == "executive":
                    car_type = "Executive (E-segment)"
                elif work_status == "businessman":
                    car_type = "Luxury(F-segment)"
                else:
                    print("Please enter a valid answer: (yes) or (no) ")
                    continue
            if type_of_owned_car == "no":
                work_status = input("Are you worker/executive/businessman(women)")
                if work_status == "worker":
                    family_status = input("What is your family status(single/married/parent/grandparent)? ")
                    if family_status == "single" or family_status == "married":
                        car_type = "Subcompact crossover SUV (B-segment)"
                    elif family_status == "parent":
                        car_type = "Compact crossover SUV (C-segment)"
                    elif family_status == "grandparent":
                        car_type = "Mid-size crossover SUV (D/E-segment)"
                    else:
                        print("Please enter a valid answer: (single/married/parent/grandparent) ")
                elif work_status == "executive":
                    car_type = "Mid-size crossover SUV (D/E-segment)"
                elif work_status == "businessman":
                    car_type = "Full-size crossover SUV"
                else:
                    print("Please enter a valid answer: (yes) or (no) ")
                    continue
        else:
            print("Please enter a valid answer: (yes) or (no) ")
            continue
        if value_of_car < 0:
            print("It seems that the value of your car is higher than the value we think is right for your car ")
            information_for_method = input("Do you want more information about the calculating method(yes/no)? ")
            if information_for_method == "yes":
                print("We calculate the value by the formula: value = Yearly gross income / 10")
                problem_value = input("Is this acceptable for you(yes/no)? ")
                if problem_value == "no":
                    custom_value = input("What is the value you think is good for your wallet? ")
                    value_of_car = custom_value
        print("Your car must be from type", car_type, "and the cost of the car must be: ", value_of_car)
        right_car = input("Do you want now to find make and model of your future car? ")
        if right_car == "yes":
            print("These are the most popular cars in this segment")
            if car_type == "Subcompact(B-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["B-segment"])
                print(data)
            elif car_type == "Small family car(C-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["C-segment"])
                print(data)
            elif car_type == "Large family car(D-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["D-segment"])
                print(data)
            elif car_type == "Executive (E-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["E-segment"])
                print(data)
            elif car_type == "Luxury(F-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["F-segment"])
                print(data)
            elif car_type == "Subcompact crossover SUV (B-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(B)"])
                print(data)
            elif car_type == "Compact crossover SUV (C-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(C)"])
                print(data)
            elif car_type == "Mid-size crossover SUV (D/E-segment)":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(D)"])
                print(data)
            elif car_type == "Full-size crossover SUV":
                data = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(F)"])
                print(data)
        elif right_car == "no":
            continue
        else:
            print("Please enter a valid answer: (yes) or (no) ")
    else:
        print("Please enter a valid answer: (yes) or (no) ")
