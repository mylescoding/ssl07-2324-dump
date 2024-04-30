

kbt5 = 3886
kbt9 = 23
kbt10 = 97

sum1 = kbt5+kbt9+kbt10

print("sum1:"+ str(sum1))

kuf5 = 3754
kuf4b = 115
kuf4a = 4
kuf4 = 135

#divide into kuf 5,4b,4a,4

sum2 = (kuf4 + kuf4a + kuf4b + kuf5)

print("sum2:"+ str(sum2))


ratio1 = kuf5/sum2
ratio2 = kuf4b/sum2
ratio3 = kuf4a/sum2
ratio4 = kuf4/sum2

for_kbt5 = ratio1*kbt5 + ratio2*kbt5 + ratio3*kbt5 + ratio4*kbt5
for_kbt9 = ratio1*kbt9 + ratio2*kbt9 + ratio3*kbt9 + ratio4*kbt9
for_kbt10 = ratio1*kbt10 + ratio2*kbt10 + ratio3*kbt10 + ratio4*kbt10

kbt5_to_kuf5 =int(ratio1*kbt5)
kbt5_to_kuf4b = int(ratio2*kbt5)
kbt5_to_kuf4a =int(ratio3*kbt5)
kbt5_to_kuf4 = int(ratio4*kbt5)

print("kbt5 to kuf5:" + str(kbt5_to_kuf5))
print("kbt5 to kuf4b:" + str(kbt5_to_kuf4b))
print("kbt5 to kuf4a:" + str(kbt5_to_kuf4a))
print("kbt5 to kuf4:" + str(kbt5_to_kuf4))


print("kbt5 to kuf5:" + str(ratio1*kbt5))
print("kbt5 to kuf4b:" + str(ratio2*kbt5))
print("kbt5 to kuf4a:" + str(ratio3*kbt5))
print("kbt5 to kuf4:" + str(ratio4*kbt5))

print("for kbt5: " + str(for_kbt5))
print("from integers:" + str(kbt5_to_kuf5 + kbt5_to_kuf4b + kbt5_to_kuf4a +kbt5_to_kuf4))




print("sum3:" + str(for_kbt5 + for_kbt9 + for_kbt10))


#lacks special case for uturn