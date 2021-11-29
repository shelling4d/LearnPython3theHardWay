#汽车总数
cars = 100

#汽车定员
space_in_a_car = 4.0

#司机数量
drivers = 30

#乘客数量
passengers = 90

#没有司机的车
cars_not_driven = cars - drivers

#有司机的车
cars_driven = drivers

#
carpool_capacity = cars_driven * space_in_a_car

#平均每辆车乘客
average_passengers_per = passengers / cars_driven

print("There are", cars, "cars in avaiable.")
print("There are only", drivers, "drivers available.")
print("That will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "peoople today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per, "in each car.")
