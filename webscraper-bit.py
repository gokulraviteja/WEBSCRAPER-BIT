import os
os.chdir("C:\\Users\\bellapukonda\\Desktop\\newfiles")
from bs4 import  BeautifulSoup
from urllib.request import urlopen
html = urlopen("https://www.bitmesra.ac.in/Show_Faculty_List?cid=1&deptid=140")
soup = BeautifulSoup(html.read(),'html.parser' )
mydivs = soup.findAll("div", {"class": "list-event-item"})
file = open("chem.txt","w") 




images=[]
names=[]
emails=[]
areas=[]
mobno=[]
tds= soup.findAll("td")
temp=0
for i in tds:
    if(temp==3):
        mobno.append(i.contents[0])
        temp=0
    if(temp==2):
        if(len(i.contents)>1):
            if("Contact" in i.contents[1]):
                temp=3
            else:
                mobno.append(0)
                temp=0
        else:
            mobno.append(0)
            temp=0
    if(temp==1):
            temp+=1
    if(len(i.contents)>1):

        if("Email" in i.contents[1]):
            temp=1

temp=0
for i in tds:
    if(temp==1):
        areas.append(i.contents[0])
        temp=0
    if(len(i.contents)>1):
        if("Area of Interest" in i.contents[1]):
            temp=1

qual=[]
temp=0
for i in tds:
    if(temp==1):
        qual.append(i.contents[0])
        temp=0
    if(len(i.contents)>1):
        if("Qualification" in i.contents[1]):
            temp=1
    

for i in mydivs:
    images.append(i.img['src'])
    emails.append(i.a.contents[0])
    names.append(i.h5.b.contents[0])





#print(len(names),len(mobno),len(images))
for i in range(len(images)-len(mobno)):
    mobno.append(0)

for i in range(len(names)):

    a=names[i]
    b=emails[i]
    if(mobno[i]!=0):
        c=mobno[i]
    else:
        c="Not Available"
    d=areas[i]
    e=qual[i]
    g="https://www.bitmesra.ac.in/"
    f=images[i]
    g=g+f
    file.write(' <section>  <div class="container py-3" style="background-color:rgba(255,255,255,0.7);width:50%;margin-left:140px;border-radius:10px;box-shadow:5px 5px rgba(244, 36, 15,0.7);" >   <div class="card"> <div class="row ">          <div class="col-md-4">     <img  style="height: 150px; width:145px" src="    ')
    file.write(g)
    file.write('   "  class= "w-75" >  </div> <div class="col-md-8 px-3" style="margin-left:0 ; padding-left:0">             <div class="card-block px-3">  <h4 class="card-title"> ')
    file.write(a)
    file.write('   </h4> \n <p class="card-text"> <b> Qualifications: </b>')
    file.write(e)
    file.write('  </p> \n  <p class="card-text"> <b> Area of Interest: </b>    ')
    file.write(d)
    file.write('  </p>  <p class="card-text"> <b> Contact: </b>    ')
    file.write(c)
    file.write('  </p>  <p class="card-text"> <b> Email: </b>    ')
    file.write(b)
    file.write('  </p>  </div>   </div>        </div> </div> </div>  </section> <br> <br>  \n')

    
    



file.close()



                               

