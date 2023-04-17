

def countMatches(items =[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
                ruleKey ="color", 
                ruleValue ="silver"):
    match = 0
    hash = {"type": 0, "color": 1, "name": 2}
    for i in items:
        if i[hash[ruleKey]] == ruleValue:
            match += 1
    return match

