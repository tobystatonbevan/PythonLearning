blocks = int(input("Enter the number of blocks: "))
height = 0

#if blocks:
#    layer = 1
#else:
#    layer = 0

#you have to check layer against blocks before you can increment height (i still don't understand why you need a layer variable, when it is largely the same as height)
#I think it is because a layer may not complete and so height shouldn't increment for a failed layer
#while layer <= blocks: 
#    height+=1
#    blocks-=layer
#    layer+=1

#while the height/width is less than the number of blocks available (a layer can be completed)
while height <= blocks: 
    #removes the number of blocks needed for this layer from available blocks
    blocks-=height
    #increments the height ready for the next attempt
    height+=1
else:
    #removes the previous increment if attempt not successful
    height-=1
    
print("The height of the pyramid:", height)