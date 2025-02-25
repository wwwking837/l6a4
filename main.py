setc1 = {"green", "blue"}
setc2 = {"blue", "yellow"}
setc3 = {"blue", "red"}

print("Original sets :")
print(setc1)
print(setc2)
print(setc3)

seta = setc1.union(setc2)
print("\nUnion of the above sets :")
print(seta)

setb = setc2.union(setc3)
print("\nUnion of the above sets :")
print(setb)

setc = setc1.union(setc3)
print("\nUnion of the above sets :")
print(setc)