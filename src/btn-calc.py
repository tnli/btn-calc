## startup-values, these should be replaced with some sort of arguments, or something 

world0_tn = 3
world0_ag = False
world0_ex = True
world0_na = True
world0_in = True
world0_ni = False
world0_aff = 'terran'

world1_tn = 4
world1_ag = True
world1_ex = False
world1_na = False
world1_in = False
world1_ni = True
world1_aff = 'imperial'

distance = 3


## basic BTN calculation
btn = world0_tn + world1_tn

## checking if one world is agricultural and the other is either extreme or not agricultural

if (world0_ag and world1_na or world1_ex):
    btn = btn + 0.5
elif (world1_ag and world0_na or world0_ex):
    btn = btn + 0.5

## adjust BTN by affiliation, that is, if one is imperial and the other is in the confederation

if (world0_aff == 'terran' and world1_aff == 'imperial'):
    btn = btn-1
elif (world0_aff == 'imperial' and world1_aff == 'terran'):
    btn = btn-1

## adjust BTN by distance
if (distance <= 0):
    btn = btn + 1
elif (distance > 0 and distance <= 2):
    btn = btn - 0.5
elif (distance > 2 and distance <= 5):
    btn = btn - 1
elif (distance > 5 and distance <= 9):
    btn = btn - 1.5
elif (distance > 9 and distance <= 19):
    btn = btn - 2
else:
    btn = 0 
# return btn

## check if BTN is too big (can't be more than twice+1 the smaller of the two world TN:s

## find smallest, make a function for this...

if (world0_tn > world1_tn):
    smallest_tn = world1_tn
else:
    smallest_tn = world0_tn

if btn > 2 * smallest_tn + 1:
    btn = 2 * smallest_tn + 1

print(btn)
# retrun btn
