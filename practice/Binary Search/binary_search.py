def BinarySearch(arr,search,l,h):
    # l=0
    # m=(len(arr)-1)/2
    # h=len(arr)-1
        if h>=l:
            mid=int(l + (h - l) / 2)
            print(mid)
            if(arr[mid]==search):
                return mid
            if(arr[mid]>search):
                
                return BinarySearch(arr,search,l,mid-1)
            else:
                   
                return BinarySearch(arr,search,mid+1,h)
        else : return -1
def BinarySearch_V2(arr,search):
    l=0
    h=len(arr)-1
    
    while(h>=l):
        mid=l + (h - l) // 2
        if(arr[mid]==search):
            return mid
        if(arr[mid]>search):
            h=mid-1
        else: l=mid-1




    return -1
        

arr=[1,2,3,4,5,6,7,8,9]

search=7
print(BinarySearch_V2(arr,search))
