try:
    fhand = open("mailbox.txt")
except:
    print('File cannot be opened')
    exit()


lines=fhand.readlines()
file=open('output.txt', 'w')
for line in lines:
       if 'JAMES SMTP' in line:
           ind=line.find('SMTP ID ')
           en_ind=line.find(';')
           word=line[ind+8:en_ind]
           print(word)
           file.write(word)
           file.write('\n')
fhand.close()
