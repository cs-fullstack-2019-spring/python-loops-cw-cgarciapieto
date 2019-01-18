
def main():
    # prints the range from -21 to 50
    # for x in range(-21, 51):
    #     print(x)


    # # prints range by 2
    # for x in range(0, 10):
    #     print(x * 2)


num = int(input('How many numbers: '))
total_sum = 0

for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers

avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

if __name__ == '__main__':



    main()


