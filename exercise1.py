fhand = open("mailbox.txt")

lines=fhand.readlines()
fhand=open('output.txt', 'w')

for line in lines:
   if 'SMTP ID' in line:
      print(line[68:-1])
      fhand.write(line[68:-1])
      fhand.write('\n')
fhand.close()
fhand.close()
