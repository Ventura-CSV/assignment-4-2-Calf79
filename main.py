def main():
    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
   
    """
    ########################################
    Code Your Program here
    ########################################
    """
    while True:
        if N>2:
            break
        else:
            print("N should be greater than 2")
    result =[a1,a2]
    for i in range(2,N):
        num= result[-2] + result[-1]
        result.append(num)
        print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result



if __name__ == '__main__':
    main()
