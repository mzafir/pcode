
def playGame(arr, cntr):

    if cntr > len(arr) - 1:
        cntr = cntr - len(arr) - 1
        playGame(arr, cntr)

    if cntr < 0 :
        cntr= len(arr) + cntr
        playGame(arr,cntr)

    if 0 <= cntr <= len(arr)-1 and arr[cntr] == 0:
         playGame(arr, cntr)


    else:
        playGame(arr, cntr+arr[cntr])
        playGame(arr, cntr-arr[cntr])


array1 = [1,2,1,7,0,3,2,5,2]
playGame(array1, 0)