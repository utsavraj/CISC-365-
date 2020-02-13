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



def main():
  sample = [1,2,3,4,5,6]
  Binary_Search(sample, 3)



if __name__ == '__main__':
    main()
