def main():
    s = int(input())
    
    #s=3672
    
    h = s//3600
    s -= h*3600
    
    m = s//60
    s -= m*60
    
    print("Hours: ", h)
    print("Minutes: ", m)
    print("Seconds: ", s)

main()
