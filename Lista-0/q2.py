ferro_total = int(input())
ferro_hogsmade = ferro_total//3
ferro_kakariko = ferro_total//3
ferro_solitude = ferro_total//3
ferro_fora = ferro_total - ferro_solitude - ferro_hogsmade - ferro_kakariko

if ferro_total >= 3:
    print(str(ferro_solitude))
    print(str(ferro_fora))