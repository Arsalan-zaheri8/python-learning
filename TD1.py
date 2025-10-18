def sapain2 ():
     for i in range(11):
          if i == 10:
               print(" " * (i - 2) + "A" * (i - 7))
          else:
                sapin = " " * (9 - i) + (2 * i + 1) * "A"
                print(sapin)
     
     

sapain2()