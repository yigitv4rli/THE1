print("""Sequence 1 = [13, 7, 13, 11, 5, 3, 3, 1, 11, 7, 9, 13, 1, 11, 11, 9, 3, 9, 1, 11, 9, 1, 7, 13, 13]
Sequence 2 = [12, 12, 8, 0, 0, 2, 4, 8, 8, 12, 14, 0, 10, 12, 8, 10, 12, 4, 4, 4, 6, 12, 6, 10, 12]
Sequence 3 = [12, 10, 10, 6, 4, 10, 2, 4, 0, 6, 4, 2, 10, 2, 2, 10, 6, 6, 4, 4, 12, 0, 6, 4, 2]
Sequence 4 = [6, 12, 6, 0, 14, 12, 0, 12, 0, 10, 0, 12, 12, 6, 12, 6, 14, 4, 2, 6, 8, 2, 14, 4, 8]
Sequence 5 = [6, 9, 3, 9, 12, 9, 12, 12, 0, 0, 9, 3, 6, 3, 9, 12, 12, 9, 6, 6, 6, 6, 6, 9, 9]
Sequence 6 = [11, 13, 0, 6, 13, 2, 1, 6, 15, 10, 14, 13, 5, 5, 7, 0, 10, 14, 14, 9, 16, 11, 17, 14, 17]
Sequence 7 = [15, 7, 13, 8, 7, 6, 12, 8, 17, 10, 8, 12, 3, 0, 2, 6, 0, 17, 10, 17, 16, 10, 13, 16, 7]
Sequence 8 = [16, 13, 1, 8, 3, 8, 3, 3, 15, 6, 8, 17, 0, 12, 15, 3, 10, 9, 5, 6, 10, 17, 13, 1, 16]
Sequence 9 = [4, 15, 6, 5, 11, 1, 10, 0, 7, 0, 13, 0, 0, 13, 8, 12, 6, 3, 15, 12, 5, 1, 6, 8, 8]
Sequence 10 = [16, 15, 5, 13, 9, 12, 4, 4, 16, 7, 2, 17, 15, 8, 15, 9, 16, 7, 1, 5, 11, 7, 9, 7, 6]
Sequence 11 = [1, X, 8, 0, 10, 7, 0, 16, 2, 1, 11, 8, 0, 10, 16, 0, 2, 1, 3, 1, 16, 8, 0, 10, 26, 0, 2, 2, 3, 1, 16,10, 34, 0, 3, 1, 2, 2, 14, 2, 1, 16, 10, 45, 0, 3, 1, 4, 37, 14, 13, 4, 1, 16,
10, 61, 1, 0, 8, 0, 0, 1, 1, 4, 37, 11, 8, 37, 9, 34] Sequence 11 checks whether or not X is prime""")

seq = [[13, 7, 13, 11, 5, 3, 3, 1, 11, 7, 9, 13, 1, 11, 11, 9, 3, 9, 1, 11, 9, 1, 7, 13, 13],
[12, 12, 8, 0, 0, 2, 4, 8, 8, 12, 14, 0, 10, 12, 8, 10, 12, 4, 4, 4, 6, 12, 6, 10, 12],
[12, 10, 10, 6, 4, 10, 2, 4, 0, 6, 4, 2, 10, 2, 2, 10, 6, 6, 4, 4, 12, 0, 6, 4, 2],
[6, 12, 6, 0, 14, 12, 0, 12, 0, 10, 0, 12, 12, 6, 12, 6, 14, 4, 2, 6, 8, 2, 14, 4, 8],
[6, 9, 3, 9, 12, 9, 12, 12, 0, 0, 9, 3, 6, 3, 9, 12, 12, 9, 6, 6, 6, 6, 6, 9, 9],
[11, 13, 0, 6, 13, 2, 1, 6, 15, 10, 14, 13, 5, 5, 7, 0, 10, 14, 14, 9, 16, 11, 17, 14, 17],
[15, 7, 13, 8, 7, 6, 12, 8, 17, 10, 8, 12, 3, 0, 2, 6, 0, 17, 10, 17, 16, 10, 13, 16, 7],
[16, 13, 1, 8, 3, 8, 3, 3, 15, 6, 8, 17, 0, 12, 15, 3, 10, 9, 5, 6, 10, 17, 13, 1, 16],
[4, 15, 6, 5, 11, 1, 10, 0, 7, 0, 13, 0, 0, 13, 8, 12, 6, 3, 15, 12, 5, 1, 6, 8, 8],
[16, 15, 5, 13, 9, 12, 4, 4, 16, 7, 2, 17, 15, 8, 15, 9, 16, 7, 1, 5, 11, 7, 9, 7, 6],
[1, 6, 8, 0, 10, 7, 0, 16, 2, 1, 11, 8, 0, 10, 16, 0, 2, 1, 3, 1, 16, 8, 0, 10, 26, 0, 2, 2, 3, 1, 16,10, 34, 0, 3, 1, 2, 2, 14, 2, 1, 16, 10, 45, 0, 3, 1, 4, 37, 14, 13, 4, 1, 16,10, 61, 1, 0, 8, 0, 0, 1, 1, 4, 37, 11, 8, 37, 9, 34]]

x = int(input("\nWhich sequence do you want to work on? (Please write a number in range 1-11): "))
    
seq = seq[x-1]

r1 = 0 
r2 = 0
i = 0
c = 0
if x == 11:
	X = int(input("\nWhich number do you want to test: "))
	seq[1] = X
print("\nYour sequence is {}:".format(seq))
input("Press Enter to Start\n")

while True:
    inst = seq[i]
    c +=1
    print("--------------------Cycle {}---------------------\n".format(c))

    if inst == 0:
        print("Instruction 0. Halt the process.")
        print("Final Picture of Your Sequence is {}".format(seq))
        print("Final Picture of R1, R2, I ==>  R1: {} , R2: {} , I: {}\n".format(r1,r2,i))
        
        break

    elif inst == 1:
        print("Instruction 1. Load R1 with the next number in the sequence. R1 <- [I+1], I <- I+2")
        r1 = seq[i+1]
        i +=2

    elif inst == 2:
        print("Instruction 2. Load R2 with the next number in the sequence. R2 <- [I+1], I <- I+2")
        r2 = seq[i+1]
        i +=2

    elif inst == 3:
        print("Instruction 3. Load R1 with the sequence element which is at the position given as the next number in the sequence. R1 <- [[I+1]], I <- I+2")
        r1 = seq[seq[i+1]]
        i +=2

    elif inst == 4:
        print("Instruction 4. Load R2 with the sequence element which is at the position given as the next number in the sequence. R2 <- [[I+1]], I <- I+2")
        r2 = seq[seq[i+1]]
        i +=2

    elif inst == 5:
        print("Instruction 5. Load R1 with the content of R2. R1 <- R2 ,I <- I+1")
        r1 = r2
        i +=1

    elif inst == 6:
        print("Instruction 6. Load R1 with the sequence element which is at the position R2. R1 <- [R2], I <- I+1")
        r1 = seq[r2]
        i +=1

    elif inst == 7:
        print("Instruction 7. Change the sequence element which is at the position R1 to be the content of R2. [R1] <- R2, I <- I+1")
        seq[r1] = r2
        i +=1

    elif inst == 8:
        print("Instruction 8. Change the sequence element which is at the position given as the next number in the sequence to the content of R1. [[I+1]] <- R1 , I <- I+2")
        seq[seq[i+1]] = r1
        i +=2

    elif inst == 9:
        print("Instruction 9. Take the sequence element which is at the position given as the next number in the sequence as the next instruction to be performed. I <- [I+1]")
        i = seq[i+1]

    elif inst == 10:
        print("Instruction 10. If R1 contains zero continue with the sequence element following the next one as the next instruction to be performed, otherwise act like the instruction 9.\n if R1 = 0 : I <- I+2\notherwise : I <- [I+1]")
        if r1 == 0:
            i +=2
        else:
            i = seq[i+1]

    elif inst == 11:
        print("Instruction 11. Increment R1 by the content of R2. R1 <- R1+R2, I <- I+1")
        r1 = r1 + r2
        i +=1

    elif inst == 12:
        print("Instruction 12. Decrement R1 by the content of R2. R1 <- R1-R2, I <- I+1")
        r1 = r1 - r2
        i +=1

    elif inst == 13:
        print("Instruction 13. Multiply R1 by the content of R2. R1 <- R1*R2, I<- I+1")
        r1 = r1 * r2
        i +=1

    elif inst == 14:
        print("Instruction 14. Divide R1 by the content of R2 (integer division). R1 <- R1/R2, I <- I+1")
        r1 = r1 // r2
        i +=1

    elif inst == 15:
        print("Instruction 15. Change the sign of the value in R1. R1 <- -R1, I <- I+1")
        r1 = -r1
        i +=1

    elif inst == 16:
        print("Instruction 16. Compare the content of R1 with the content of R2. \nIf R1 = R2 : R1 <- 0 \nelse if R1 > R2 : R1 <- 1\notherwise: R1 <- -1\nalways I <- I+1")
        if r1 == r2:
            r1 = 0
        elif r1 > r2:
            r1 = 1
        else:
            r1 = -1
        i +=1
    if r1 < -127 :
        print("\nIn R1 underflow occured.")
        r1 = "*"
    elif r1 > +127 :
        print("\nIn R1 overflow occured.")
        r1 = "*"
    if r2 < -127 :
        print("\nIn R2 underflow occured.")
        r2 = "*"
    elif r2 > 127 :
        print("\nIn R2 overflow occured.")
        r2 = "*"
    if inst > 16:
        print("\nUndefined instruction.")
        break
    elif inst < 0:
        print("\nUndefined instruction.")
        break
    

    print("\nYour sequence: {}".format(seq))
    print("R1: {} , R2: {} , I: {}\n".format(r1,r2,i))
    print("------------------------------------------------")
    
    if r1 == "*" or r2 == "*":
        break

    input("\nPress Enter to Run Next Cycle\n")
