from hashlib import md5

i = 0
res = ''
while res[0:5] != '00000':
    i += 1
    m = md5()
    m.update('ckczppom' + str(i))
    res = m.hexdigest()
    print i
