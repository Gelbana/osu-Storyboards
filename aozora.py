# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:21:35 2015

@author: Big
"""

import math as maths
import random
class Sprite:
    def __init__(self,image,anchor,ground,filed):
        self._image=image
        self._ground=ground
        self._filed=open(filed,'a')
        self._store_values=[]
        self._anchor=anchor
        self._title='Sprite,{0},{1},\"{2}\",320,240\n'.format(self._ground,self._anchor,self._image)
        self._store_values.append(self._title)

    def move(self,ease,start,end,x,y,z,a):
        self._move=" M,{0},{1},{2},{3},{4},{5},{6}\n".format(ease,start,end,x,y,z,a)
        self._store_values.append(self._move)

    def scale(self,ease,start,end,iscale,nscale):
        self._scale=" S,{0},{1},{2},{3},{4}\n".format(ease,start,end,iscale,nscale)
        self._store_values.append(self._scale)

    def scaleVec(self,ease,start,end,iscalex,iscaley,nscalex,nscaley):
        self._scaleVec=" V,{0},{1},{2},{3},{4},{5},{6}\n".format(ease,start,end,iscalex,iscaley,nscalex,nscaley)
        self._store_values.append(self._scaleVec)

    def fade(self,ease,start,end,ifade,nfade):
        self._fade=" F,{0},{1},{2},{3},{4}\n".format(ease,start,end,ifade,nfade)
        self._store_values.append(self._fade)

    def colour(self,ease,start,end,r,g,b,r1,g1,b1):
        self._colour=" C,{0},{1},{2},{3},{4},{5},{6},{7},{8}\n".format(ease,start,end,r,g,b,r1,g1,b1)
        self._store_values.append(self._colour)

    def rotate(self,ease,start,end,rotate,rotate1):
        self._rotate=" R,{0},{1},{2},{3},{4}\n".format(ease,start,end,rotate,rotate1)
        self._store_values.append(self._rotate)

    def looplyrics(self,start,loopcount,timedif,x,y):
        self._looplyrics=" L,{0},{1}\n  F,0,{2},{3},{4}\n  F,0,{5},{6},{7}\n".format(start,loopcount,timedif,timedif+200,x,timedif+200,timedif+400,y)
        self._store_values.append(self._looplyrics)


    def loopdraw(self,start,loopcount,timedif,x,y,z,a):
        self._loopdraw=" L,{0},{1}\n  M,0,{2},{3},{4},{5},{6},{7}\n  M,0,{8},{9},{10},{11},{12},{13}\n".format(
        start,loopcount,timedif,timedif+200,x,y,x,y,timedif+200,timedif+400,z,a,z,a)

        self._store_values.append(self._loopdraw)
    def end(self):
        for item in self._store_values:
            self._filed.write(item)
        self._filed.close()




output= 'yuiko & Meis Clauson - Aozora Memories (Kinshara).osb'
open(output,"w").close()
out1=open(output,"a")
out1.write("[Events]\nSprite,Background,TopLeft,\"bg.jpg\",0,0\n")
out1.close()

def drawdraw(image,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            if int(line[2])==123 and int(line[3])==108:
                colour.append((26,42,39))
            else:
                colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        if i%4==0:
            c='Break'
            if xlist[i]==c:
                localstart,movestart=start,start

            else:
                xlist[i]=int(xlist[i])
                ylist[i]=int(ylist[i])
                movestart=start
                colourc=colour[i]
                temp=int(localstart)
                rotation=random.random()*2*3.14
                rotation2=random.random()*2*3.14
                xrand=random.randint(-1,0)
                yrand=random.randint(0,1)
                xrand2=random.randint(-1,0)
                yrand2=random.randint(0,1)
                dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
                dot.rotate(0,temp,temp,rotation,rotation)
                dot.scale(0,temp,temp+200,0.06,0.125)
                dot.fade(0,temp,temp,0.7,0.7)
                dot.fade(0,temp,temp,0,0)
                if localstart>=end-2000 and image=="sb/4.txt":
                    dot.fade(0,end-2000,end,0,0)
                else:
                    dot.fade(0,end-2000,end,0.7,0)
                    dot.move(0,temp,end,xlist[i],ylist[i],xlist[i],ylist[i])
                    dot.colour(0,temp,temp,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

                localstart=localstart+pace







                dot.end()

def drawdraw2(image,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            if int(line[2])==123 and int(line[3])==108:
                colour.append((26,42,39))
            else:
                colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        if i%4==0:
            c='Break'
            if xlist[i]==c:
                localstart,movestart=start,start

            else:
                if i==1000 or i==2000 or i==3000 or i==3500:
                    localstart,movestart=start,start
                xlist[i]=int(xlist[i])
                ylist[i]=int(ylist[i])
                movestart=start
                colourc=colour[i]
                temp=int(localstart)
                rotation=random.random()*2*3.14
                rotation2=random.random()*2*3.14
                xrand=random.randint(-1,0)
                yrand=random.randint(0,1)
                xrand2=random.randint(-1,0)
                yrand2=random.randint(0,1)
                dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
                dot.rotate(0,temp,temp,rotation,rotation)
                dot.fade(0,temp,temp+200,0,0.7)
                dot.scale(0,temp,temp+300,0.06,0.125)
                #dot.fade(0,temp,temp,0.24,0.24)
                dot.fade(0,temp,temp,0,0)
                if localstart>=end-2000 and image=="sb/4.txt":
                    dot.fade(0,end-2000,end,0,0)
                else:
                    dot.fade(0,end-2000,end,0.7,0)
                    dot.move(0,temp,end,xlist[i],ylist[i],xlist[i],ylist[i])
                    dot.colour(0,temp,temp,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

                localstart=localstart+pace







                dot.end()

def image(image,start,end,fadestart,x,y,scale,rot):
    image=Sprite("sb\{0}\{1}.png".format("crappy",image),"TopCentre","Foreground",output)
    image.move(0,start,end,x,y,x,y)
    image.fade(0,start,start,0,0)
    image.fade(2,fadestart,end-2000,0,0.7)
    image.scaleVec(0,start,start,scale,scale,scale,scale)
    image.rotate(0,start,start,rot,rot)
    image.scaleVec(0,end,end+270,scale,scale,scale,0)
    image.end()

def image2(image,start,end,fadestart,x,y,scale,rot):
    image=Sprite("sb\{0}\{1}.png".format("crappy",image),"TopCentre","Foreground",output)
    image.move(0,start,end,x,y,x,y)
    image.fade(0,start,start,0,0)
    image.fade(2,fadestart-3000,fadestart,0,0.7)
    image.fade(2,end-2000,end,0.7,0)
    image.scaleVec(0,start,start,scale,scale,scale,scale)
    image.rotate(0,start,start,rot,rot)
    image.scaleVec(0,end,end+300,scale,scale,scale,0)
    image.end()


def bgflip(bgs,start,end):
    x=random.randint(-1,1)
    y=random.randint(-1,1)
    while x==0 or y==0:
       x=random.randint(-1,1)
       y=random.randint(-1,1)


    bg=Sprite("sb\{0}.jpg".format("tex"),"TopCentre","Foreground",output)
    bg.move(0,bgs,start,320,0,320,0)
    bg.move(0,start,end,320,0,320,-00)
    bg.scaleVec(0,bgs,start,x*0.625,y*0.625,x*0.625,y*0.625)
    bg.scaleVec(0,start,end-100,x*0.625,y*0.625,x*0.625,0)
    bg.end()

def bgflip2(bgs,start,end):
    x=random.randint(-1,1)
    y=random.randint(-1,1)
    while x==0 or y==0:
       x=random.randint(-1,1)
       y=random.randint(-1,1)


    bg=Sprite("sb\{0}.jpg".format("tex"),"TopCentre","Foreground",output)
    bg.move(0,bgs,start,320,0,320,0)
    bg.move(0,start,end,320,0,320,-00)
    bg.scaleVec(0,bgs,start,x*0.625,y*0.625,x*0.625,y*0.625)
    bg.colour(2,end-2000,end,255,255,255,0,0,0)
    bg.end()

def bgflip3(bgs,start,end):
    x=random.randint(-1,1)
    y=random.randint(-1,1)
    while x==0 or y==0:
       x=random.randint(-1,1)
       y=random.randint(-1,1)


    bg=Sprite("sb\{0}.jpg".format("tex"),"TopCentre","Foreground",output)
    bg.colour(1,bgs-300,start-100,0,0,0,255,255,255)
    bg.move(0,bgs,start,320,0,320,0)
    bg.move(0,start,end,320,0,320,-00)
    bg.scaleVec(0,bgs,start,x*0.625,y*0.625,x*0.625,y*0.625)
    bg.scaleVec(0,start,end-100,x*0.625,y*0.625,x*0.625,0)
    bg.end()

def pageflip(start,end):
    page=Sprite("sb\{0}.png".format("test"),"BottomCentre","Foreground",output)
    page.scaleVec(8,start,end,0.65,0,0.65,-1)

    page.move(0,start,end,320,450,320,00)
    page.end()


def verse(image1,image2, start, end, x,y,scale,flip):

    name=Sprite("sb\{0}\{1}.png".format("verse",image1),"TopCentre","Foreground",output)
    name2=Sprite("sb\{0}\{1}.png".format("verse",image2),"TopCentre","Foreground",output)

    name.move(0,start,end,x,y,x,y)
    name.scaleVec(0,start,start,scale,scale,scale,scale)
    name2.move(0,start,end,x,y,x,y)
    name2.fade(0,start,start,0,0)
    name2.scaleVec(0,start,start,scale,scale,scale,scale)

    time=end-flip
    ratio=(480-y)/480.0
    ratio2=int(time*ratio)

    loopcount=(flip-start)/400
    starty=(loopcount*400)+start
    offset=flip-starty

    name.looplyrics(start,loopcount,0,1,0)
    name2.looplyrics(start,loopcount,0,0,1)
    name.scaleVec(0,flip,flip+ratio2,scale,scale,scale,0)
    name2.scaleVec(0,flip,flip+ratio2,scale,scale,scale,0)

    name.fade(0,starty,starty,1,1)
    name2.fade(0,starty,starty,0,0)



    name.end()
    name2.end()

def verse2(image1,image2, start, end, x,y,scale,flip):

    name=Sprite("sb\{0}\{1}.png".format("verse",image1),"TopCentre","Foreground",output)
    name2=Sprite("sb\{0}\{1}.png".format("verse",image2),"TopCentre","Foreground",output)

    name.move(0,start,end,x,y,x,y)
    name.scaleVec(0,start,start,scale,scale,scale,scale)
    name2.move(0,start,end,x,y,x,y)
    name2.fade(0,start,start,0,0)
    name2.scaleVec(0,start,start,scale,scale,scale,scale)
    loopcount=(end-start)/400


    name.looplyrics(start,loopcount,0,1,0)
    name2.looplyrics(start,loopcount,0,0,1)
    starty=(loopcount*400)+start

    offset=flip-starty
    name.fade(0,starty,starty,1,1)
    name.fade(0,starty+offset/2,starty+offset/2,0,0)

    name2.fade(0,starty,starty,0,0)
    name2.fade(0,starty+offset/2,starty+offset/2,1,1)

    name.end()
    name2.end()


def names(image1,image2, start, end, x,y,scale,flip):

    name=Sprite("sb\{0}\{1}.png".format("names",image1),"TopCentre","Foreground",output)
    name2=Sprite("sb\{0}\{1}.png".format("names",image2),"TopCentre","Foreground",output)

    name.move(0,start,end,x,y,x,y)
    name.scaleVec(0,start,start,scale,scale,scale,scale)
    name2.move(0,start,end,x,y,x,y)
    name2.fade(0,start,start,0,0)
    name2.scaleVec(0,start,start,scale,scale,scale,scale)
    time=end-flip
    ratio=(480-y)/480.0
    ratio2=int(time*ratio)-50
    name.scaleVec(0,flip,flip+ratio2,scale,scale,scale,0)

    while start<end:
        if start+400>flip:
            offset=end-start
            name.fade(0,start,start,1,1)
            name.fade(0,start+offset,start+offset,0,0)

            start=start+offset
        else:
            name.fade(0,start,start,1,1)
            name.fade(0,start+200,start+200,0,0)
            name2.fade(0,start+200,start+200,1,1)
            name2.fade(0,start+400,start+400,0,0)
            start=start+400

    name.end()
    name2.end()

def drawbase(image,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start

        elif i%2==0:
            localstart=localstart+pace
            continue

        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)
            dot.fade(0,end-200,end,0.6,0)
            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)




            dot.end()




def drawstay(image,start,end, pace, r,g,bb):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start

        elif i%2==0:
            localstart=localstart+pace
            continue

        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.14,0.14)
            dot.fade(0,localstart,localstart,0.5,0.5)
            dot.fade(0,movestart,movestart,0,0)
            dot.fade(0,end-500,end,0.5,0)
            dot.colour(0,localstart,localstart,r,g,bb,r,g,bb)

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            dot.end()

def drawstay2(image,start,end, pace, r,g,bb):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.14,0.14)
            dot.fade(0,localstart-200,localstart,00,0.5)
            dot.fade(0,localstart,localstart,0.5,0.5)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,r,g,bb,r,g,bb)

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace



            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.fade(0,end-500,end,0.4,0)
            dot.end()

def drawyubi(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]
            endreal=end
            endi=end-random.randint(1000,2200)

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+400,0.06,0.16)
            dot.scale(0,endi,endreal+500,0.15,random.randint(-30,30)/100.0)
            dot.fade(0,localstart,localstart,0.54,0.54)
            dot.fade(0,movestart,movestart,0,0)
            dot.fade(0,endi,endi+1500,0.54,0)
            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace
            dot.move(2,endi,endreal+500,xlist[i],ylist[i],random.randint(1000,2000),random.randint(-100,600))


            loopcount=(endi-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)




            loopcount=(end-start)/400



            dot.end()

def drawslowpart(image,nextimage,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(nextimage,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    localstart=start
    sant=[]
    fakeend=end-250


    for i in range(0,len(x2list)):

        sant.append(i)

    for i in range(0,len(xlist)):


        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            movestart=start
            colourc=colour[i]

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

          #      if xlist[i]<initialx:
          #          dot.move(0,movestart,movestart+100,xlist[i]+randint(100,200),ylist[i]+rand(-200,200),xlist[i],ylist[i])




            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(0,1)
            yrand=random.randint(-1,0)
            xrand2=random.randint(0,1)
            yrand2=random.randint(-1,0)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.145,0.1450)
            dot.fade(0,localstart,localstart,0.55,0.55)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace



            loopcount=((fakeend-start)/400 )
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=fakeend-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+offset/2,fakeend,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)



            if i>len(x2list):
                doo=random.randint(0,len(x2list)-1)

                dot.move(5,fakeend,end,xlist[i],ylist[i],int(x2list[doo]),int(y2list[doo]))

               # sant.remove(doo)



            dot.end()
    for i in sant:
        c='Break'
        b=sant.index(i)

        a=random.randint(0,len(xlist)-1)
        if xlist[a]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

            dot.rotate(0,fakeend,fakeend,rotation,rotation)
            dot.scale(0,fakeend,fakeend,0.144,0.1440)
            dot.fade(0,fakeend,fakeend,0.55,0.55)

            dot.colour(0,fakeend,fakeend,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            dot.move(5,fakeend,end,int(xlist[a]),int(ylist[a]),int(x2list[b]),int(y2list[b]))

            dot.end()

def drawslowpart3(image,nextimage,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(nextimage,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    localstart=start
    sant=[]
    fakeend=end-250


    for i in range(0,len(x2list)):
        sant.append(i)

    for i in range(0,len(xlist)):


        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            movestart=start
            colourc=colour[i]

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

          #      if xlist[i]<initialx:
          #          dot.move(0,movestart,movestart+100,xlist[i]+randint(100,200),ylist[i]+rand(-200,200),xlist[i],ylist[i])




            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(0,1)
            yrand=random.randint(-1,0)
            xrand2=random.randint(0,1)
            yrand2=random.randint(-1,0)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.145,0.1450)
            dot.fade(0,localstart,localstart,0.55,0.55)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace




            dot.move(0,start,fakeend,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)




            if i>len(x2list):
                doo=random.randint(0,len(x2list)-1)

                dot.move(5,fakeend,end,xlist[i],ylist[i],int(x2list[doo]),int(y2list[doo]))

               # sant.remove(doo)



            dot.end()
    for i in sant:
        c='Break'
        b=sant.index(i)

        a=random.randint(0,len(xlist)-1)
        if xlist[a]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

            dot.rotate(0,fakeend,fakeend,rotation,rotation)
            dot.scale(0,fakeend,fakeend,0.145,0.145)
            dot.fade(0,fakeend,fakeend,0.55,0.55)

            dot.colour(0,fakeend,fakeend,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            dot.move(5,fakeend,end,int(xlist[a]),int(ylist[a]),int(x2list[b]),int(y2list[b]))

            dot.end()


def drawslowpart2(image,nextimage,start,end, pace ,r,g,bb , offset):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(nextimage,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    localstart=start
    sant=[]
    fakeend=offset


    for i in range(0,len(x2list)):
        sant.append(i)

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            movestart=start
            colourc=colour[i]
            initialx=130
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

          #      if xlist[i]<initialx:
          #          dot.move(0,movestart,movestart+100,xlist[i]+randint(100,200),ylist[i]+rand(-200,200),xlist[i],ylist[i])




            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(0,1)
            yrand=random.randint(-1,0)
            xrand2=random.randint(0,1)
            yrand2=random.randint(-1,0)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.145,0.1450)
            dot.fade(0,localstart,localstart,0.55,0.55)

            dot.colour(0,localstart,localstart,r,g,bb,r,g,bb)

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace


            while movestart<fakeend:
                if movestart+400>fakeend:
                    offset=(fakeend-movestart)

                    dot.move(0,movestart,movestart+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
                    dot.move(0,movestart+offset/2,fakeend,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)

                    movestart=movestart+offset
                else:
                    dot.move(0,movestart,movestart+200,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
                    dot.move(0,movestart+200,movestart+400,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)
                    movestart=movestart+400



            if i>len(x2list):
                doo=random.randint(0,len(x2list)-1)
                do=sant.index(doo)
                dot.move(1,fakeend,end,xlist[i],ylist[i],int(x2list[doo]),int(y2list[doo]))

               # sant.remove(doo)



            dot.end()
    for i in sant:

        b=sant.index(i)

        a=random.randint(0,len(xlist)-1)
        dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

        dot.rotate(0,fakeend,fakeend,rotation,rotation)
        dot.scale(0,fakeend,fakeend,0.145,0.145)
        dot.fade(0,fakeend,fakeend,0.55,0.55)

        dot.colour(0,fakeend,fakeend,r,g,bb,r,g,bb)
        dot.move(1,fakeend,end,int(xlist[a]),int(ylist[a]),int(x2list[b]),int(y2list[b]))

        dot.end()



def follow(image,start,end):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()


    for i in range(0,300):

        xlist[i]=int(xlist[i])
        ylist[i]=int(ylist[i])
        localstart=start
        dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
        rotation=random.random()*2*3.14
        dot.rotate(0,localstart,localstart,rotation,rotation)
        dot.scale(0,localstart,localstart,0.2,0.2)
       # dot.colour(0,localstart,localstart,colour[i][0],colour[i][1],colour[i][2])
        for i in range(0,len(xlist)):
            if i%2==0:
                continue
            dot.move(1,localstart,localstart+10,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+10
        dot.end()
        start=start+3


def drawweird(image,image2,image3,start,end1,end2,end3,pace,pace2):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]
    x3list=[]
    y3list=[]
    colour3=[]
    a=0
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(image2,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    z=open(image3,'r')
    for line in z:

       line=line.split(',')
       if line[0]=='\n':
           pass

       else:
           x3list.append(line[0])
           y3list.append(line[1])
           colour3.append((line[2],line[3],int(line[4])))
    z.close()


    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            movestart=start
            colourc=colour[i]
            end=end1
            off=random.randint(-500,500)
            end=end+off
            j=int(a)
            xfollow,yfollow=random.randint(-1*j,j),random.randint(-1*j,j)

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart-200,localstart,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)


            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

           # while end<end2:
            count=0
            for k in range(0,len(x2list)-1):

                if k==0:

                    dot.move(2,end,end+200,xlist[i]+xrand2,ylist[i]+yrand2,int(x2list[k+1])+xfollow,int(y2list[k+1])+yfollow)
                    end=end+200
                else:
                    dot.move(0,end,end+pace2,int(x2list[k])+xfollow,int(y2list[k])+yfollow,int(x2list[k+1])+xfollow,int(y2list[k+1])+yfollow)
                    end=end+pace2
                count+=1

            a+=0.05
            randx=random.randint(-300,300)
            randy=random.randint(-300,300)

            if i<len(x3list)-1:

                while (randx)**2 + (randy)**2 > 200**2:
                    randx=random.randint(-200,200)
                    randy=random.randint(-200,200)
                loopcount2=((end3-(end+200))/400)
                dot.move(0,end,end+200,int(x2list[len(x2list)-1])+xfollow,int(y2list[len(x2list)-1])+yfollow,int(x3list[i])+xrand,int(y3list[i])+yrand)
                dot.loopdraw(end,loopcount2,400-off,int(x3list[i])+xrand2,int(y3list[i])+yrand2,int(x3list[i])+xrand,int(y3list[i])+yrand)

                dot.move(1,end3,end3+900,int(x3list[i])+xrand,int(y3list[i])+yrand,int(x3list[i])+randx,int(y3list[i])+randy)
                dot.fade(2,end3,end3+random.randint(50,500),0.6,0)
            #    rr,gg,bb=random.randint(0,255),random.randint(0,255),random.randint(0,255)
            #    dot.colour(0,end3+00,end3+200,0,0,0,rr,gg,bb)


            else:
                fr=random.randint(0,len(x3list)-1)
                dot.move(0,end,end+200,int(x2list[len(x2list)-1])+xfollow,int(y2list[len(x2list)-1])+yfollow,int(x3list[fr]),int(y3list[fr]))





            dot.end()



def drawexplode(image,image2,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass

        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            randx=random.randint(-200,200)
            randy=random.randint(-200,200)
            while (randx)**2 + (randy)**2 > 200**2:
                randx=random.randint(-200,200)
                randy=random.randint(-200,200)
            dot.move(1,end,end+900,int(xlist[i])+xrand,int(ylist[i])+yrand,int(xlist[i])+randx,int(ylist[i])+randy)
            dot.fade(2,end,end+random.randint(50,500),0.6,0)
           # rr,gg,bb=random.randint(0,255),random.randint(0,255),random.randint(0,255)
         #   dot.colour(0,end+00,end+200,0,0,0,rr,gg,bb)
            dot.end()




def drawin(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            off=random.randint(-300,100)
            offs=random.randint(-100,400)
            movestart=start+off
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            colourc=colour[i]
            randx=random.randint(-300,300)
            randy=random.randint(-300,300)
            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,movestart,movestart,rotation,rotation)
            dot.scale(0,movestart,movestart+200,0.18,0.16)

            dot.fade(0,movestart-400,movestart,0,0.6)
            dot.fade(0,end-200,end+00,0.6,0)
            dot.move(1,movestart-500,movestart+offs,xlist[i]+randx,ylist[i]+randy,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.colour(0,movestart,movestart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            movestart=movestart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount+1,0-off,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            dot.end()


def spiral(image,image2,start,end,pace,shift,sec):

    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]
    k=0
    x=open(image,'r')
    pp=0
    for line in x:
        line=line.split(',')
        if line[0]=='\n':
            pass
        elif pp==1:
            pp=0
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
            pp=pp+1
    x.close()
    hh=0
    y=open(image2,'r')
    for line in y:
        line=line.split(',')
        if line[0]=='\n':
            pass
        elif hh==1:
            hh=0
            pass
        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
            hh=hh+1
    y.close()

    it=sec

    xxlist=[]
    yylist=[]
    xx2list=[]
    yy2list=[]
    while it<len(xlist):
        xxlist.append(xlist[it])
        yylist.append(ylist[it])
        it+=3
    il=sec

    while il<len(x2list):
        xx2list.append(x2list[il])
        yy2list.append(y2list[il])
        il+=3

    movestart=start
    period=0.01

    offsety=240
    xd=-107
    xx2list1=xx2list[:int(len(xx2list)*0.640522875817)]
    xx2list2=xx2list[int(len(xx2list)*0.640522875817):]
    yy2list1=yy2list[:int(len(yy2list)*0.640522875817)]
    yy2list2=yy2list[int(len(yy2list)*0.640522875817):]
    print len(xx2list1),len(xx2list2)
    while xd<854:
        xd+=1.1
        xrand=random.randint(-1,0)
        yrand=random.randint(0,1)
        xrand2=random.randint(-1,0)
        yrand2=random.randint(0,1)


        rotation=random.random()*2*3.14
        randy=random.randint(-15,15)
        randx=random.randint(-10,10)
        x=int(xd)
        if k==1:
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.scale(0,movestart,movestart,0.15,0.15)
            dot.colour(0,movestart,movestart,0,0,0,0,0,0)
            dot.fade(0,movestart,movestart+100,0,0.7)
            dot.rotate(0,movestart,movestart,rotation,rotation)

            y=60*maths.sin((period*x)-shift)+offsety
            dot.move(1,movestart,movestart+1000,x,y,x+randx,y+randy)
            dot.fade(0,movestart+600,movestart+980,0.7,0)
            dot.end()
            k=0
        else:
            k=k+1

        count=0
        t=0


        for li in xxlist:

            if int(li)==x:
                yylist[count]=int(yylist[count])
                rand=random.randint(0,400)
                tth=0
                dot2=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
                dot2.scale(0,movestart,movestart,0.15,0.15)
                dot2.colour(0,movestart,movestart,0,0,0,0,0,0)
                dot2.fade(0,movestart+rand,movestart+100+rand,0,0.6)
                dot2.rotate(0,movestart,movestart,rotation,rotation)
                dot2.move(1,movestart+rand,movestart+1200+rand,x,y,int(li),yylist[count])
                #dot2.move(1,movestart+1200+rand,67646,int(li),yylist[count],int(li),yylist[count])

                start=movestart+1200+rand
                loopcount=(67646-start)/400
                dot2.loopdraw(start,loopcount,0-(start%200),int(li)+xrand2,yylist[count]+yrand2,int(li)+xrand,yylist[count]+yrand)
                starty=(loopcount*400)+start-(start%400)
                offset=67646-starty
                dot2.move(0,starty,starty+offset/2,int(li)+xrand2,yylist[count]+yrand2,int(li)+xrand2,yylist[count]+yrand2)
                dot2.move(0,starty+offset/2,67646,int(li)+xrand,yylist[count]+yrand,int(li)+xrand,yylist[count]+yrand)

                startt=67646
                end=68352
                inter=(end-startt)/20

                x1=int(li)
                y1=yylist[count]


                if len(xx2list2)>0 and x<320:
                    endrand=random.randint(0,len(xx2list2)-1)
                    endx=int(xx2list2[endrand])
                    endy=int(yy2list2[endrand])
                    del xx2list2[endrand]
                    del yy2list2[endrand]
                    #print len(xx2list2)

                elif len(xx2list1)>0 and x>320:
                    endrand=random.randint(0,(len(xx2list1)-1))
                    endx=int(xx2list1[endrand])
                    endy=int(yy2list1[endrand])
                    del xx2list1[endrand]
                    del yy2list1[endrand]


                else:
                    endrand=random.randint(0,len(x2list)-1)
                    endx=int(x2list[endrand])
                    endy=int(y2list[endrand])
                    tth=1


                radius=(x1-320)**2 + (y1-240)**2
                radius2=(endx-320)**2 + (endy-240)**2




                radius=maths.sqrt(radius)
                radius2=maths.sqrt(radius2)
                raddif=(radius-radius2)/20.0
                if x>320:
                    angle=maths.atan((y1-240)/(x1-320.0))
                    endangle=maths.atan((endy-240)/(endx-320.0))+(maths.pi*3)
                else:
                    angle=maths.atan((y1-240)/(x1-320.01))+maths.pi
                    endangle=maths.atan((endy-240)/(endx-320.0))+(maths.pi*4)

                angledif=(angle-endangle)/20.0
                while startt<end:

                    x2=int(320+(radius*maths.cos(angle)))
                    y2=int(240+(radius*maths.sin(angle)))
                    dot2.move(0,startt,startt+inter,x1,y1,x2,y2)



                    startt=startt+inter
                    angle=angle-angledif
                    x1=x2
                    y1=y2
                    radius=radius-raddif





                xx=int(320+ (-1*13*(12*maths.sin(t)-4*maths.sin(3*t))))
                yy=int(200+ (-1*13*(13*maths.cos(t)-5*maths.cos(2*t)-2*maths.cos(3*t))))

                if xx>320 and yy>240:
                    randdx=random.randint(0,20)
                    randdy=random.randint(0,20)

                elif xx>320 and yy<240:
                    randdx=random.randint(0,20)
                    randdy=random.randint(-20,0)

                elif xx<320 and yy>240:
                    randdx=random.randint(-20,0)
                    randdy=random.randint(0,20)

                else:
                    randdx=random.randint(-20,0)
                    randdy=random.randint(-20,0)

                if tth==1:

                    dot2.fade(0,startt-400,startt-50,0.6,0)
                    dot2.end()
                else:
                    dot2.move(0,end,69058,endx,endy,endx,endy)
                    dot2.fade(0,69058+2500,69058+3200,0.6,0)
                    dot2.colour(0,69058,69058+700,0,0,0,255,0,0)
                    dot2.move(19,69058,69058+3000,endx,endy,xx+randdx,yy+randdy)
                    dot2.end()
            count+=1
            t+=0.8


        movestart=movestart+pace



def drawitsu(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start
    jumble = [112823,112999,113352,113529,113646,113764,113882,113999,114117]
    x2=-100000
    y2=-1000000
    jump=[-1,1]
    jumpy=jump[random.randint(0,1)]
    #random.shuffle(jumble)

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

            if 0<i<72 or i>1359:
                end=0
            elif 72<i<144 or 1287 < i < 1359:
                end=1
            elif 144<i<216 or 1215<i<1287:
                end=2
            elif 216<i<288 or 1143<i<1215:
                end=3
            elif 288<i<360 or 1215<i<1143:
                end=4
            elif 360<i<432 or 1143<i<1215:
                end=5
            elif 432<i<504 or 999<i<1143:
                end=6
            elif 504<i<576 or  927<i<999:
                end=7
            elif 576<i<927:
                end=8
            else:
                end=0
                dot.scale(0,jumble[end],jumble[end],0,0)


            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]
            endi=jumble[end]


            rotation=random.random()*2*3.14

            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)

            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)
            dot.fade(0,endi,endi+140,0.6,0)
            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace
            dot.move(2,endi,endi+200,xlist[i],ylist[i],xlist[i]+100,ylist[i]+100)


            loopcount=(endi-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            if abs(xlist[i]-x2)<2:
                x2=x2+random.randint(-3,3)
                y2=y2+random.randint(-3,3)
                dot.move(1,endi,endi+200,xlist[i],ylist[i],x2,y2)

            else:

                radx=random.randint(-100,100)
                rady=random.randint(-100,100)
                dot.move(1,endi,endi+200,xlist[i],ylist[i],xlist[i]+radx,ylist[i]+rady)
                x2=xlist[i]+radx
                y2=ylist[i]+rady







            dot.end()

def drawline(image,image2,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(image2,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace

            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=end-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            if i<len(x2list):
                e=len(x2list)-i-1
                x2list[e]=int(x2list[e])
                y2list[e]=int(y2list[e])
                dot.move(17,end,119882,xlist[i]+xrand,ylist[i]+yrand,x2list[e]+xrand2,y2list[e]+yrand2)
            else:
                e=len(x2list)-i+200
                x2list[e]=int(x2list[e])
                y2list[e]=int(y2list[e])
                dot.move(17,end,119882,xlist[i]+xrand,ylist[i]+yrand,x2list[e]+xrand2,y2list[e]+yrand2)
                dot.fade(0,119882-200,119882,0.6,0)

            x2list[e]=int(x2list[e])
            y2list[e]=int(y2list[e])


            loopcount=(124823-119882)/400
            dot.loopdraw(119882,loopcount,0,x2list[e]+xrand2,y2list[e]+yrand2,x2list[e]+xrand,y2list[e]+yrand)

            starty=(loopcount*400)+119882
            offset=124823-starty
            dot.move(0,starty,starty+offset/2,x2list[e]+xrand2,y2list[e]+yrand2,x2list[e]+xrand,y2list[e]+yrand)
            dot.move(0,starty+offset/2,124823,x2list[e]+xrand,y2list[e]+yrand,x2list[e]+xrand2,y2list[e]+yrand2)


            randx=random.randint(-200,200)
            randy=random.randint(-200,200)
            while (randx)^2 + (randy)^2 > 200^2:
                randx=random.randint(-200,200)
                randy=random.randint(-200,200)
            dot.move(1,124823,124823+900,int(x2list[e])+xrand,int(y2list[e])+yrand,int(x2list[e])+randx,int(y2list[e])+randy)
            dot.fade(2,124823,124823+random.randint(50,500),0.6,0)
            dot.end()


def guitarr(image,start,end, r,g,b,enterx,entery,endspeed,sec,orix,oriy):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start
    list1=[]
    i=0
    while i<len(xlist):
        list1.append(i)
        i+=1


    for i in range((len(xlist)*(sec-1)/6),((len(xlist)*sec/6)-1)):
        rotation=random.random()*2*3.14
        xrand=random.randint(-1,0)
        yrand=random.randint(0,1)
        xrand2=random.randint(-1,0)
        yrand2=random.randint(0,1)
        xlist[i]=int(xlist[i])
        ylist[i]=int(ylist[i])
        dot2=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
        dot2.rotate(0,localstart,localstart,rotation,rotation)
        dot2.scale(0,localstart,localstart+200,0.15,0.15)
        dot2.fade(0,localstart-300,localstart-300,0,0)
        dot2.fade(0,localstart,localstart,0.4,0.4)
        #dot2.move(0,start,end,xlist[i],ylist[i],xlist[i],ylist[i])
        dot2.colour(0,localstart,localstart,0,0,0,0,0,0)
        dot2.fade(0,end-200,end,0.4,0.0)

        loopcount=(end-start)/400
        dot2.loopdraw(start,loopcount+1,0-(start%200),xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


        starty=(loopcount*400)+start
        offset=end-starty
        dot2.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
        dot2.move(0,starty+offset/2,end,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)
        dot2.end()

    for i in range(0,100):

        rotation=random.random()*2*3.14
        rotation2=random.random()*2*3.14
        dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
        dot.rotate(0,localstart,localstart,rotation,rotation)
        dot.scale(0,localstart,localstart+200,0.15,0.15)
        dot.fade(0,localstart-endspeed*1/2,localstart,0,0.7)


        dot.colour(0,localstart-endspeed,localstart,0,0,255,255,0,0)
        dot.colour(0,localstart,localstart+endspeed*4/5,255,0,0,0,0,255)



        randx=random.randint(-15,15)
        randy=random.randint(-15,15)
        while (randx)**2 + (randy)**2 > 15**2:
            randx=random.randint(-15,15)
            randy=random.randint(-15,15)

        m=(oriy*1.0-entery)/(orix*1.0-enterx)
        c=oriy-(m*orix)

        y=m*(orix+(orix-enterx))+c
        x=(orix+(orix-enterx))


        dot.move(2,start-endspeed/2,start,enterx+randx,entery+randy,orix+randx,oriy+randy)
        rx=random.randint(-100,100)
        ry=random.randint(-100,100)
        while (rx)**2 + (ry)**2 > 100**2:
            rx=random.randint(-100,100)
            ry=random.randint(-100,100)
        dot.move(1,start,start+endspeed,orix+randx,oriy+randy,x+rx,y+ry)
        dot.fade(0,start+endspeed/2,start+endspeed*4/5,0.7,0)


        dot.end()

def spiral2(image,image2,start,end,pace,shift,sec):

    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]
    k=0
    hh=0
    x=open(image,'r')
    for line in x:
        line=line.split(',')
        if line[0]=='\n':
            pass
        elif hh==1:
            hh=0
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
            hh=hh+1
    x.close()
    pp=0
    y=open(image2,'r')
    for line in y:
        line=line.split(',')
        if line[0]=='\n':
            pass
        elif pp==1:
            pp=0
            pass
        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
            pp=pp+1
    y.close()

    it=sec

    xxlist=[]
    yylist=[]
    xx2list=[]
    yy2list=[]
    while it<len(xlist):
        xxlist.append(xlist[it])
        yylist.append(ylist[it])
        it+=3
    il=sec

    while il<len(x2list):
        xx2list.append(x2list[il])
        yy2list.append(y2list[il])
        il+=3

    movestart=start
    period=0.01

    offsety=240
    xd=-107
    xx2list1=xx2list[:int(len(xx2list)*0.678010471204)]
    xx2list2=xx2list[int(len(xx2list)*0.678010471204):]
    yy2list1=yy2list[:int(len(yy2list)*0.678010471204)]
    yy2list2=yy2list[int(len(yy2list)*0.678010471204):]
    while xd<854:
        xd+=1.1
        xrand=random.randint(-1,0)
        yrand=random.randint(0,1)
        xrand2=random.randint(-1,0)
        yrand2=random.randint(0,1)


        rotation=random.random()*2*3.14
        randy=random.randint(-15,15)
        randx=random.randint(-10,10)
        x=int(xd)
        if k==1:
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.scale(0,movestart,movestart,0.15,0.15)
            dot.colour(0,movestart,movestart,0,0,0,0,0,0)
            dot.fade(0,movestart,movestart+100,0,0.6)
            dot.rotate(0,movestart,movestart,rotation,rotation)

            y=60*maths.sin((period*x)-shift)+offsety
            dot.move(1,movestart,movestart+1000,x,y,x+randx,y+randy)
            dot.fade(0,movestart+600,movestart+980,0.6,0)
            dot.end()
            k=0
        else:
            k=k+1

        count=0
        t=0
        for li in xxlist:

            if int(li)==x:
                yylist[count]=int(yylist[count])
                rand=random.randint(0,400)
                dot2=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
                dot2.scale(0,movestart,movestart,0.15,0.15)
                dot2.colour(0,movestart,movestart,0,0,0,0,0,0)
                dot2.fade(0,movestart+rand,movestart+100+rand,0,0.6)
                dot2.rotate(0,movestart,movestart,rotation,rotation)
                dot2.move(1,movestart+rand,movestart+1200+rand,x,y,int(li),yylist[count])
                #dot2.move(1,movestart+1200+rand,67646,int(li),yylist[count],int(li),yylist[count])

                start=movestart+1200+rand
                loopcount=(135411-start)/400
                dot2.loopdraw(start,loopcount,0-(start%200),int(li)+xrand2,yylist[count]+yrand2,int(li)+xrand,yylist[count]+yrand)
                starty=(loopcount*400)+start-(start%400)
                offset=135411-starty
                dot2.move(0,starty,starty+offset/2,int(li)+xrand2,yylist[count]+yrand2,int(li)+xrand2,yylist[count]+yrand2)
                dot2.move(0,starty+offset/2,135411,int(li)+xrand,yylist[count]+yrand,int(li)+xrand,yylist[count]+yrand)

                startt=135411
                end=136117
                inter=(end-startt)/20
                balh=0
                x1=int(li)
                y1=yylist[count]

                if len(xx2list1)>0 and x>320:
                    endrand=random.randint(0,(len(xx2list1)-1))
                    endx=int(xx2list1[endrand])
                    endy=int(yy2list1[endrand])
                    xx2list1.pop(endrand)
                    yy2list1.pop(endrand)

                elif len(xx2list2)>0 and x<320:
                    endrand=random.randint(0,len(xx2list2)-1)
                    endx=int(xx2list2[endrand])
                    endy=int(yy2list2[endrand])
                    xx2list2.pop(endrand)
                    yy2list2.pop(endrand)

                else:
                    endrand=random.randint(0,len(x2list)-1)
                    endx=int(x2list[endrand])
                    endy=int(y2list[endrand])
                    dot2.fade(0,end-500,end,0.4,0)
                    balh=1

                radius=(x1-320)**2 + (y1-240)**2
                radius2=(endx-320)**2 + (endy-240)**2



                radius=maths.sqrt(radius)
                radius2=maths.sqrt(radius2)
                raddif=(radius-radius2)/20.0
                if x>320:
                    angle=maths.atan((y1-240)/(x1-320.0))
                    endangle=maths.atan((endy-240)/(endx-320.0))+(maths.pi*3)
                else:
                    angle=maths.atan((y1-240)/(x1-320.01))+maths.pi
                    endangle=maths.atan((endy-240)/(endx-320.0))+maths.pi+(maths.pi*3)

                angledif=(angle-endangle)/20.0
                while startt<end:

                    x2=int(320+(radius*maths.cos(angle)))
                    y2=int(240+(radius*maths.sin(angle)))
                    dot2.move(0,startt,startt+inter,x1,y1,x2,y2)



                    startt=startt+inter
                    angle=angle-angledif
                    x1=x2
                    y1=y2
                    radius=radius-raddif

                dot2.move(0,end,136823,endx,endy,endx,endy)
                #dot2.fade(0,end-50,end,0.4,0)


                xx=random.randint(-107,854)

                yy=random.randint(0,130)

                if xx>320 and yy>240:
                    randdx=random.randint(0,60)
                    randdy=random.randint(0,60)

                if xx>320 and yy<240:
                    randdx=random.randint(0,60)
                    randdy=random.randint(-60,0)

                if xx<320 and yy>240:
                    randdx=random.randint(-60,0)
                    randdy=random.randint(0,60)

                if xx<320 and yy<240:
                    randdx=random.randint(-60,0)
                    randdy=random.randint(-60,0)
                dot2.colour(0,136823,136823+700,0,0,0,0,0200,150)
                dot2.move(19,136823,136823+4000,endx,endy,xx+randdx,yy+randdy)
                if balh==1:
                    balh=0
                else:
                    dot2.fade(0,136823+1500,136823+3000,0.6,0)
                dot2.end()
            count+=1
            t+=1


        movestart=movestart+pace

bgflip2(170352,213058,213058)



bgflip(147764,170352,170705)
#ddd
pageflip(170352,170705)


bgflip(108235,147764,148117)
  #dddd
pageflip(147764,148117)



#bgflip(108235,113882,114235)
#dddd


bgflip(102588,108235,108588)
  #ddddd
pageflip(108235,108588)

verse("verse19-1","verse19-2",103646,108588,640,100,0.34,108235)
verse("verse20-1","verse20-2",106117,108588,0,100,0.35,108235)

bgflip(91293,102588,102941)
  #dddddd


image("5",91646,102588,96588,314,65,0.53,0.0)
drawdraw("sb/5.txt",91646,100588,6)
verse("verse17-1","verse17-2",97293 ,102941,640,100,0.28,102588)
verse("verse18-1","verse18-2",100117,102941,0,100,0.28,102588)

verse2("verse15-1","verse15-2",91293,97293,640,100,0.25,96941)
verse2("verse16-1","verse16-2",94470,97293,0,100,0.25,96941)
bgflip(79999,91293,91646)
pageflip(102588,102941)
#ddddddddddddddddddddddddddddddddd

image("4",80352,91293,83500,328,40,0.56,0.0)
drawdraw("sb/4.txt",80352,88823,3.10)

verse("verse13-1","verse13-2",85999 ,91646,640,100,0.28,91293)
verse("verse14-1","verse14-2",88823,91646,0,100,0.32,91293)

verse2("verse11-1","verse11-2",79999,85999,640,100,0.25,85646)
verse2("verse12-1","verse12-2",83176,85999,0,100,0.25,85646)
bgflip(46117,79999,80352)

pageflip(91293,91646)



pageflip(79999,80352)

bgflip(40470,46117,46470)
#verse("verse11-1","verse11-2",41529,45764,320,200,0.35,46117)
pageflip(46117,46470)


bgflip(34823,40470,40823)

verse("verse9-1","verse9-2",35882,40823,640,100,0.25,40470)
verse("verse10-1","verse10-2",38352,40823,0,100,0.25,40470)
pageflip(40470,40823)

bgflip(12235,34823,23882)

verse("verse7-1","verse7-2",29529,35176,640,100,0.25,34823)
verse("verse8-1","verse8-2",32352,35176,0,100,0.25,34823)
image("2",23882,34823,28529,315,80,0.57,0.0)
drawdraw("sb/2.txt",23882,33823,9)
pageflip(34823,35176)

image("1",12588,23529,17802,323,69,0.51,0.05)
drawdraw("sb/1.txt",12802,21941,6)

verse2("verse5-1","verse5-2",23529,29529,640,100,0.25,29176)
verse2("verse6-1","verse6-2",26705,29529,0,100,0.25,29176)



verse("verse3-1","verse3-2",18235,23882,640,100,0.25,23529)
verse("verse4-1","verse4-2",21058,23882,0,100,0.25,23529)

verse2("verse1-1","verse1-2",12235,18235,640,100,0.25,17882)
verse2("verse2-1","verse2-2",15411,18235,0,100,0.25,17882)
pageflip(23529,23882)

bgflip(6588,12235,12588)

names("kocari1","kocari2",6588,12588,160,110,0.3,12235)
names("kibbleru1","kibbleru2",6588,12588,480,110,0.3,12235)
names("vincent1","vincent2",6588,12588,160,220,0.3,12235)
names("zan1","zan2",6588,12588,480,220,0.3,12235)
names("rei1","rei2",6588,12588,320,320,0.3,12235)
pageflip(12235,12588)

bgflip(941,6588,6941)
names("kinshara1","kinshara2",941,6941,500,340,0.4,6588)
names("title1","title2",941,6941,300,80,0.4,6588)
pageflip(6588,6941)

bgflip3(0,941,1294)
pageflip(941,1294)

""
drawitsu('sb/pre2chorus.txt',108588,45764,4)
#drawbase('sb/test.txt',12588,23529,5)
drawyubi('sb/yubi.txt',40823,45764,4)
drawbase('sb/futari.txt',46470,50352,2)
drawbase('sb/sukoshiii.txt',47352,50352,2)
drawbase('sb/chorus3.txt',48058,50352,3)
#follow('sb/sss.txt',10823,45764)

#drawbase('sb/kocari.txt',80352,91293,5)
drawbase('sb/2chorus1.txt',114235,119529,3)
drawbase('sb/2chorus2.txt',114941,119529,2)
drawline('sb/2chorus3.txt','sb/2chorus5.txt',115999,119176,2)
drawbase('sb/2chorus4.txt',117764,119529,2)
drawexplode('sb/2chorus6.txt','sb/2chorus6.txt',120588,125176, 2)
drawexplode('sb/2chorus7.txt','sb/2chorus6.txt',121646,125352, 3)
drawexplode('sb/2chorus8.txt','sb/2chorus6.txt',123411,124999, 3)
drawbase('sb/2chorus11.txt',127293,130470,3)
drawbase('sb/2chorus12.txt',129323,130470,3)

drawslowpart('sb/kaze.txt','sb/kimi.txt',148117,149176,0)
drawslowpart('sb/kimi.txt','sb/ino.txt',149176,150235,0)
drawslowpart('sb/ino.txt','sb/kaku.txt',150235,151999,0)
drawslowpart('sb/kaku.txt','sb/sukoshi.txt',151999,153764,0)
drawslowpart('sb/sukoshi.txt','sb/sekai.txt',153764,154823,0)
drawslowpart('sb/sekai.txt','sb/ga.txt',154823,155882,0)
drawslowpart3('sb/ga.txt','sb/ugo.txt',155882,156235,0)
drawslowpart('sb/ugo.txt','sb/shun.txt',156235,157646,0)
drawslowpart('sb/shun.txt','sb/fui.txt',157646,159411,0)
drawslowpart('sb/fui.txt','sb/fure.txt',159411,160470,0)
drawslowpart('sb/fure.txt','sb/megu.txt',160470,161529,0)
drawslowpart('sb/megu.txt','sb/futa.txt',161529,163293,0)
drawslowpart('sb/futa.txt','sb/ima.txt',163293,164705,0)
drawstay('sb/ima.txt',164645,165411,0,0,0,0)

drawslowpart2('sb/usu.txt','sb/beni.txt',165764,166470,0,0,0,0,165764)
drawstay2('sb/usu.txt',165764,170352,0,0,0,0)
drawstay('sb/beni.txt',166470,170352,0,0,0,0)
drawstay('sb/iro.txt',167176,170352,0,0,0,0)
drawstay('sb/ni.txt',167882,170352,0,0,0,0)
drawstay('sb/shi.txt',168588,170352,0,0,0,0)
drawstay('sb/ta.txt',169203,170352,0,0,0,0)

drawslowpart2('sb/beni.txt','sb/iro.txt',166470,167176,0,0,0,0,166470)
drawslowpart2('sb/iro.txt','sb/ni.txt',167176,167882,0,0,0,0,167176)
drawslowpart2('sb/ni.txt','sb/shi.txt',167882,168588,0,0,0,0,167882)
drawslowpart2('sb/shi.txt','sb/ta.txt',168588,169293,0,0,0,0,168588)

spiral("sb/chorus14.txt","sb/chorus15.txt",63411,67646,3,320,1)
spiral("sb/chorus14.txt","sb/chorus15.txt",63411,67646,3,230,2)
spiral("sb/chorus14.txt","sb/chorus15.txt",63411,67646,3,140,3)

spiral2("sb/2chorus14.txt","sb/2chorus15.txt",131176,135411,3,320,1)
spiral2("sb/2chorus14.txt","sb/2chorus15.txt",131176,135411,3,230,2)
spiral2("sb/2chorus14.txt","sb/2chorus15.txt",131176,135411,3,140,3)

drawweird("sb/chorus4.txt","sb/trail.txt",'sb/chorus5.txt',50352,51411,52117,57058,0,15)
drawexplode('sb/chorus6.txt','sb/chorus6.txt',52823,57411,2)
drawexplode('sb/chorus7.txt','sb/chorus6.txt',53882,57588,2)
drawexplode('sb/chorus8.txt','sb/chorus6.txt',55646,57235,2)
drawin('sb/chorus9.txt',57764,63588,0)
drawin('sb/chorus10.txt',58823,63588,0)
drawbase('sb/chorus11.txt',59705,63588,2)
drawbase('sb/chorus12.txt',61426,63588,4)
drawbase('sb/chorus13.txt',62705,63588,2)

drawin('sb/chorus9.txt',125529,130470,0)
drawin('sb/chorus10.txt',126588,130470,0)

vig=Sprite("sb\{0}.png".format("vignette"),"Centre","Foreground",output)
vig.scale(0,-1000,180000,0.625,0.625)
vig.move(0,-2000,216842,320,240,320,240)
vig.fade(0,0,0,0.7,0.7)
vig.fade(0,213058,216842,0.7,0)
vig.end()

#guitar(10,20)


guitarr("sb/gi.txt",137529,147764, 255,0,0,-50,40,600,1,140,190)
guitarr("sb/gi.txt",142117,147764,255,0,0,350,50,1100,2,150,200)
guitarr("sb/gi.txt",140705,147764,255,0,0,200,360,400,3,150,210)
guitarr("sb/gi.txt",146176,147764,255,0,0,400,70,500,4,160,194)
guitarr("sb/gi.txt",139293,147764,255,0,255,00,300,1100,5,151,205)
guitarr("sb/gi.txt",143176,147764,255,0,255,200,400,600,6,170,180)

guitarr("sb/taa.txt",143882,147764,255,0,155,80,20,1100,1,210,190)
guitarr("sb/taa.txt",140352,147764,255,0,355,350,270,500,2,225,190)


guitarr("sb/taa.txt",145823,147764,255,0,355,350,270,700,3,235,195)
guitarr("sb/taa.txt",137705,147764,255,0,355,50,300,500,4,225,213)
guitarr("sb/taa.txt",141588,147764,255,0,355,155,120,1100,5,214,224)
guitarr("sb/taa.txt",146529,147764,255,0,355,155,300,600,6,220,200)
guitarr("sb/long.txt",137882,147764,255,0,355,340,20,400,1,275,201)

guitarr("sb/long.txt",144411,147764,255,0,355,480,220,1100,2,280,205)
guitarr("sb/long.txt",142823,147764,255,0,355,200,80,1000,3,290,205)
guitarr("sb/long.txt",139999,147764,255,0,355,400,360,900,4,295,205)
guitarr("sb/long.txt",146352,147764,255,0,355,200,80,400,5,300,205)
guitarr("sb/long.txt",144941,147764,255,0,355,100,280,1200,6,320,205)

guitarr("sb/so.txt",138764,147764,255,0,355,550,400,1000,1,375,270)
guitarr("sb/so.txt",143705,147764,255,0,355,200,80,600,2,407,266)
guitarr("sb/so.txt",145999,147764,255,0,355,470,180,500,3,403,275)
guitarr("sb/so.txt",138058,147764,255,0,355,470,450,600,4,400,285)
guitarr("sb/so.txt",143352,147764,255,0,355,400,130,600,5,395,295)
guitarr("sb/so.txt",146705,147764,255,0,355,190,280,900,6,390,300)

guitarr("sb/ro.txt",138235,147764,255,0,355,580,160,600,1,445,272)
guitarr("sb/ro.txt",141058,147764,255,0,355,540,440,1100,2,455,265)
guitarr("sb/ro.txt",140882,147764,255,0,355,320,140,700,3,477,277)
guitarr("sb/ro.txt",143529,147764,255,0,355,700,290,500,4,475,285)
guitarr("sb/ro.txt",140529,147764,255,0,355,260,360,600,5,470,295)
guitarr("sb/ro.txt",147235,147764,255,0,355,630,120,1200,6,470,295)


def chorus3top(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    backwards=1000
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace
            endi=173800+(backwards)
            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+200,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+200,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)


            dot.move(2,endi,endi+650,xlist[i],ylist[i],xlist[i]+random.randint(400,500),ylist[i]+random.randint(-30,30))
            dot.fade(0,endi+500,endi+650,0.6,0)

            dot.end()
            if backwards!=0:
                backwards=backwards-1


def chorus3bottom(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    backwards=0
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace
            endi=end+(backwards)
            loopcount=(end-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+200,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+200,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)


            dot.move(2,endi,endi+650,xlist[i],ylist[i],xlist[i]-random.randint(400,500),ylist[i]-random.randint(-30,30))
            dot.fade(0,endi+500,endi+650,0.6,0)

            dot.end()

            backwards=backwards+1

def chorus3part2(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)
            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace
            radd=random.randint(400,800)
            endi=end-radd
            loopcount=(end-start)/400 - 2
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+200,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+200,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)


            rx=random.randint(-20 ,20)
            ry=random.randint(-20,20)
            while (rx)**2 + (ry)**2 > 20**2:
                rx=random.randint(-20,20)
                ry=random.randint(-20,20)

            dot.move(2,endi,endi+radd-20,xlist[i],ylist[i],320+rx,240+ry)


            dot.end()


def drawitsu2(image,start,end,pace):
    xlist=[]
    ylist=[]
    colour=[]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    localstart=start
    jumble = [181293,181470,181646,181823]
    x2=-100000
    y2=-1000000
    jump=[-1,1]
    jumpy=jump[random.randint(0,1)]
    #random.shuffle(jumble)
    print len(xlist)
    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start
        elif i%2==0:
            localstart=localstart+pace
            continue
        else:
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

            if 0<i<500:
                end=0
            elif 500<i<730:
                end=2
            elif 730<i<890:
                end=3
            elif 890<i<991:
                end=1
            else:
                end=0
                dot.scale(0,jumble[end],jumble[end],0,0)



            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]
            endi=jumble[end]


            rotation=random.random()*2*3.14

            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.06,0.16)

            dot.fade(0,localstart,localstart,0.6,0.6)
            dot.fade(0,movestart,movestart,0,0)
            dot.fade(0,endi,endi+140,0.6,0)
            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace
            dot.move(2,endi,endi+200,xlist[i],ylist[i],xlist[i]+100,ylist[i]+100)


            loopcount=(endi-start)/400
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            dot.move(0,starty+offset/2,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand2,ylist[i]+yrand2)

            if abs(xlist[i]-x2)<2:
                x2=x2+random.randint(-3,3)
                y2=y2+random.randint(-3,3)
                dot.move(1,endi,endi+200,xlist[i],ylist[i],x2,y2)

            else:

                radx=random.randint(-100,100)
                rady=random.randint(-100,100)
                dot.move(1,endi,endi+200,xlist[i],ylist[i],xlist[i]+radx,ylist[i]+rady)
                x2=xlist[i]+radx
                y2=ylist[i]+rady

            dot.end()

def chorus3part3(image,image2,start,end,pace,blah):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    cheese=0
    colour2=[]
    t=3.14
    hh=0
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        elif hh==1:
            hh=0
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
            hh=hh+1
    x.close()
    pp=0
    y=open(image2,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass
        elif pp==1:
            pp=0
            pass
        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
            pp=pp+1
    y.close()
    localstart=start

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start

        else:

            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            radd=random.randint(500,2000)
            movestart=start+radd
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart+200,0.12,0.15)
            dot.fade(0,localstart,localstart,0.6,0.6)

            rrrr=int(i*2.7)
            endi=end+rrrr
            if blah==1:
                t=3.14*3/2
            else:
                t=3.14/2
            x,y=xlist[i],ylist[i]
            radius=160
            tempend=endi

            x2=radius*maths.cos(t)+320
            y2=radius*maths.sin(t)+240
            xrann=random.randint(-5,5)
            yrann=random.randint(-5,5)
            xrann2=random.randint(-5,5)
            yrann2=random.randint(-5,5)
            dot.move(2,tempend,tempend+600,x,y,x2+xrann2,y2+yrann2)
            tempend+=600
            t=t+.35
            x=x2
            y=y2
            while tempend<187999+i*3:
                x2=radius*maths.cos(t)+320
                y2=radius*maths.sin(t)+240
                xrann=random.randint(-5,5)
                yrann=random.randint(-5,5)
                xrann2=random.randint(-5,5)
                yrann2=random.randint(-5,5)


                if 187999+i*3-tempend<100:

                    ste=187999+i*3-tempend
                    t=t-((100-ste)/100)*0.32
                    dot.move(0,tempend,tempend+ste,x+xrann,y+yrann,x2+xrann2,y2+yrann2)
                    tempend=tempend+ste
                else:
                    dot.move(0,tempend,tempend+100,x+xrann,y+yrann,x2+xrann2,y2+yrann2)
                    tempend+=100
                x=x2+xrann2
                y=y2+yrann2
                t=t+.32


            g=tempend-(187999+i*3)
            if i<len(x2list):
                dot.move(1,tempend,tempend+1000,x,y,int(x2list[i])+xrand2,int(y2list[i])+yrand2)
                loopcount=(191882-tempend+1000)/400
                offest=(tempend+1000)%200
                dot.loopdraw(tempend+1000,loopcount,-offest,int(x2list[i])+xrand2,int(y2list[i])+yrand2,int(x2list[i])+xrand,int(y2list[i])+yrand)
                dot.fade(0,192235-300,192235,0.4,0)
            else:
                dot.fade(0,tempend-300,tempend,0.4,0)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace


            loopcount=(endi-start+radd)/400 - 10
            offest=(start+radd)%200
            dot.loopdraw(movestart,loopcount,-offest,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)


            starty=(loopcount*400)+movestart
            offset=endi-starty
            dot.move(0,starty,starty+200,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+200,endi,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)


            rx=random.randint(-10 ,10)
            ry=random.randint(-10,10)
            while (rx)**2 + (ry)**2 > 10**2:
                rx=random.randint(-10,10)
                ry=random.randint(-10,10)

            dot.move(1,start,start+radd,320+rx,240+ry,xlist[i],ylist[i])
            if i==len(xlist)-1 and blah!=1:
                cheese=i
                print cheese
            dot.end()

    if cheese>=1:

        for i in range(cheese,len(x2list)):
            xrann=random.randint(-5,5)
            yrann=random.randint(-5,5)
            xrann2=random.randint(-5,5)
            yrann2=random.randint(-5,5)
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,tempend,tempend,rotation,rotation)
            dot.scale(0,tempend,tempend+200,0.12,0.15)
            dot.fade(0,tempend,tempend,0.6,0.6)
            dot.move(1,tempend,tempend+1000,480+xrann,225+yrann,int(x2list[i])+xrand2,int(y2list[i])+yrand2)
            loopcount=(191882-tempend+1000)/400
            offest=(tempend+1000)%200
            dot.loopdraw(tempend+1000,loopcount,-offest,int(x2list[i])+xrand2,int(y2list[i])+yrand2,int(x2list[i])+xrand,int(y2list[i])+yrand)
            dot.fade(0,192235-300,192235,0.6,0)
            dot.colour(0,tempend,tempend,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace
            dot.end()

    for i in range(0,100):
        radd=random.randint(500,2000)
        dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
        dot.rotate(0,localstart,localstart,rotation,rotation)
        dot.scale(0,localstart,localstart+200,0.12,0.16)
        dot.fade(0,localstart,localstart,0.6,0.6)

        rx=random.randint(-20,20)
        ry=random.randint(-20,20)
        while (rx)**2 + (ry)**2 > 20**2:
            rx=random.randint(-20,20)
            ry=random.randint(-20,20)
        if blah==1:
            xra=random.randint(-200,400)
            yra=random.randint(-100,200)
        else:
            xra=random.randint(270,900)
            yra=random.randint(300,600)
        dot.colour(0,start,start,0,0,0,0,0,0)
        dot.move(1,start,start+radd,320+rx,240+ry,xra,yra)
        dot.fade(0,start+radd-200,start+radd,0.6,0)
        dot.end()

def drawsplit(image,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]


    tt=[191882,191970,192058,192146,192235]
    tr=[192588,192764,192941,193117,193293]
    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    drawstay("sb/tobira.txt",tr[0],197529,0,0,0,0)
    drawstay("sb/wo.txt",tr[1],197529,0,0,0,0)
    drawstay("sb/a.txt",tr[2],197529,0,0,0,0)
    drawstay("sb/ke.txt",tr[3],197529,0,0,0,0)
    drawstay("sb/te.txt",tr[4],197529,0,0,0,0)


    localstart=start

    for i in range(0,len(xlist)):
        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start

        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])
            movestart=start
            colourc=colour[i]

            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(-1,0)
            yrand=random.randint(0,1)
            xrand2=random.randint(-1,0)
            yrand2=random.randint(0,1)
            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.15,0.15)
            dot.fade(0,localstart,localstart,0.4,0.4)
            dot.fade(0,movestart,movestart,0,0)


            dot.move(2,end-300,end,xlist[i]+xrand2,ylist[i]+yrand2,320,240)
            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            localstart=localstart+pace

            '''loopcount=(end-300-start)/400 -2
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)'''



            dot.move(0,start,end-300,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)


            rrrr=random.randint(1100,1100)
            endi=end+rrrr
            if 0<i<len(xlist)/5:
                t=1.256-((i-0)/100)
                endd=tt[0]
                enddd=tr[0]
            elif len(xlist)/5<i<len(xlist)*2/5:
                t=2.51-((i-len(xlist)/5)/100)
                endd=tt[1]
                enddd=tr[1]
            elif len(xlist)*2/5<i<len(xlist)*3/5:
                t=3.77-((i-len(xlist)*2/5)/100)
                endd=tt[2]
                enddd=tr[2]
            elif len(xlist)*3/5<i<len(xlist)*4/5:
                t=5.026-((i-len(xlist)*3/5)/100)
                endd=tt[3]
                enddd=tr[3]
            elif len(xlist)*4/5<i<len(xlist):
                t=6.28-((i-len(xlist)*4/5)/100)
                endd=tt[4]
                enddd=tr[4]
            else:
                endd=tt[1]
                enddd=tr[1]
                dot.fade(0,end,enddd,0,0)
                t=1.256



            x,y=320,240


            xrann=random.randint(-10,10)
            yrann=random.randint(-10,10)
            while xrann**2+yrann**2>10**2:
                xrann=random.randint(-10,10)
                yrann=random.randint(-10,10)
            xrann2=random.randint(-10,10)
            yrann2=random.randint(-10,10)



            radius=(x-320)**2 + (y-240)**2
            radius=maths.sqrt(radius)
            rad=radius
            tempend=end
            endrad=215
            raddif=(215-radius)/(((end-endi)/50)*1.0)
            step=30
            while tempend<endi:
                if step<150:
                    step+=1
                x2=radius*maths.cos(t)+320
                y2=radius*maths.sin(t)+240

                raddif=(220-rad)/(((end-endi)/step)*1.0)
                dot.move(0,tempend,tempend+step,x+xrann,y+yrann,x2+xrann,y2+yrann)


                x=x2
                y=y2
                t=t-.20
                tempend+=step
                radius=radius-raddif

            dif=0.15
            while tempend<enddd-300:
                x2=radius*maths.cos(t)+320
                y2=radius*maths.sin(t)+240


                dot.move(0,tempend,tempend+step,x+xrann,y+yrann,x2+xrann,y2+yrann)


                x=x2
                y=y2

                if dif>0.08:
                    dif-=0.01
                t=t-dif
                tempend+=step

            rrd=random.randint(-35,35)
            rre=random.randint(-35,35)
            while rrd**2+rre**2>35**2:
                rrd=random.randint(-35,35)
                rre=random.randint(-35,35)

            rrd2=random.randint(-55,55)
            rre2=random.randint(-55,55)
            while rrd2**2+rre2**2>55**2:
                rrd2=random.randint(-55,55)
                rre2=random.randint(-55,55)

            if endd==tt[0]:
                dot.colour(0,endd,endd,242,36,108,242,36,108)
                dot.fade(0,endd-100,endd-100,0.8,0.8)
                dot.move(2,enddd-300,enddd,x+xrann,y+yrann,193+rrd,240+rre)
                dot.move(1,enddd,enddd+500,193+rrd,240+rre,370+rrd2,380+rre2)
                dot.fade(0,enddd+300,enddd+450,0.8,0)

            elif endd==tt[1]:
                dot.colour(0,endd,endd,148,48,162,148,48,162)
                dot.move(2,enddd-300,enddd,x+xrann,y+yrann,257+rrd,230+rre)
                dot.fade(0,endd-100,endd-100,0.8,0.8)
                dot.move(1,enddd,enddd+500,257+rrd,230+rre,260+rrd2,440+rre2)
                dot.fade(0,enddd+300,enddd+450,0.8,0)

            elif endd==tt[2]:
                dot.colour(0,endd,endd,0,201,237,0,201,237)
                dot.move(2,enddd-300,enddd,x+xrann,y+yrann,326+rrd,230+rre)
                dot.fade(0,endd-100,endd-100,0.8,0.8)
                dot.move(1,enddd,enddd+500,326+rrd,230+rre,185+rrd2,430+rre2)
                dot.fade(0,enddd+300,enddd+450,0.8,0)


            elif endd==tt[3]:
                dot.colour(0,endd,endd,91,211,64,91,211,64)
                dot.move(2,enddd-300,enddd,x+xrann,y+yrann,395+rrd,230+rre)
                dot.fade(0,endd-100,endd-100,0.8,0.8)
                dot.move(1,enddd,enddd+500,395+rrd,230+rre,160+rrd2,170+rre2)
                dot.fade(0,enddd+300,enddd+450,0.8,0)



            elif endd==tt[4]:
                dot.colour(0,endd,endd,248,159,33,248,159,33)
                dot.move(2,enddd-300,enddd,x+xrann,y+yrann,467+rrd,230+rre)
                dot.fade(0,endd-100,endd-100,0.8,0.8)
                dot.move(1,enddd,enddd+500,467+rrd,230+rre,540+rrd2,0+rre2)
                dot.fade(0,enddd+350,enddd+450,0.8,0)



            dot.end()




    for i in range(0,1000):
        dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)
        if  0<=i<250:
            endd=tt[0]
            enddd=tr[0]
            x,y=110,174
            x2,y2=193,240
            x3,y3=370,380
            dot.colour(0,enddd-300,enddd-300,242,36,108,242,36,108)
        elif  250<=i<500:
            endd=tt[1]
            enddd=tr[1]
            x,y=262,25
            x2,y2=257,230
            x3,y3=260,440
            dot.colour(0,enddd-300,enddd-300,148,48,162,148,48,162)
        elif 500<=i<750:
            endd=tt[2]
            enddd=tr[2]
            x,y=478,82
            x2,y2=326,230
            x3,y3=185,430
            dot.colour(0,enddd-300,enddd-300,0,201,237,0,201,237)
        elif 750<=i<1000:
            endd=tt[3]
            enddd=tr[3]
            x,y=535,272
            x2,y2=395,230
            x3,y3=160,170
            dot.colour(0,enddd-300,enddd-300,91,211,64,91,211,64)
        else:
            endd=tt[4]
            enddd=tr[4]
            x,y=412,440
            x2,y2=467,230
            x3,y3=540,0
            dot.colour(0,enddd-300,enddd-300,248,159,33,248,159,33)

        rrd=random.randint(-35,35)
        rre=random.randint(-35,35)
        while rrd**2+rre**2>35**2:
            rrd=random.randint(-35,35)
            rre=random.randint(-35,35)

        rrd2=random.randint(-85,85)
        rre2=random.randint(-85,85)
        while rrd2**2+rre2**2>55**2:
            rrd2=random.randint(-85,85)
            rre2=random.randint(-85,85)

        rotation=random.random()*2*3.14
        dot.rotate(0,enddd-300,enddd-300,rotation,rotation)
        dot.scale(0,enddd-300,enddd-300,0.15,0.15)
        dot.fade(0,endd-500,endd-500,0,0)

        dot.fade(0,endd-100,endd-100,0.8,0.8)
        dot.move(2,enddd-300,enddd,x,y,x2+rrd,y2+rre)
        if enddd==tr[4]:
            dot.move(1,enddd,enddd+500,x2+rrd,y2+rre,x3+rrd2,y3+rre2)
        else:
            dot.move(1,enddd,enddd+500,x2+rrd,y2+rre,x3+rrd2,y3+rre2)
        dot.fade(0,enddd+300,enddd+450,0.8,0)
        dot.end()












image2("ddddd",198235,210235,203558,315,9,0.532,0.0)
drawdraw2("sb/check.txt",197529,204411,11.2)
drawdraw2("sb/c.txt",197529,204411,11.2)
drawdraw2("sb/fin.txt",209235,213705,4)

chorus3top("sb/3chorus1.txt",170705,174235,2)
chorus3bottom("sb/3chorus2.txt",172646,174235,3)
drawbase("sb/3chorus3.txt",174235,175999,2)
chorus3part2("sb/chorus9.txt",175999,181999,2)
chorus3part2("sb/3chorus4.txt",177058,181999,2)
drawitsu2("sb/3chorus5.txt",178470,181999,2)
chorus3part2("sb/3chorus6.txt",179882,181999,3)
chorus3part3("sb/3chorus7.txt","sb/3chorus11.txt",181999,185529,0,1)
chorus3part3("sb/3chorus8.txt","sb/3chorus12.txt",181999,185529,0,-1)

def drawslowpart4(image,nextimage,start,end, pace):
    xlist=[]
    ylist=[]
    colour=[]
    x2list=[]
    y2list=[]
    colour2=[]

    x=open(image,'r')
    for line in x:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            xlist.append(line[0])
            ylist.append(line[1])
            colour.append((line[2],line[3],int(line[4])))
    x.close()

    y=open(nextimage,'r')
    for line in y:

        line=line.split(',')
        if line[0]=='\n':
            pass
        else:
            x2list.append(line[0])
            y2list.append(line[1])
            colour2.append((line[2],line[3],int(line[4])))
    y.close()

    localstart=start
    sant=[]
    fakeend=end-250


    for i in range(0,len(x2list)):
        sant.append(i)

    for i in range(0,len(xlist)):

        c='Break'
        if xlist[i]==c:
            localstart,movestart=start,start

        else:
            xlist[i]=int(xlist[i])
            ylist[i]=int(ylist[i])

            movestart=start
            colourc=colour[i]

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

          #      if xlist[i]<initialx:
          #          dot.move(0,movestart,movestart+100,xlist[i]+randint(100,200),ylist[i]+rand(-200,200),xlist[i],ylist[i])




            rotation=random.random()*2*3.14
            rotation2=random.random()*2*3.14
            xrand=random.randint(0,1)
            yrand=random.randint(-1,0)
            xrand2=random.randint(0,1)
            yrand2=random.randint(-1,0)

            dot.rotate(0,localstart,localstart,rotation,rotation)
            dot.scale(0,localstart,localstart,0.14,0.140)
            dot.fade(0,localstart-300,localstart,0.0,0.4)

            dot.colour(0,localstart,localstart,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])

           # dot.move(0,start,end,int(xlist[i]),int(ylist[i]),int(xlist[i]),int(ylist[i]))
            localstart=localstart+pace



            loopcount=((fakeend-start)/400 )
            dot.loopdraw(movestart,loopcount,0,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand,ylist[i]+yrand)
            starty=(loopcount*400)+movestart
            offset=fakeend-starty
            dot.move(0,starty,starty+offset/2,xlist[i]+xrand2,ylist[i]+yrand2,xlist[i]+xrand2,ylist[i]+yrand2)
            dot.move(0,starty+offset/2,fakeend,xlist[i]+xrand,ylist[i]+yrand,xlist[i]+xrand,ylist[i]+yrand)



            if i>len(x2list):
                doo=random.randint(0,len(x2list)-1)

                dot.move(5,fakeend,end,xlist[i],ylist[i],int(x2list[doo]),int(y2list[doo]))

               # sant.remove(doo)



            dot.end()
    for i in sant:
        c='Break'
        b=sant.index(i)

        a=random.randint(0,len(xlist)-1)
        if xlist[a]==c:
            localstart,movestart=start,start
        else:

            dot=Sprite("sb\{0}\{1}.png".format("crappy","dot"),"Centre","Foreground",output)

            dot.rotate(0,fakeend,fakeend,rotation,rotation)
            dot.scale(0,fakeend,fakeend,0.14,0.140)
            dot.fade(0,fakeend,fakeend,0.4,0.4)

            dot.colour(0,fakeend,fakeend,colourc[0],colourc[1],colourc[2],colourc[0],colourc[1],colourc[2])
            dot.move(5,fakeend,end,int(xlist[a]),int(ylist[a]),int(x2list[b]),int(y2list[b]))

            dot.end()


drawslowpart4("sb/3chorus9.txt","sb/3chorus10.txt",185705,187293, 2)
drawsplit("sb/3chorus10.txt",187293,187646, 0)
drawbase("sb/nee.txt",130646,131352,0)

out=open(output,"a")
out.write("//Stupid Glitch")
out.close()
