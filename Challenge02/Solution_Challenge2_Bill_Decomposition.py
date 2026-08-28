def main():
    n = int(input())
    
    ballenas = n//500
    n -= ballenas*500
    
    sorjuana = n//200
    n -= sorjuana*200
    
    moctezuma = n//100
    n -= moctezuma*100
    
    ajolote = n//50
    n -= ajolote*50
    
    benito = n//20
    n -= benito*20
    
    print("500: ", ballenas)
    print("200: ", sorjuana)
    print("100: ", moctezuma)
    print("50: ", ajolote)
    print("20: ", benito)
    
    if n > 0:
        print("Remaining: ", n)

main()


