while True:
    print('please type p or a for get Perimeter or Area')
    t=input()
    if t in ['a','p']:
        print('give me your width and length')
        x=int(input())
        y=int(input())
        if  t=='a':
            print('your Area: ',(x*y))
        elif t=='p':
            print('your Perimeter: ',(2*(y+x)))
        repetition=input("Let's do next calculation? (yes/no): ")
        if repetition=='no':
            print('Thank you for choosing us')
            break
    else:
        print('Invalid Input')
