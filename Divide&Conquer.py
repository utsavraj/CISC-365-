#For Chapter: Divide and Conquer


def Binary_Search(A, to_find):
  #If array is empty
  if not A:
    print("Not in Array")
  
  else:
    mid = len(A)//2
    if (A[mid] == to_find):
      print("Found")

    if (A[mid] < to_find):
      Binary_Search(A[mid+1:len(A)], to_find)

    if (A[mid] > to_find):
      Binary_Search(A[0:mid], to_find)


def Merge_Sort(A):
  if not A:
    print("Empty Array provided as input")
  
  if (len(A) < 4):
    sorted(A)

  else:
    mid = len(A)//2
    first_half = Merge_Sort(A[0:mid])
    second_half = Merge_Sort(A[mid+1:len(A)])




#Used as a pivot to sort everything arround it. 
def Partition(A):






def Quick_Sort(A):
  if not A:
    print("Empty Array provided as input")

  if (len(A) < 4):
    sorted(A)

  else:
    q = Partition(A)
    first_half = Quick_Sort(A[0:q - 1])
    second_half = Quick_Sort(A[q + 1:len(A)])







def main():

  #For Search Algo only
  sample_1 = [1,2,3,4,5,6]
  Binary_Search(sample_1, 3)

  #For Sort Algo only
  sample_2 = [6,5,4,3,2,1,0]
  Merge_Sort(sample_2)
  Quick_Sort(sample_2)

if __name__ == '__main__':
    main()
