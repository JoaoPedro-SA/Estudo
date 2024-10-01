N = int(input())  

for _ in range(N):
    K = int(input())  
    for _ in range(K):
        feedback = int(input())  
        if feedback == 1:
            print('Rolien')
        elif feedback == 2:
            print('Naej')
        elif feedback == 3:
            print('Elehcim')
        elif feedback == 4:
            print('Odranoel')