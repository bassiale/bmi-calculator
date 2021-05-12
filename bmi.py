print("this program tells you your bmi")
def bma():
    #take the parameters
     name = input('insert your name here')
     height = float(input('insert your height:'))
     weight = int(input('insert your weight here'))
     age = int(input('input your age here'))
     done = 1
     #actually calculate bmi if you can
     if age >= 16 :
         bmi = weight/(height**2)
         print(name)
         print("your bmi is:" + str(bmi))
         done = int(input('type 1 if you want to calculate another bmi, type 2 if you want to stop:'))
     else:
         print('bmi cannot be calculated if under 16yrs old')
         done = int(input('type 1 if you want to calculate another bmi, type 2 if you want to stop:'))
     return done

while True :
    done = bma()
    if done == 1:
         bma()
         print(done)
    elif done == 2 :
        print("finished")
        quit()