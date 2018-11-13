
#CONSTANTS
ZONE_1_BEGIN = 0
ZONE_1_END = 30
ZONE_2_BEGIN = ZONE_1_END + 1
ZONE_2_END = 60
ZONE_3_BEGIN = ZONE_2_END + 1
ZONE_3_END = 90
ENTRANCE_FEE = 1.25
CAMERA_CHARGE = 4.15
PER_KM_CHARGE_LIGHT = 0.4085
PER_KM_CHARGE_HEAVY = 0.8175
ZONE2_SURCHARGE = 1.27
TAXES = 1.13

#DISPLAY INSTRUCTIONS FUNCTION
def display_instructions():
    '''() -> None
    
    Print program instructions on screen.
    
    >>> display_instructions()
    None
    
    '''
    print("This program calculates the toll charges for a paid highway.\nLight vehicles will be charged at a rate of", round(PER_KM_CHARGE_LIGHT * 100, 2), "cents per km.\nHeavy vehicles will be charged at a rate of", round(PER_KM_CHARGE_HEAVY * 100, 2), "cents per km.\nThere are three travelling zones as follows:\n\n-Zone 1: from km marker", ZONE_1_BEGIN, "to marker", ZONE_1_END, ".\n-Zone 2: from km marker", ZONE_2_BEGIN, "to marker", ZONE_2_END, ".\n-Zone 3: from km marker", ZONE_3_BEGIN, "to marker", ZONE_3_END, ". \n\nThere will be a surcharge of " + "{0:.0f}%".format((ZONE2_SURCHARGE - 1) * 100) + " to travel in Zone 2.\nEach trip will be charged a highway entrance fee of $" + str(ZONE2_SURCHARGE) + ".\nVehicles without a rental transponder will be charged an additional camera recording fee of $" + str(CAMERA_CHARGE) + ".\nAll applicable Ontario taxes " + "({0:.0f}%)".format((TAXES - 1) * 100) + " will be added to the total.")
           
           
  
#DETERMINE ZONE FUNCTION           
def determine_zone(marker):
    ''' (int) -> int
    
    Return the highway zone correspondent to the kilometer marker entered by customer. 
    
    >>> determine_zone(46)
    2
    
    >>> determine_zone(80)
    3
    
    >>> determine_zone(0)
    1
    '''
    if marker >= ZONE_1_BEGIN and marker <= ZONE_1_END:
        return 1
    if marker >= ZONE_2_BEGIN and marker <= ZONE_2_END:
        return 2
    if marker >= ZONE_3_BEGIN and marker <= ZONE_3_END:
        return 3
    
    
#CALCULATE TOLL CHARGE FUNCTION    
def calculate_toll_charge(entry, exit, vehicle):
    '''(int, int, str) -> float
    
    Return the toll charge for a given customer based on entry marker, exit marker and vehicle type.
    
    >>> calculate_toll_charge(4, 28, "L")
    9.804
    
    >>> calculate_toll_charge(6, 78, "L")
    32.72085
    '''
    
    entry_zone = determine_zone(entry)
    exit_zone = determine_zone(exit)
    total_distance = abs(entry - exit)
    distance1 = 0
    distance2 = 0
    distance3 = 0
    
    if entry_zone == exit_zone:
        if entry_zone == 1:
            distance1 = total_distance
        elif entry_zone == 2:
            distance2 = total_distance        
        elif entry_zone == 3:
            distance3 = total_distance 
            
    elif entry_zone == 1 and exit_zone == 2:
        distance1 = abs(ZONE_1_END - entry)
        distance2 = total_distance - distance1
        
    elif entry_zone == 1 and exit_zone == 3:
        distance1 = abs(ZONE_1_END - entry)
        distance2 = 30
        distance3 = total_distance - distance1 - distance2
        
    elif entry_zone == 2 and exit_zone == 3:
        distance2 = abs(ZONE_2_END - entry)
        distance3 = total_distance - distance2
        
    elif entry_zone == 2 and exit_zone == 1:
        distance2 = abs(ZONE_1_END - entry)
        distance1 = total_distance - distance2
        
    elif entry_zone == 3 and exit_zone == 2: 
        distance3 = abs(ZONE_2_END - entry)
        distance2 = total_distance - distance3
        
    elif entry_zone == 3 and exit_zone == 1:
        distance3 = abs(ZONE_2_END - entry)
        distance2 = 30
        distance1 = total_distance - distance3 - distance2
        
    if vehicle == "L" or vehicle == "l":
        total_charge = (distance1 * PER_KM_CHARGE_LIGHT)  + (distance2 * ZONE2_SURCHARGE * PER_KM_CHARGE_LIGHT) + (distance3 * PER_KM_CHARGE_LIGHT)
        return total_charge
    
    elif vehicle == "H" or vehicle == "h":
        total_charge = (distance1 * PER_KM_CHARGE_HEAVY)  + (distance2 * ZONE2_SURCHARGE * PER_KM_CHARGE_HEAVY) + (distance3 * PER_KM_CHARGE_HEAVY)
        return total_charge
        
    

#CALCULATE TOTAL BILL FUNCTION
def calculate_total_bill(toll_charge, transponder):
    '''(float, bool) -> float
    
    Return the total bill for a given customer based off of toll charge and if the customer has a transponder or not.
    
    >>> calculate_total_bill(9.804, True)
    12.49
    >>> calculate_total_bill(8.987, True)
    11.57
    '''
    toll_charge = calculate_toll_charge(entry, exit, vehicle)
    if transponder == True:
        return (toll_charge + ENTRANCE_FEE) * TAXES
    else: 
        return (toll_charge + CAMERA_CHARGE + ENTRANCE_FEE) * TAXES
    
    
#MAIN FUNCTION
display_instructions()
entry = int(input("Enter the entry marker: "))
exit = int(input("Enter the exit marker: "))
vehicle = input("Enter the type of vehicle driven on your trip. Type L for light and H for heavy: ")
transponder = input("Do you have a transponder? Type Y for yes and N for no: ")
if transponder == "Y" or transponder == "y":
    transponder = True
elif transponder == "N" or transponder =="n":
    transponder = False
    print("NOTE: Since you do not own a transponder, you will be required to pay\nan additional camera recording fee of $" + str(CAMERA_CHARGE) + ".") 
toll_charge = calculate_toll_charge(entry, exit, vehicle)
total_charge = calculate_total_bill(calculate_toll_charge, transponder)
print ("Total due is:", round(total_charge, 2)) 

