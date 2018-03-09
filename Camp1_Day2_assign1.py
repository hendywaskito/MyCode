#Assigment Answer for Camp1_Day2_assign1
#Script Author: Hendy Waskito
#Company: Packet Systems Indonesia

#Given dataset as below
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

#Getting sessions value and split it
Hasil = Sessions_Attended.get('sessions').split(',')

#Count the size of array from split result
Ukuran = len(Hasil)

#Print
print("I have attended",Ukuran, "sessions!!")
