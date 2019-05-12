import re
import os

class Modify(object):
    def __init__(self):
        self.file = 'AWS-SysOps_v6.txt'
        self.path='./files2/'

    def main(self):
        f=open(self.file,'r',encoding='utf-8')
        lines=f.readlines()
        f.close()
        file_q=self.path+self.file.replace('.txt','_q.txt')
        file_a=self.path+self.file.replace('.txt','_a.txt')
        if os.path.exists(file_a):
            os.remove(file_a)
        if os.path.exists(file_q):
            os.remove(file_q)
        f_q=open(file_q,'a+',encoding='utf-8')
        f_a=open(file_a,'a+',encoding='utf-8')
        for line in lines:
            if 'Question' in line:
                number=re.findall(r'\d+',str(line))[0]
                f_a.write(number+'.')
            if 'Correct Answer:' not in line:
                f_q.write(line)
            else:
                answer=line.split(':')[1].strip().replace(' ','')
                f_a.write(answer+'\n')
        f_q.close()
        f_a.close()


if __name__ == '__main__':
    app = Modify()
    app.main()
