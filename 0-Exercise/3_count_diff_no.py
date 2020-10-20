
ip = input('Enter ip address = ')
ip = ip + '.'

seg_no = 1
seg_len = 0

for i in ip:
    if i in '0123456789':
        seg_len += 1
    elif i == '.':
        print('The segment no. {} has length of {}'.format(seg_no,seg_len))
        seg_no = seg_len + 1
        seg_len = 0
