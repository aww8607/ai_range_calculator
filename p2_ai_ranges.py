import pandas as pd
#Copyright Africa Cross Games LLC 2023

#This script calculates the distance between each pair of hexes on a map, accounting for obstructions.
#This map will allow the video game AI to navigate ships through chokepoints.
#The hex_type.csv file contains the terrain type of each hex.
#The adjacency function of the range_array_builder class will exclude hexes with impassible terrain types when determining adjacency
#The program will output a .csv file with a two-dimensional array that shows the distance between each hex number.



import numpy as np

ob1=pd.read_csv('hex_type.csv')

number_of_hexes = 375

class range_array_builder():
    def __init__(self):
        print('init')
    
    def adjacency(self, loc_no, side, hex_type):
        
        hex_adjacency = [-1,-1,-1,-1,-1,-1]
        
        if loc_no > -1:
            if loc_no%50>=25:
                if loc_no < 25:
                    hex_adjacency[0] = -1
                else:
                    hex_adjacency[0] = loc_no - 25
                    
                if loc_no < 25 or loc_no%25 == 24:
                    hex_adjacency[1] = -1
                else:
                    hex_adjacency[1] = loc_no - 24
                    
                if loc_no < 25 or loc_no%25 == 24:
                    hex_adjacency[2] = -1
                else:
                    hex_adjacency[2] = loc_no + 1
                    
                if loc_no > 349 or loc_no%25 == 24:
                    hex_adjacency[3] = -1
                else:
                    hex_adjacency[3] = loc_no + 26
                
                if loc_no > 349:
                    hex_adjacency[4] = -1
                else:
                    hex_adjacency[4] = loc_no + 25
                
                if loc_no%25 == 0:
                    hex_adjacency[5] = -1
                else:
                    hex_adjacency[5] = loc_no -1
                    
            elif loc_no%50<25:
                if loc_no < 25 or loc_no%50 == 0:
                    hex_adjacency[0] = -1
                else:
                    hex_adjacency[0] = loc_no - 26
                
                if loc_no < 25:
                    hex_adjacency[1] = -1
                else:
                    hex_adjacency[1] = loc_no - 25
               
                if loc_no%25 == 24:
                    hex_adjacency[2] = -1
                else:
                    hex_adjacency[2] = loc_no + 1
                    
                if loc_no > 349:
                    hex_adjacency[3] = -1
                else:
                    hex_adjacency[3] = loc_no + 25
                    
                if loc_no > 349 or loc_no % 25 == 0:
                    hex_adjacency[4] = -1
                else:
                    hex_adjacency[4] = loc_no + 24
            
                if loc_no % 25 == 0:
                    hex_adjacency[5] = -1
                else:
                    hex_adjacency[5] = loc_no - 1
        
        if side > -1:            
            for i in range(6):
                if hex_adjacency[i] > -1:
                     if hex_type[hex_adjacency[i]] < 1:
                        hex_adjacency[i] = -1
                     elif hex_type[hex_adjacency[i]] == 2 and side > -1:
                        hex_adjacency[i] = -1
                     elif hex_type[hex_adjacency[i]] == 3 and side == 1:
                        hex_adjacency[i] = -1
                     elif hex_type[hex_adjacency[i]] == 4 and side == 0:
                        hex_adjacency[i] = -1
                     elif hex_type[hex_adjacency[i]] == 5 and side == 1:
                        hex_adjacency[i] = -1
                        
                
        
        return hex_adjacency
                     
    def in_range_hexes(self, hex_type, start_range):
        return_array = []
        
        for i in range(number_of_hexes):
            holder_array = []
            holder_array.extend(start_range[i])
            for j in start_range[i]:    
                k = self.adjacency(j,1,hex_type)
                holder_array.extend(k)
                
            return_array.append(set(holder_array))
        return return_array        
        
        
range_0 = []    
for i in range(number_of_hexes):
    n = [i]    
    range_0.append(n)


r1 = range_array_builder()

range_1 = r1.in_range_hexes(ob1.hex_type, range_0)
range_2 = r1.in_range_hexes(ob1.hex_type, range_1)
range_3 = r1.in_range_hexes(ob1.hex_type, range_2)
range_4 = r1.in_range_hexes(ob1.hex_type, range_3)
range_5 = r1.in_range_hexes(ob1.hex_type, range_4)
range_6 = r1.in_range_hexes(ob1.hex_type, range_5)
range_7 = r1.in_range_hexes(ob1.hex_type, range_6)
range_8 = r1.in_range_hexes(ob1.hex_type, range_7)
range_9 = r1.in_range_hexes(ob1.hex_type, range_8)
range_10 = r1.in_range_hexes(ob1.hex_type, range_9)
range_11 = r1.in_range_hexes(ob1.hex_type, range_10)
range_12 = r1.in_range_hexes(ob1.hex_type, range_11)
range_13 = r1.in_range_hexes(ob1.hex_type, range_12)
range_14 = r1.in_range_hexes(ob1.hex_type, range_13)
range_15 = r1.in_range_hexes(ob1.hex_type, range_14)
range_16 = r1.in_range_hexes(ob1.hex_type, range_15)
range_17 = r1.in_range_hexes(ob1.hex_type, range_16)
range_18 = r1.in_range_hexes(ob1.hex_type, range_17)
range_19 = r1.in_range_hexes(ob1.hex_type, range_18)
range_20 = r1.in_range_hexes(ob1.hex_type, range_19)
range_21 = r1.in_range_hexes(ob1.hex_type, range_20)
range_22 = r1.in_range_hexes(ob1.hex_type, range_21)
range_23 = r1.in_range_hexes(ob1.hex_type, range_22)
range_24 = r1.in_range_hexes(ob1.hex_type, range_23)
range_25 = r1.in_range_hexes(ob1.hex_type, range_24)
range_26 = r1.in_range_hexes(ob1.hex_type, range_25)
range_27 = r1.in_range_hexes(ob1.hex_type, range_26)
range_28 = r1.in_range_hexes(ob1.hex_type, range_27)
range_29 = r1.in_range_hexes(ob1.hex_type, range_28)
range_30 = r1.in_range_hexes(ob1.hex_type, range_29)
range_31 = r1.in_range_hexes(ob1.hex_type, range_30)
range_32 = r1.in_range_hexes(ob1.hex_type, range_31)
range_33 = r1.in_range_hexes(ob1.hex_type, range_32)
range_34 = r1.in_range_hexes(ob1.hex_type, range_33)
range_35 = r1.in_range_hexes(ob1.hex_type, range_34)
range_36 = r1.in_range_hexes(ob1.hex_type, range_35)
range_37 = r1.in_range_hexes(ob1.hex_type, range_36)
range_38 = r1.in_range_hexes(ob1.hex_type, range_37)
range_39 = r1.in_range_hexes(ob1.hex_type, range_38)
range_40 = r1.in_range_hexes(ob1.hex_type, range_39)

#print(range_40[188])

distance_score = []    
for m in range(number_of_hexes):
    for n in range(number_of_hexes):
        distance_number = 42
        
        if m == n:
            distance_number = 1
        elif n in range_1[m]:
            distance_number = 2
        elif n in range_2[m]:
            distance_number = 3
        elif n in range_3[m]:
            distance_number = 4
        elif n in range_4[m]:
            distance_number = 5
        elif n in range_5[m]:
            distance_number = 6
        elif n in range_6[m]:
            distance_number = 7
        elif n in range_7[m]:
            distance_number = 8
        elif n in range_8[m]:
            distance_number = 9
        elif n in range_9[m]:
            distance_number = 10
        elif n in range_10[m]:
            distance_number = 11
        elif n in range_11[m]:
            distance_number = 12
        elif n in range_12[m]:
            distance_number = 13
        elif n in range_13[m]:
            distance_number = 14
        elif n in range_14[m]:
            distance_number = 15
        elif n in range_15[m]:
            distance_number = 16
        elif n in range_16[m]:
            distance_number = 17
        elif n in range_17[m]:
            distance_number = 18
        elif n in range_18[m]:
            distance_number = 19
        elif n in range_19[m]:
            distance_number = 20
        elif n in range_20[m]:
            distance_number = 21
        elif n in range_21[m]:
            distance_number = 22
        elif n in range_22[m]:
            distance_number = 23
        elif n in range_23[m]:
            distance_number = 24
        elif n in range_24[m]:
            distance_number = 25
        elif n in range_25[m]:
            distance_number = 26
        elif n in range_26[m]:
            distance_number = 27
        elif n in range_27[m]:
            distance_number = 28
        elif n in range_28[m]:
            distance_number = 29
        elif n in range_29[m]:
            distance_number = 30
        elif n in range_30[m]:
            distance_number = 31
        elif n in range_31[m]:
            distance_number = 32
        elif n in range_32[m]:
            distance_number = 33
        elif n in range_33[m]:
            distance_number = 34
        elif n in range_34[m]:
            distance_number = 35
        elif n in range_35[m]:
            distance_number = 36
        elif n in range_36[m]:
            distance_number = 37
        elif n in range_37[m]:
            distance_number = 38
        elif n in range_38[m]:
            distance_number = 39
        elif n in range_39[m]:
            distance_number = 40
        elif n in range_40[m]:
            distance_number = 41
            
               
               
        text_holder = 'ai_ranges['+str(m)+']['+str(n)+']='+str(distance_number)+';'
        distance_score.append(text_holder)    

out_df = pd.DataFrame(distance_score)

out_df.to_csv('p2_ai_ranges.csv', index=False)


