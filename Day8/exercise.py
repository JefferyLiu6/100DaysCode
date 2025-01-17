def calculate_love_score(name1 = "Angela Yu", name2 = "Jack Bauer"):
    name3 = name1+name2
    name3 = name3.lower()
    list1 = ["t","r","u","e"]
    list2 = ["l","o","v","e"]
    count1 = 0
    count2 = 0
    
    for i in range (len(name3)):
        if name3[i] in list1:
            count1 += 1
        
        if name3[i] in list2:
            count2 += 1
            
    print(count1*10+count2)
        
calculate_love_score("Kanye West", "Kim Kardashian")