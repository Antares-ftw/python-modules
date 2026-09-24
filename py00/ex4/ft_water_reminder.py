def ft_water_reminder():
    watering = input("Days since last watering: ")

    if int(watering) > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_reminder()
