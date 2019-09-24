print("HelloWorld");
import re
snl = "";
with open('HelloWorld.py') as f:
    while True:
        s=f.readline();
        if(len(s)==0):
            break
        sn=re.sub('\s{2,5}',' '*4,s);
        snl+=sn;
    with open('HelloWorld.py','w') as f:
        f.writelines(snl);
    # w=open("test.py","w");
    # w.write(snl);
    # w.close();
    # print(snl);
