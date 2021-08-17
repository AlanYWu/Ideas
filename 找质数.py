for i in range(2,100):
     for j in range(2,int(i**0.5)):
          if i % j == 0:
               break
          else:
               print(i)
          break
             