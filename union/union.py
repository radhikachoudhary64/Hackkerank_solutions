num_eng=int(input())
eng=set(map(int,input().split()))
num_french=int(input())
french=set(map(int,input().split()))
print(len(eng.union(french)))
