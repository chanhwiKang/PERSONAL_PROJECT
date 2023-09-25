def solution(hp):
    five = hp // 5
    hp %= 5 
    three = hp // 3
    hp %= 3
        
    return five + three + hp