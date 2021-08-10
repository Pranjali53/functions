def speeds_of_drivers(speed):
    if speed<70:
        print("ok")
    else:
        points=0
        i=70
        while i<speed:
            if speed%5==0:
                points+=1
            i=i+5
    if points>12:
        print("License suspended")
    else:
        print(points)
speeds_of_drivers(85)
speeds_of_drivers(135)


