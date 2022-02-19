x = bytes('한글', 'utf-8')
print(f'문자열을 바이트로 변환: {x}')
y = x.decode('utf-8')
print(f'바이트를 문자열로 변환: {y}')