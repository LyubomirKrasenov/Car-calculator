import streamlit as st
import pandas as pd
car_type = ""
data_of_cars = ""
st.title("Car Calculator")
st.subheader("Now I will help you find your future car")
main_answer = st.radio("Do you want to buy a new car(yes/no)?", options=("yes", "no"))
if main_answer == "yes":
    income = st.slider(
            "What is your yearly gross income? ", key="income_slider", min_value=0, max_value=1000000, value=100000)
    value_of_car = income / 10
    st.write(f"The value of your car/cars must be: {value_of_car}")
    state = st.checkbox("Do you have another car?", value=False)
    if state:
        value_of_owned_car = st.slider(
            "What is the value of owned car? ", key="value_slider", min_value=0, max_value=1000000, value=100)
        value_of_car = value_of_car - value_of_owned_car
        type_of_car = st.checkbox("Is the car you have SUV(yes/no)?", value=False)
        if state:
            work_status = st.radio("What is your work status? ", options=("worker", "executive", "businessmen"))
            if work_status == "worker":
                family_status = st.radio("What is your family status? ", options=("single", "married", "parent",
                                                                                  "grandparent"))
                if family_status == "single" or family_status == "married":
                    car_type = "Subcompact(B-segment)"
                elif family_status == "parent":
                    car_type = "Small family car(C-segment)"
                else:
                    car_type = "Large family car(D-segment)"
            elif work_status == "executive":
                car_type = "Executive (E-segment)"
            else:
                car_type = "Luxury(F-segment)"
        else:
            work_status = st.radio("What is your work status? ", options=("worker", "executive", "businessmen"))
            if work_status == "worker":
                family_status = st.radio("What is your family status? ", options=("single", "married", "parent",
                                                                                  "grandparent"))
                if family_status == "single" or family_status == "married":
                    car_type = "Subcompact crossover SUV (B-segment)"
                elif family_status == "parent":
                    car_type = "Compact crossover SUV (C-segment)"
                else:
                    car_type = "Mid-size crossover SUV (D/E-segment)"
            elif work_status == "executive":
                car_type = "Mid-size crossover SUV (D/E-segment)"
            else:
                car_type = "Full-size crossover SUV"
    else:
        work_status = st.radio("What is your work status? ", options=("worker", "executive", "businessmen"))
        if work_status == "worker":
            family_status = st.radio("What is your family status? ", options=("single", "married", "parent",
                                                                              "grandparent"))
            if family_status == "single" or family_status == "married":
                car_type = "Subcompact crossover SUV (B-segment)"
            elif family_status == "parent":
                car_type = "Compact crossover SUV (C-segment)"
            else:
                car_type = "Mid-size crossover SUV (D/E-segment)"
        elif work_status == "executive":
            car_type = "Mid-size crossover SUV (D/E-segment)"
        else:
            car_type = "Full-size crossover SUV"
    if value_of_car < 0:
        st.write("It seems that the value of your car is higher than the value we think is right for your car ")
        information_for_method = st.radio("Do you want more information about the calculating method(yes/no)? ",
                                          options=("yes", "no"))
        if information_for_method == "yes":
            st.write("We calculate the value by the formula: value = Yearly gross income / 10")
            problem_answer = st.radio("Do you want to write your own value for car(yes/no)? ", options=("yes", "no"))
            if problem_answer == "yes":
                custom_value = st.slider("What is the value you think is good for your wallet? ", min_value=0,
                                         max_value=1000000, value=100000)
                value_of_car = custom_value
    st.write("Your car must be from type", car_type, "and the cost of the car must be: ", value_of_car)
    right_car = st.radio("Do you want now to find make and model of your future car(yes/no)? ", options=("yes", "no"))
    if right_car == "yes":
        st.write("These are the most popular cars in this segment")
        if car_type == "Subcompact(B-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["B-segment"])
        elif car_type == "Small family car(C-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["C-segment"])
        elif car_type == "Large family car(D-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["D-segment"])
        elif car_type == "Executive (E-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["E-segment"])
        elif car_type == "Luxury(F-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["F-segment"])
        elif car_type == "Subcompact crossover SUV (B-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(B)"])
        elif car_type == "Compact crossover SUV (C-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(C)"])
        elif car_type == "Mid-size crossover SUV (D/E-segment)":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(D)"])
        elif car_type == "Full-size crossover SUV":
            data_of_cars = pd.read_csv(r"C:\Users\Lubomir\Desktop\cars.csv", usecols=["SUV(F)"])
        st.write(data_of_cars)
car_list = st.radio("Now would you like to see car classifieds in your region(yes/no)? ", options=("yes", "no"))
if car_list == "yes":
    st.write("Go to this website:")
    st.markdown("[Mobile.bg](https://www.mobile.bg/)")
