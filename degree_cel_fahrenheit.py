def convert_cel_to_far(celci):
    return celci*9/5+32
def convert_far_to_cel(farh):
    return (farh-32)*5/9
y=input("Enter temperature in degrees F: ")
print(f"{y} degress F = "+str(convert_far_to_cel(float(y)))+" degrees C")
x=input("Enter temperature in degrees C: ")
print(f"{x} degrees C = "+str(convert_cel_to_far(float(x)))+" degrees F")