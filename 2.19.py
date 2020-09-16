lemon_juice=float(input('Enter amount of lemon juice (in cups):'))
water=float(input('Enter amount of water (in cups):'))
agave_nectar=float(input('Enter amount of agave nectar (in cups):'))
serving=float(input('How many servings does this make?'))

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(serving))+' servings')
print(str('{:.2f}'.format(lemon_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(water))+' cup(s) water')
print(str('{:.2f}'.format(agave_nectar))+' cup(s) agave nectar')

print("")
new_serving=float(input('How many servings would you to make?'))
x=new_serving/serving #calculating variable x to find factor of serving to multiply
new_lemon_juice=lemon_juice*x #multiplying every variable by x to adjust it's proportion in lemonade
new_water=water*x
new_agave_nectar=agave_nectar*x

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice))+' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water))+' cup(s) water')
print(str('{:.2f}'.format(new_agave_nectar))+' cup(s) agave nectar')

print("")
print('Lemonade ingredients - yields '+str('{:.2f}'.format(new_serving))+' servings')
print(str('{:.2f}'.format(new_lemon_juice/16))+' cup(s) lemon juice')
print(str('{:.2f}'.format(new_water/16))+' cup(s) water')
print(str('{:.2f}'.format(new_agave_nectar/16))+' cup(s) agave nectar')