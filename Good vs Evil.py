def goodVsEvil(good, evil):
    i = 0
    good = good.split()
    evil = evil.split()
    cgood = [1,2,3,3,4,10]
    cevil = [1,2,2,2,3,5,10]
    good_result = 0
    evil_result = 0
    for g in good:
        good_result += float(g) * cgood[i]
        i += 1
    i = 0
    for e in evil:
        evil_result += float(e) * cevil[i]
        i+= 1
    if good_result > evil_result:
        return 'Battle Result: Good triumphs over Evil'
    elif good_result < evil_result:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'