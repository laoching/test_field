txt = input('문자열: ')
cnt = {}
'''
for ch in txt:
    if ch not in cnt:
        cnt[ch] = 1
    else:
        cnt[ch] +=1
'''
# 내포 표기
cnt = {ch: txt.count(ch) for ch in txt}
print('분포=', cnt)