# -*- coding:gbk -*-

import sys
reload(sys)
sys.setdefaultencoding('gbk')

import os
import logging
import random
import math
import time
import datetime
import struct
logging.basicConfig(
    level       = logging.INFO,
    format      = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt     = '%Y-%m-%d %H:%M:%S',
    filename    = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'CQHanlder.log'),
    filemode    = 'w+'
)

import CQSDK

array0=[0]*51
array0[0]=10000
array=[0]*50
lib0= open("d:\\drawlib\\name.txt","r")
namelist=[" "]*50
lines=lib0.readlines(100)
i=0
for line in lines:
	namelist[i]=line.strip('\n')
	i+=1
	
#localtim=datetime.date.today()
	#date=localtim.isoweekday()


			
class CQHandler(object):

						
						
    def __init__(self):
        logging.info('__init__')
        
    def __del__(self):
        logging.info('__del__')
        
    def OnEvent_Enable(self):
        logging.info('OnEvent_Enable')

    def OnEvent_Disable(self):
        logging.info('OnEvent_Disable')

    def OnEvent_PrivateMsg(self, subType, sendTime, fromQQ, msg, font):
        logging.info('OnEvent_PrivateMsg: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, font={4}'.format(subType, sendTime, fromQQ, msg, font))

        #try:
            #CQSDK.SendPrivateMsg(fromQQ, msg)
        #except Exception as e:
            #logging.exception(e)

    def OnEvent_GroupMsg(self, subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font):
		logging.info('OnEvent_GroupMsg: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, fromAnonymous={4}, msg={5}, font={6}'.format(subType, sendTime, fromGroup, fromQQ, fromAnonymous, msg, font))

        #try:
            #CQSDK.SendGroupMsg(fromGroup, msg)
        #except Exception as e:
            #logging.exception(e)
		if (fromQQ == 825419319):
			if (msg[0:7] == '!repeat'):
				CQSDK.SendGroupMsg(fromGroup, msg[7:])
			if (msg[0:4] =='test'):	
				j=random.randint(1,49)
				CQSDK.SendGroupMsg(fromGroup, namelist[j])
				#CQSDK.SendGroupMsg(fromGroup, str(array0))
			if (msg[0:11] =='!datechange'):				
				path="d:/drawlib/"
				files= os.listdir(path)			
				for file in files:
					if file != "name.txt":						
						filename='d:/drawlib/'+file
						lib=open(filename,"r")						
						bag=[' ']*51
						lines=lib.readlines(100)
						k=0		
						lib.close()
						for line in lines:
							bag[k]=int(line)
							k+=1
						bag[50]=0						
						lib=open(filename,"w")
						for p in bag:
							lib.write(str(p))
							lib.write('\n')	
						lib.close()
				CQSDK.SendGroupMsg(fromGroup, 'Date changed')
		
		
		if (msg[0:12] =="!qll draw 1 "):
			#CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"\nNo enough jewel")
			filename="d:\\drawlib\\"+str(fromQQ)+'.txt'
			
			#bag2=lib.read()
			#CQSDK.SendGroupMsg(fromGroup, '23'+bag2+len(bag2))
			if os.path.exists(filename):
				lib=open(filename,"r")
				#CQSDK.SendGroupMsg(fromGroup, 'ari')
				
				bag=[" "]*51
				lines=lib.readlines(100)
				k=0
				for line in lines:
					bag[k]=int(line)#.strip('\n')
					k+=1
				#CQSDK.SendGroupMsg(fromGroup, bag)
					
				
				if bag[0]<150:
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"\nNo enough jewel")
				else:
					bag[0]-=150
					rslt1=random.randint(1,100)
					if rslt1<=2:
						rslt2=random.randint(1,17)
						bag[rslt2]+=1
						CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']Get:\n'+namelist[rslt2])
					elif rslt1>2 and rslt1<=20:
						rslt2=random.randint(1,18)
						bag[rslt2+17]+=1
						CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']Get:\n'+namelist[rslt2+17])
					else:
						rslt2=random.randint(1,14)
						bag[rslt2+35]+=1
						CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']Get:\n'+namelist[rslt2+35])
					lib=open(filename,"w")
					for p in bag:
						lib.write(str(p))
						lib.write('\n')
					#lib.write(bag)
				
					
			else:
				#CQSDK.SendGroupMsg(fromGroup, 'inai')
				lib=open(filename,"w+")
				CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Account registered, 10000 jewel obtained.')
				for p in array0:
					lib.write(str(p))
					lib.write('\n')
				#lib.writelines(str(array0))
			if lib:	
				lib.close()
		
		
				
					
			else:
				#CQSDK.SendGroupMsg(fromGroup, 'inai')
				lib=open(filename,"w+")
				CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Account registed, 10000 jewel obtained.')
				for p in array0:
					lib.write(str(p))
					lib.write('\n')
				#lib.writelines(str(array0))
			if lib:	
				lib.close()
				
				
				
		if (msg[0:12] =="!qll draw 10"):
			#CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"\nNo enough jewel")
			filename="d:\\drawlib\\"+str(fromQQ)+'.txt'
			
			#bag2=lib.read()
			#CQSDK.SendGroupMsg(fromGroup, '23'+bag2+len(bag2))
			if os.path.exists(filename):
				lib=open(filename,"r")
				#CQSDK.SendGroupMsg(fromGroup, 'ari')
				
				bag=[" "]*51
				lines=lib.readlines(100)
				k=0
				lib.close()
				for line in lines:
					bag[k]=int(line)#.strip('\n')
					k+=1
				#CQSDK.SendGroupMsg(fromGroup, bag)
					
				
				if bag[0]<1500:
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"\nNo enough jewel")
				else:
					bag[0]-=1500
					list2=[" "]*10
					for num in range(0,9):
						rslt1=random.randint(1,100)
						if rslt1<=2:
							rslt2=random.randint(1,17)
							bag[rslt2]+=1
							list2[num]=namelist[rslt2]
						elif rslt1>2 and rslt1<=20:
							rslt2=random.randint(1,18)
							bag[rslt2+17]+=1
							list2[num]=namelist[rslt2+17]
						else:
							rslt2=random.randint(1,14)
							bag[rslt2+35]+=1
							list2[num]=namelist[rslt2+35]
							
					rslt3=random.randint(1,100)
					if rslt3<=2:
						rslt2=random.randint(1,17)
						bag[rslt2]+=1
						list2[9]=namelist[rslt2]
					else:
						rslt2=random.randint(1,18)
						bag[rslt2+17]+=1
						list2[9]=namelist[rslt2+17]
						
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"Get:\n"+'\n'.join(list2))
					
					lib=open(filename,"w")
					for p in bag:
						lib.write(str(p))
						lib.write('\n')
					#lib.write(bag)
					lib.close()
					
			else:
				#CQSDK.SendGroupMsg(fromGroup, 'inai')
				lib=open(filename,"w+")
				
				CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Account registered, 10000 jewel obtained.')
				for p in array0:
					lib.write(str(p))
					lib.write('\n')
				#lib.writelines(str(array0))
				if lib:	
					lib.close()
			
			
		if (msg[0:8] =="!qll bag"):		
			filename="d:\\drawlib\\"+str(fromQQ)+'.txt'
			if os.path.exists(filename):
				lib=open(filename,"r")
				bag=[" "]*51
				lines=lib.readlines(100)
				k=0
				lib.close()
				for line in lines:
					bag[k]=int(line)#.strip('\n')
					k+=1
				if os.path.exists(filename):
					baglist=[" "]*50
					for num in range(0,50):
						baglist[num]=namelist[num]+'   '+str(bag[num])
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']'+"Your Bag:\n"+'\n'.join(baglist))
				else:
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'You have not registered')
			else:
				#CQSDK.SendGroupMsg(fromGroup, 'inai')
				lib=open(filename,"w+")
				
				CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Account registered, 10000 jewel obtained.')
				for p in array0:
					lib.write(str(p))
					lib.write('\n')
				#lib.writelines(str(array0))
				if lib:	
					lib.close()
			
			
		if (msg[0:8] =="!checkin"):
			filename="d:/drawlib/"+str(fromQQ)+'.txt'
			if os.path.exists(filename):
				lib=open(filename,"r")
				bag=[" "]*51
				lines=lib.readlines(100)
				k=0
				lib.close()
				for line in lines:
					bag[k]=int(line)#.strip('\n')
					k+=1
				if bag[50]==0:
					signin=random.randint(500,2000)
					bag[0]+=signin
					bag[50]=1
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Succeeded. You got '+str(signin)+' jewels')
					lib=open(filename,"w")
					for p in bag:
						lib.write(str(p))
						lib.write('\n')
					lib.close()
				else:
					CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'You have checked in today')
			else:
				#CQSDK.SendGroupMsg(fromGroup, 'inai')
				lib=open(filename,"w+")
				
				CQSDK.SendGroupMsg(fromGroup, '[CQ:at,qq='+str(fromQQ)+']\n'+'Account registered, 10000 jewel obtained.')
				for p in array0:
					lib.write(str(p))
					lib.write('\n')
				#lib.writelines(str(array0))
				if lib:	
					lib.close()
		
		
		if (msg[0:9] =="!qll help"):
			CQSDK.SendGroupMsg(fromGroup, "!help:\nPlease draw first to start your account!\n!qll draw 1 : spend 150 jewels\n\
!qll draw 10: spend 1500 jewels\n!qll bag: see your bag\n!checkin: get 500 to 2000 jewels")
		
		'''
		localt=datetime.date.today()
		#date2=localt.isoweekday()
		
		#CQSDK.SendGroupMsg(fromGroup, str(date)+str(date2)
		#lip=date2 - date
		#CQSDK.SendGroupMsg(fromGroup, ' 23 ')
		if   localt>localtim  : #lip > datetime.timedelta(hours=20):
				
			#CQSDK.SendGroupMsg(fromGroup, '233  ')	
			path="d:/drawlib/"
			files= os.listdir(path)	
					
			for file in files:
					
				if file != "name.txt":						
					filename='d:/drawlib/'+file
					lib=open(filename,"r")						
					bag=[' ']*51
					lines=lib.readlines(100)
					k=0			
					lib.close()
					for line in lines:
						bag[k]=int(line)
						k+=1
					bag[50]=0						
					lib=open(filename,"w")
					for p in bag:
						lib.write(str(p))
						lib.write('\n')	
					lib.close()
				#CQSDK.SendGroupMsg(fromGroup, 'Date changed')	
			localtim=localt
		#else:
		#	CQSDK.SendGroupMsg(fromGroup, ' 34 ')	
		'''
    def OnEvent_DiscussMsg(self, subType, sendTime, fromDiscuss, fromQQ, msg, font):
        logging.info('OnEvent_DiscussMsg: subType={0}, sendTime={1}, fromDiscuss={2}, fromQQ={3}, msg={4}, font={5}'.format(subType, sendTime, fromDiscuss, fromQQ, msg, font))

    def OnEvent_System_GroupAdmin(self, subType, sendTime, fromGroup, beingOperateQQ):
        logging.info('OnEvent_System_GroupAdmin: subType={0}, sendTime={1}, fromGroup={2}, beingOperateQQ={3}'.format(subType, sendTime, fromGroup, beingOperateQQ))

    def OnEvent_System_GroupMemberDecrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberDecrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_System_GroupMemberIncrease(self, subType, sendTime, fromGroup, fromQQ, beingOperateQQ):
        logging.info('OnEvent_System_GroupMemberIncrease: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, beingOperateQQ={4}'.format(subType, sendTime, fromGroup, fromQQ, beingOperateQQ))

    def OnEvent_Friend_Add(self, subType, sendTime, fromQQ):
        logging.info('OnEvent_Friend_Add: subType={0}, sendTime={1}, fromQQ={2}'.format(subType, sendTime, fromQQ))

    def OnEvent_Request_AddFriend(self, subType, sendTime, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddFriend: subType={0}, sendTime={1}, fromQQ={2}, msg={3}, responseFlag={4}'.format(subType, sendTime, fromQQ, msg, responseFlag))

    def OnEvent_Request_AddGroup(self, subType, sendTime, fromGroup, fromQQ, msg, responseFlag):
        logging.info('OnEvent_Request_AddGroup: subType={0}, sendTime={1}, fromGroup={2}, fromQQ={3}, msg={4}, responseFlag={5}'.format(subType, sendTime, fromGroup, fromQQ, msg, responseFlag))

    def OnEvent_Menu01(self):
        logging.info('OnEvent_Menu01')

    def OnEvent_Menu02(self):
        logging.info('OnEvent_Menu02')

    def OnEvent_Menu03(self):
        logging.info('OnEvent_Menu03')

    def OnEvent_Menu04(self):
        logging.info('OnEvent_Menu04')

    def OnEvent_Menu05(self):
        logging.info('OnEvent_Menu05')

    def OnEvent_Menu06(self):
        logging.info('OnEvent_Menu06')

    def OnEvent_Menu07(self):
        logging.info('OnEvent_Menu07')

    def OnEvent_Menu08(self):
        logging.info('OnEvent_Menu08')

    def OnEvent_Menu09(self):
        logging.info('OnEvent_Menu09')