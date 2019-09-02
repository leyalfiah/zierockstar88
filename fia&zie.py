from LINEPY import *
from akad.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, asyncio, os, requests, subprocess, six, urllib, urllib.parse
from thrift.transport import TTransport,TSocket,THttpClient,TTransport,TZlibTransport
from thrift.protocol import TCompactProtocol,TMultiplexedProtocol,TProtocol
from thrift.server import THttpServer,TServer,TProcessPoolServer
from threading import Thread
import ast,re,time,random,sys,json,codecs,threading,glob,tempfile, os, six
import os,six, urllib, wikipedia, requests, bs4, html5lib, multiprocessing
import subprocess

line = LINE("")
line.log("Auth Token : " + str(line.authToken))
ki = LINE("")
ki.log("Auth Token : " + str(ki.authToken))
kk = LINE("")
kk.log("Auth Token : " + str(kk.authToken))
kc = LINE("")
kc.log("Auth Token : " + str(kc.authToken))
ks = LINE("")
ks.log("Auth Token : " + str(ks.authToken))
ka = LINE("")
ka.log("Auth Token : " + str(ka.authToken))
kb = LINE("")
kb.log("Auth Token : " + str(kb.authToken))
print ("\nSTARTING SYSTEM...")
cl = line
oepoll = OEPoll(cl)
oepoll1 = OEPoll(ki)
oepoll2 = OEPoll(kk)
oepoll3 = OEPoll(kc)
oepoll4 = OEPoll(ks)
oepoll5 = OEPoll(ka)
oepoll6 = OEPoll(kb)
All = [ki,kk,kc,ks,ka,kb]
mid = cl.profile.mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Botku = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid]
Fiaku = ["u6753b4e8b582e34a0dd69f2c96a59198"]
Zie = ["u6753b4e8b582e34a0dd69f2c96a59198"]
Fiazie = Fiaku + Botku + Zie
Setbot = codecs.open("setting2.json","r","utf-8")
Setmain = json.load(Setbot)

#------------------------------------------------
settings = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }
}
#------------------------------------------------

mulai   = time.time()
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def AUTO_RELOAD(path=None, update_headers=None, service=None):
    Headers = {'User-Agent': RELOAD_UA,'X-Line-Application': RELOAD_LA,"x-lal": "ja-US_US"}
    Headers.update({"x-lpqs" : path})
    if(update_headers is not None):
        Headers.update(update_headers)
    transport = THttpClient.THttpClient(host + path)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    cl = service(protocol)
    return client

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "[=====][ Mentones ][=====]\n[:] 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "[:]  {}. ".format(str(no))
            else:
                textx += "\n[=====] Total Member : {} [=====]".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def cek(mid):
    if mid in (Botku + Fiaku):
        return True
    else:
        return False    

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return

        if op.type == 5:
            if Setmain["Rautoadd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (Setmain["Rmessage"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendMessage(op.param1,format(str(Setmain["Rmessage"])))

        if op.type == 11:#NOTIFIED_UPDATE_GROUP
           if op.param1 in Setmain["qr"]:
             if op.param3 == '4':
               if op.param2 in Fiazie:
                  pass
               else:
                   if op.param2 not in Setmain["Rblacklist"]:
                      Setmain["Rblacklist"][op.param2] = True
                      f=codecs.open('setting2.json','w','utf-8')
                      json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                   G = random.choice(All).getGroup(op.param1)
                   G.preventedJoinByTicket = True
                   random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                   X = random.choice(All).getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   random.choice(All).updateGroup(X)
                   

        if op.type == 11:#NOTIFIED_UPDATE_GROUP
           if op.param2 in Setmain["Rblacklist"]:
             if op.param3 == '4':
               if op.param2 in Fiazie:
                  pass
               else:
                   G = random.choice(All).getGroup(op.param1)
                   G.preventedJoinByTicket = True
                   random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                   X = random.choice(All).getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   random.choice(All).updateGroup(X)                  

        if op.type == 13:
            if mid in op.param3:
                if Setmain["Rautojoin"] ==True:
                    if op.param2 in Fiazie:
                      cl.acceptGroupInvitation(op.param1)
                    else:
                      cl.acceptGroupInvitation(op.param1)
                      cl.leaveGroup(op.param1)

        if op.type == 13:#NOTIFIED_INVITE_INTO_GROUP
            if op.param1 in Setmain["inv"]:
               if op.param2 in Fiazie:
                  pass
               else:
                   if op.param2 not in Setmain["Rblacklist"]:
                      Setmain["Rblacklist"][op.param2] = True
                      f=codecs.open('setting2.json','w','utf-8')
                      json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                   anu = random.choice(All).getCompactGroup(op.param1)
                   if anu.invitee is not None:
                         pipo = [a.mid for a in anu.invitee]
                         for target in pipo:
                             if target in op.param3:
                                random.choice(All).cancelGroupInvitation(op.param1,[target])
                                random.choice(All).kickoutFromGroup(op.param1,[target])
                         random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                         
        if op.type == 13:#NOTIFIED_INVITE_INTO_GROUP
            if op.param2 in Setmain["Rblacklist"]:
               if op.param2 in Fiazie:
                  pass
               else:
                  try:
                      anu = random.choice(All).getCompactGroup(op.param1)
                      if anu.invitee is not None:
                            pipo = [a.mid for a in anu.invitee]
                            for target in pipo:
                                if target in op.param3:
                                    random.choice(All).cancelGroupInvitation(op.param1,[target])
                                    random.choice(All).kickoutFromGroup(op.param1,[target])
                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      pass          
                                                 
        if op.type == 32:#NOTIFIED_CANCEL_INVITATION_GROUP
           if op.param1 in Setmain["cancel"]:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                  try:
                    random.choice(All).getCompactGroup(op.param1)
                    random.choice(All).findAndAddContactsByMid(op.param3)
                    random.choice(All).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(All).acceptGroupInvitation(op.param1)
                  except:
                      pass

        if op.type == 32:#NOTIFIED_CANCEL_INVITATION_GROUP
           if op.param2 in Setmain["Rblacklist"]:
              if op.param2 in Fiazie:
                 pass
              else:
                 random.choice(All).getCompactGroup(op.param1)
                 random.choice(All).findAndAddContactsByMid(op.param3)
                 random.choice(All).inviteIntoGroup(op.param1,[op.param3])
                 random.choice(All).acceptGroupInvitation(op.param1)
                 random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                 
        if op.type == 19 or op.type == 13 or op.type == 11:#NOTIFIED_KICKOUT_FROM_GROUP
           if mid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    cl.acceptGroupInvitation(op.param1)
                    kb.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        cl.acceptGroupInvitation(op.param1)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            cl.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                cl.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,Botku)
                                    cl.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,Botku)
                                        cl.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = kb.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kb.updateGroup(G)
                                               Ticket = kb.reissueGroupTicket(op.param1)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return
                 
        if op.type == 19 or op.type == 13 or op.type == 11:
           if Amid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ka.findAndAddContactsByMid(op.param3)
                    ka.kickoutFromGroup(op.param1,[op.param2])
                    ka.inviteIntoGroup(op.param1,Botku)
                    ki.acceptGroupInvitation(op.param1)
                    ks.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        ki.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            ki.acceptGroupInvitation(op.param1)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                ki.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Botku)
                                    ki.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        ki.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ka.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = ka.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               ka.updateGroup(G)
                                               Ticket = ka.reissueGroupTicket(op.param1)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return   
                 
        if op.type == 19 or op.type == 13 or op.type == 11:
           if Bmid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    kk.acceptGroupInvitation(op.param1)
                    kb.kickoutFromGroup(op.param1,[op.param2])
                    ka.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,Botku)
                        kk.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            kk.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                kk.acceptGroupInvitation(op.param1)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Botku)
                                    kk.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        kk.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = ks.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               ks.updateGroup(G)
                                               Ticket = ks.reissueGroupTicket(op.param1)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return                      
                 
        if op.type == 19 or op.type == 13 or op.type == 11:
           if Cmid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    kc.acceptGroupInvitation(op.param1)
                    ka.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        kc.acceptGroupInvitation(op.param1)
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,Botku)
                            kc.acceptGroupInvitation(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                kc.acceptGroupInvitation(op.param1)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Botku)
                                    kc.acceptGroupInvitation(op.param1)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        kc.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        kk.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = ki.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               ki.updateGroup(G)
                                               Ticket = ki.reissueGroupTicket(op.param1)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return                      
                 
        if op.type == 19 or op.type == 13 or op.type == 11:
           if Dmid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    ks.acceptGroupInvitation(op.param1)
                    kb.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        ks.acceptGroupInvitation(op.param1)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            ks.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ka.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,Botku)
                                ks.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Botku)
                                    ks.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        ks.acceptGroupInvitation(op.param1)
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ka.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = kk.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kk.updateGroup(G)
                                               Ticket = kk.reissueGroupTicket(op.param1)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return                      
                 
        if op.type == 19 or op.type == 13 or op.type == 11:
           if Emid in op.param3:
              if op.param2 in Fiazie:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    ka.acceptGroupInvitation(op.param1)
                    kb.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        ka.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            ka.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                ka.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Botku)
                                    ka.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        ka.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = kc.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               kc.updateGroup(G)
                                               Ticket = kc.reissueGroupTicket(op.param1)
                                               cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return

        if op.type == 19 or op.type == 13 or op.type == 11:
           if Fmid in op.param3:
              if op.param2 in RTeam:
                 pass
              else:
                if op.param2 not in Setmain["Rblacklist"]:
                  Setmain["Rblacklist"][op.param2] = True
                  f=codecs.open('setting2.json','w','utf-8')
                  json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    kb.acceptGroupInvitation(op.param1)
                    ka.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        kb.acceptGroupInvitation(op.param1)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            kb.acceptGroupInvitation(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                kb.acceptGroupInvitation(op.param1)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,Botku)
                                    kb.acceptGroupInvitation(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,Botku)
                                        kb.acceptGroupInvitation(op.param1)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        kk.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            random.choice(All).findAndAddContactsByMid(op.param3)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).inviteIntoGroup(op.param1,Botku)
                                            random.choice(All).acceptGroupInvitation(op.param1)
                                            random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                               G = cl.getGroup(op.param1)
                                               G.preventedJoinByTicket = False
                                               cl.updateGroup(G)
                                               Ticket = cl.reissueGroupTicket(op.param1)
                                               kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                               random.choice(All).kickoutFromGroup(op.param1,[op.param2])
              return

        if op.param3 in Fiaku:
            if op.param2 in Fiazie:
                pass
            else:
                if op.param2 not in Setmain["Rblacklist"]:
                    Setmain["Rblacklist"][op.param2] = True
                    f=codecs.open('setting2.json','w','utf-8')
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    ks.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,Botku)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,Botku)
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            cl.findAndAddContactsByMid(op.param3)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,Botku)
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                            ka.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                random.choice(All).findAndAddContactsByMid(op.param3)
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(All).inviteIntoGroup(op.param1,Botku)
                                                random.choice(All).acceptGroupInvitation(op.param1)
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                pass
            return
        if op.param3 in Zie:
            if op.param2 in Fiazie:
                pass
            else:
                if op.param2 not in Setmain["Rblacklist"]:
                    Setmain["Rblacklist"][op.param2] = True
                    f=codecs.open('setting2.json','w','utf-8')
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                try:
                    ki.findAndAddContactsByMid(op.param3)
                    ki.kickoutFromGroup(op.param1,[op.param2])
                    ki.inviteIntoGroup(op.param1,Botku)
                    ks.kickoutFromGroup(op.param1,[op.param2])
                    kk.cancelGroupInvitation(op.param1,[op.param2])
                except:
                    try:
                        kk.findAndAddContactsByMid(op.param3)
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,Botku)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Botku)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            ks.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ks.findAndAddContactsByMid(op.param3)
                                ks.kickoutFromGroup(op.param1,[op.param2])
                                ks.inviteIntoGroup(op.param1,Botku)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,Botku)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,Botku)
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            cl.findAndAddContactsByMid(op.param3)
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,Botku)
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                            ka.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                random.choice(All).findAndAddContactsByMid(op.param3)
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(All).inviteIntoGroup(op.param1,Botku)
                                                random.choice(All).acceptGroupInvitation(op.param1)
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(All).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                pass
            return

        if op.type == 11:
            if op.param1 in Setmain["Rprotqr"]:
                try:
                    if ki.getGroup(op.param1).preventedJoinByTicket == True:
                        if op.param2 not in Fiazie:
                            Setmain["Rblacklist"][op.param2] = True
                            f=codecs.open('setting2.json','w','utf-8')
                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.reissueGroupTicket(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = False
                            ki.updateGroup(X)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if kk.getGroup(op.param1).preventedJoinByTicket == True:
                            if op.param2 not in Fiazie:
                                Setmain["Rblacklist"][op.param2] = True
                                f=codecs.open('setting2.json','w','utf-8')
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                kk.reissueGroupTicket(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = False
                                kk.updateGroup(X)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if kc.getGroup(op.param1).preventedJoinByTicket == True:
                                if op.param2 not in Fiazie:
                                    Setmain["Rblacklist"][op.param2] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kc.reissueGroupTicket(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = False
                                    kc.updateGroup(X)
                                    ks.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if ks.getGroup(op.param1).preventedJoinByTicket == True:
                                    if op.param2 not in Fiazie:
                                        Setmain["Rblacklist"][op.param2] = True
                                        f=codecs.open('setting2.json','w','utf-8')
                                        json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        ks.reissueGroupTicket(op.param1)
                                        X = ks.getGroup(op.param1)
                                        X.preventedJoinByTicket = False
                                        ks.updateGroup(X)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if ka.getGroup(op.param1).preventedJoinByTicket == True:
                                        if op.param2 not in Fiazie:
                                            Setmain["Rblacklist"][op.param2] = True
                                            f=codecs.open('setting2.json','w','utf-8')
                                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            ka.reissueGroupTicket(op.param1)
                                            X = ka.getGroup(op.param1)
                                            X.preventedJoinByTicket = False
                                            ka.updateGroup(X)
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == True:
                                            if op.param2 not in Fiazie:
                                                Setmain["Rblacklist"][op.param2] = True
                                                f=codecs.open('setting2.json','w','utf-8')
                                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = False
                                                kb.updateGroup(X)
                                                ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

            if op.param2 in Setmain["Rblacklist"]:
                try:
                    if ki.getGroup(op.param1).preventedJoinByTicket == True:
                        if op.param2 not in Fiazie:
                            Setmain["Rblacklist"][op.param2] = True
                            f=codecs.open('setting2.json','w','utf-8')
                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                            ki.reissueGroupTicket(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = False
                            ki.updateGroup(X)
                            kk.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if kk.getGroup(op.param1).preventedJoinByTicket == True:
                            if op.param2 not in Fiazie:
                                Setmain["Rblacklist"][op.param2] = True
                                f=codecs.open('setting2.json','w','utf-8')
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                kk.reissueGroupTicket(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = False
                                kk.updateGroup(X)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if kc.getGroup(op.param1).preventedJoinByTicket == True:
                                if op.param2 not in Fiazie:
                                    Setmain["Rblacklist"][op.param2] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kc.reissueGroupTicket(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = False
                                    kc.updateGroup(X)
                                    ks.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if ks.getGroup(op.param1).preventedJoinByTicket == True:
                                    if op.param2 not in Fiazie:
                                        Setmain["Rblacklist"][op.param2] = True
                                        f=codecs.open('setting2.json','w','utf-8')
                                        json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                        ks.reissueGroupTicket(op.param1)
                                        X = ks.getGroup(op.param1)
                                        X.preventedJoinByTicket = False
                                        ks.updateGroup(X)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if ka.getGroup(op.param1).preventedJoinByTicket == True:
                                        if op.param2 not in Fiazie:
                                            Setmain["Rblacklist"][op.param2] = True
                                            f=codecs.open('setting2.json','w','utf-8')
                                            json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            ka.reissueGroupTicket(op.param1)
                                            X = ka.getGroup(op.param1)
                                            X.preventedJoinByTicket = False
                                            ka.updateGroup(X)
                                            ks.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if kb.getGroup(op.param1).preventedJoinByTicket == True:
                                            if op.param2 not in Fiazie:
                                                Setmain["Rblacklist"][op.param2] = True
                                                f=codecs.open('setting2.json','w','utf-8')
                                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                                kb.reissueGroupTicket(op.param1)
                                                X = kb.getGroup(op.param1)
                                                X.preventedJoinByTicket = False
                                                kb.updateGroup(X)
                                                ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 22:
            if mid in op.param3:
                if Setmain["Rautojoin"] == True:
                    cl.leaveRoom(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        cl.acceptGroupInvitation(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        if cl.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Amid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        ki.acceptGroupInvitation(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        if ki.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                                ki.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Bmid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        kk.acceptGroupInvitation(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        if kk.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Cmid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        kc.acceptGroupInvitation(op.param1)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        if kc.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Dmid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        ks.acceptGroupInvitation(op.param1)
                        ks.leaveGroup(op.param1)
                    else:
                        ks.acceptGroupInvitation(op.param1)
                        if ks.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                ks.cancelGroupInvitation(op.param1,[op.param2])
                                ks.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Emid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        ka.acceptGroupInvitation(op.param1)
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        if ka.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                                ka.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass
            if Fmid in op.param3:
                if Setmain["Rautojoin"] == True:
                    if op.param2 not in Fiazie:
                        kb.acceptGroupInvitation(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        if kb.getGroup(op.param1):
                          if op.param2 in Setmain["Rblacklist"]:
                            if op.param2 not in Fiazie:
                              try:
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                kb.kickoutFromGroup(op.param1,[op.param2])
                              except:
                                  pass

        if op.type == 13:#NOTIFIED_INVITE_INTO_GROUP
            if op.param1 in Setmain["Rprotinvite"]:
                if op.param2 in Fiazie:
                    pass
                else:
                    Setmain["Rblacklist"][op.param2] = True
                    f=codecs.open('setting2.json','w','utf-8')
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    anu = random.choice(All).getCompactGroup(op.param1)
                    if anu.invitee is not None:
                        pipo = [a.mid for a in anu.invitee]
                        for target in pipo:
                            if target in op.param3:
                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                                random.choice(All).cancelGroupInvitation(op.param1,[target])
                        random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                        targets = [op.param2]
                        for target in targets:
                            if target in Setmain["Rblacklist"]:
                                pass
                            else:
                                Setmain["Rblacklist"].append(target)
                                with codecs.open("setting2.json",'w','utf-8') as f:
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)

            if op.param2 in Setmain["Rblacklist"]:
                if op.param2 not in Fiazie:
                    try:
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.cancelGroupInvitation(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                                ks.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ks.cancelGroupInvitation(op.param1,[op.param3])
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.cancelGroupInvitation(op.param1,[op.param3])
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.cancelGroupInvitation(op.param1,[op.param3])
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                cl.cancelGroupInvitation(op.param1,[op.param3])
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                random.choice(All).cancelGroupInvitation(op.param1,[op.param3])
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])

            if op.param3 in Setmain["Rblacklist"]:
                if op.param3 not in Fiazie and op.param2 not in Fiazie:
                    try:
                        ki.cancelGroupInvitation(op.param1,[op.param3])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kk.cancelGroupInvitation(op.param1,[op.param3])
                            kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param3])
                                ks.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    ks.cancelGroupInvitation(op.param1,[op.param3])
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.cancelGroupInvitation(op.param1,[op.param3])
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.cancelGroupInvitation(op.param1,[op.param3])
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                cl.cancelGroupInvitation(op.param1,[op.param3])
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                random.choice(All).cancelGroupInvitation(op.param1,[op.param3])
                                                random.choice(All).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 15:
            if op.param1 in Setmain["byemsg"]:
                if op.param2 in Fiazie:
                    return
                else:
                    cl.sendText(op.param1, Setmain["leftmsg"])

        if op.type == 17:
            if op.param2 in Setmain["Rblacklist"]:
                try:
                    random.choice(All).kickoutFromGroup(op.param1,[op.param2])
                except:
                    pass

            if op.param1 in Setmain["Rgreet"]:
                if op.param2 not in Fiazie:
                    ginfo = cl.getGroup(op.param1)
                    user = cl.getContact(op.param2)
                    cl.sendText(op.param1,"Welcome at" + str(ginfo.name))
            if op.param1 in Setmain["proJoin"]:
                if op.param2 in RTeam:
                    pass
                if op.param2 not in Setmain["Rblacklist"]:
                    pass
                else:
                    try:
                        if op.param3 in Setmain["Rblacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 in Setmain["Rblacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 in Setmain["Rblacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 in Setmain["Rblacklist"]:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 in Setmain["Rblacklist"]:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 in Setmain["Rblacklist"]:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 in Setmain["Rblacklist"]:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                pass
                return
        if op.type == 19:
            if op.param1 in Setmain["Rprotkick"]:
                if op.param2 not in Fiazie:
                    Setmain["Rblacklist"][op.param2] = True
                    f=codecs.open('setting2.json','w','utf-8')
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        if op.param3 not in Setmain["Rblacklist"]:
                            contact = ki.getContact(op.param3)
                            ki.findAndAddContactsByMid(contact.mid)
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in Setmain["Rblacklist"]:
                                contact = kk.getContact(op.param3)
                                kk.findAndAddContactsByMid(contact.mid)
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 not in Setmain["Rblacklist"]:
                                    contact = kc.getContact(op.param3)
                                    kc.findAndAddContactsByMid(contact.mid)
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 not in Setmain["Rblacklist"]:
                                        contact = ks.getContact(op.param3)
                                        ks.findAndAddContactsByMid(contact.mid)
                                        ks.cancelGroupInvitation(op.param1,[op.param2])
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param3 not in Setmain["Rblacklist"]:
                                            contact = ka.getContact(op.param3)
                                            ka.findAndAddContactsByMid(contact.mid)
                                            ka.cancelGroupInvitation(op.param1,[op.param2])
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            if op.param3 not in Setmain["Rblacklist"]:
                                                contact = kb.getContact(op.param3)
                                                kb.findAndAddContactsByMid(contact.mid)
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            if op.param3 not in Setmain["Rblacklist"]:
                                                contact = cl.getContact(op.param3)
                                                cl.findAndAddContactsByMid(contact.mid)
                                                cl.cancelGroupInvitation(op.param1,[op.param2])
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 32:
            if op.param1 in Setmain["Rprotcancel"]:
                if op.param2 not in Fiazie:
                    Setmain["Rblacklist"][op.param2] = True
                    f=codecs.open('setting2.json','w','utf-8')
                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        if op.param3 not in Setmain["Rblacklist"]:
                            contact = ki.getContact(op.param3)
                            ki.findAndAddContactsByMid(contact.mid)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            if op.param3 not in Setmain["Rblacklist"]:
                                contact = kk.getContact(op.param3)
                                kk.findAndAddContactsByMid(contact.mid)
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 not in Setmain["Rblacklist"]:
                                    contact = kc.getContact(op.param3)
                                    kc.findAndAddContactsByMid(contact.mid)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 not in Setmain["Rblacklist"]:
                                        contact = ks.getContact(op.param3)
                                        ks.findAndAddContactsByMid(contact.mid)
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                        ks.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param3 not in Setmain["Rblacklist"]:
                                            contact = ka.getContact(op.param3)
                                            ka.findAndAddContactsByMid(contact.mid)
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            if op.param3 not in Setmain["Rblacklist"]:
                                                contact = kb.getContact(op.param3)
                                                kb.findAndAddContactsByMid(contact.mid)
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            if op.param3 not in Setmain["Rblacklist"]:
                                                contact = cl.getContact(op.param3)
                                                cl.findAndAddContactsByMid(contact.mid)
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
        if op.type == 46:
            if op.param2 in Botku:
                cl.removeAllMessages()
                ki.removeAllMessages()
                kk.removeAllMessages()
                kc.removeAllMessages()
                ks.removeAllMessages()
                ka.removeAllMessages()
                kb.removeAllMessages()

        if op.type == 55:
            if op.param1 in Setmain["RreadPoint"]:
                if op.param2 in Setmain["RreadMember"][op.param1]:
                    pass
                else:
                    Setmain["RreadMember"][op.param1][op.param2] = True
            else:
                pass

        if op.type == 26:
                msg = op.message
                if msg.to in Setmain["RreadPoint"]:
                    if msg._from in Setmain["RreadMember"][msg.to]:
                        pass
                    else:
                        Setmain["RreadMember"][msg.to][msg._from] = True
                else:
                    pass        

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.contentType == 13:
                    if msg.to in Setmain["Rautoscan"]:
                        msg.contentType = 0
                        cl.sendMessage(msg.to,"Mid " +msg.contentMetadata["mid"])
                    if msg._from in Fiaku:
                        if msg.to in Setmain["Rwblacklist"]:
                            if msg.contentMetadata["mid"] in Setmain["Rblacklist"]:
                                cl.sendMessageWithMention(msg.to,msg.contentMetadata["mid"],"User","In Blcaklist")
                            else:
                                Setmain["Rblacklist"][msg.contentMetadata["mid"]] = True
                                f=codecs.open('setting2.json','w','utf-8')
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendMessageWithMention(msg.to,msg.contentMetadata["mid"],"User","Was Blacklist")
                        elif msg.to in Setmain["Rdblacklist"]:
                            if msg.contentMetadata["mid"] in Setmain["Rblacklist"]:
                                del Setmain["Rblacklist"][msg.contentMetadata["mid"]]
                                f=codecs.open('setting2.json','w','utf-8')
                                json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendMessageWithMention(msg.to,msg.contentMetadata["mid"],"User","Was Deleted In Blacklist")
                            else:
                                cl.sendMessageWithMention(msg.to,msg.contentMetadata["mid"],"User","Contact not In Blacklist")

                elif msg.contentType == 1:
                    if msg._from in Fiaku or msg._from in Zie:
                        if msg.to in Setmain["Rfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            path1 = ki.downloadObjectMsg(msg_id)
                            path2 = kk.downloadObjectMsg(msg_id)
                            path3 = kc.downloadObjectMsg(msg_id)
                            path4 = ks.downloadObjectMsg(msg_id)
                            path5 = ka.downloadObjectMsg(msg_id)
                            path6 = kb.downloadObjectMsg(msg_id)
                            cl.updateProfilePicture(path)
                            ki.updateProfilePicture(path1)
                            kk.updateProfilePicture(path2)
                            kc.updateProfilePicture(path3)
                            ks.updateProfilePicture(path4)
                            ka.updateProfilePicture(path5)
                            kb.updateProfilePicture(path6)
                            del Setmain["Rfoto"][msg.to]
                            cl.sendMessage(msg.to, "Succes")
                        elif mid in Setmain["Rfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Succes")
                        elif Amid in Setmain["Rfoto"]:
                            path1 = ki.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Amid]
                            ki.updateProfilePicture(path1)
                            ki.sendMessage(msg.to,"Succes")
                        elif Bmid in Setmain["Rfoto"]:
                            path2 = kk.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Bmid]
                            kk.updateProfilePicture(path2)
                            kk.sendMessage(msg.to,"Succes")
                        elif Cmid in Setmain["Rfoto"]:
                            path3 = kc.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Cmid]
                            kc.updateProfilePicture(path3)
                            kc.sendMessage(msg.to,"Sucess")
                        elif Dmid in Setmain["Rfoto"]:
                            path4 = ks.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Dmid]
                            ks.updateProfilePicture(path4)
                            ks.sendMessage(msg.to,"Succes")
                        elif Emid in Setmain["Rfoto"]:
                            path5 = ka.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Emid]
                            ka.updateProfilePicture(path5)
                            ka.sendMessage(msg.to,"Succes")
                        elif Fmid in Setmain["Rfoto"]:
                            path6 = kb.downloadObjectMsg(msg_id)
                            del Setmain["Rfoto"][Fmid]
                            kb.updateProfilePicture(path6)
                            kb.sendMessage(msg.to,"Succes")
                        elif msg.toType == 2:
                            if msg._from in Fiaku:
                                if msg.to in Setmain["RGfoto"]:
                                    path = cl.downloadObjectMsg(msg_id)
                                    del Setmain["RGfoto"][msg.to]
                                    cl.updateGroupPicture(msg.to, path)
                                    cl.sendMessage(msg.to, "Succes")

                elif msg.contentType == 0:
                    if msg.to in Setmain["Rautoread"]:
                        ki.sendChatChecked(msg.to, msg_id)
                        kk.sendChatChecked(msg.to, msg_id)
                        kc.sendChatChecked(msg.to, msg_id)
                        ks.sendChatChecked(msg.to, msg_id)
                        ka.sendChatChecked(msg.to, msg_id)
                        kb.sendChatChecked(msg.to, msg_id)
                    if text is None:    
                        return
                    else:

#===========================================================#

                        if text.lower() == "help":
                            if msg._from in Fiaku or msg._from in Zie:
                                md = "===>SELFBOT [SUNDANESE] VERSION<===\n\n"
                                md += "me\n"
                                md += "runtime\n"
                                md += "respon\n"
                                md += ".sp \n"
                                md += "sp\n"
                                md += "ourl\n"
                                md += "curl\n"
                                md += "all cn: \n"
                                md += "up pictbot\n"
                                md += ". cban\n"
                                md += "cleanse\n"
                                md += "/relogin\n"
                                md += "rechat\n"
                                md += "tendang @\n"
                                md += ".inv\n"
                                md += "masuk\n"
                                md += ".left\n"
                                md += "pulang\n"
                                md += "banlist\n"
                                md += "setting\n"
                                md += "autojoin on:off\n"
                                md += "proinvite on:off\n"
                                md += "proqr on:off\n"
                                md += "procancel on:off\n"
                                md += "prokick on:off\n"
                                md += "projoin on:off\n"
                                md += "allprotect on:off\n"
                                md += "welcome on:off\n"
                                md += "==>line.me/ti/p/~fiazie83<=="
                                cl.sendMessage(msg.to, md)
                            else:
                                md = "===>SELFBOT [[SUNDANESE]] VERSION<===\n\n"
                                md += "info\n"
                                md += "id\n"
                                md += "banlist\n"
                                md += "ginfo\n"
                                md += "gname:\n"
                                md += "==>line.me/ti/p/~fiazie83<=="
                                cl.sendMessage(msg.to, md)

                        elif text.lower() == "setting":
                            if msg._from in Fiaku or msg._from in Zie:
                                g = ki.getGroup(msg.to)
                                md = "Group Setting {}\n\n".format(str(g.name))
                                if msg.to in Setmain["Rwblacklist"]: md+="[+] Blacklist\n"
                                else: md+="[-] Blacklist\n"
                                if msg.to in Setmain["Rdblacklist"]: md+="[+] Unblacklist\n"
                                else: md+="[-] Unblacklist\n"
                                if msg.to in Setmain["Rautoscan"]: md+="[+] Cek mid\n"
                                else: md+="[-] Cek mid\n"
                                if Setmain["Rautojoin"] == True: md+="[+] Auto Join\n"
                                else: md+="[-] Auto Join\n"
                                if msg.to in Setmain["Rautoread"]: md+="[+] Autoread\n"
                                else: md+="[-] Autoread\n"
                                if msg.to in Setmain["Rprotinvite"]: md+="[+] protect inivte\n"
                                else: md+="[-] protect invite\n"
                                if msg.to in Setmain["Rprotqr"]: md+="[+] protect Qr\n"
                                else: md+="[-] protect Qr\n"
                                if msg.to in Setmain["Rprotkick"]: md+="[+] auto kick \n"
                                else: md+="[-] auto kick \n" 
                                if msg.to in Setmain["Rprotcancel"]: md+="[+] protect cancel\n"
                                else: md+="[-] protect cancel\n"
                                if msg.to in Setmain["proJoin"]: md+="[+] protect Join\n"
                                else: md+="[-] protect Join\n"
                                if msg.to in Setmain["Rgreet"]: md+="[+] welcome\n"
                                else: md+="[-] welcome\n"
                                cl.sendMessage(msg.to,md)

                        elif text.lower() == "proinvite:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rprotinvite"]:
                                    cl.sendMessage(msg.to,"was on")
                                else:
                                    Setmain["Rprotinvite"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protect Invitation on")

                        elif text.lower() == "proinvite:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rprotinvite"]:
                                    cl.sendMessage(msg.to,"Unactiv")
                                else:
                                    del Setmain["Rprotinvite"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to,"protect Invitation off")

                        elif text.lower() == "autojoin:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rautojoin"]:
                                    cl.sendMessage(msg.to,"was on")
                                else:
                                    Setmain["Rautojoin"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "AutoJoin on")

                        elif text.lower() == "autojoin:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rautojoin"]:
                                    cl.sendMessage(msg.to,"was off")
                                else:
                                    del Setmain["Rautojoin"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Autojoin off")

                        elif text.lower() == "proqr:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rprotqr"]:
                                    cl.sendMessage(msg.to,"was on")
                                else:
                                    Setmain["Rprotqr"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protection Qr on")

                        elif text.lower() == "proqr:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rprotqr"]:
                                    cl.sendMessage(msg.to,"Unactiv")
                                else:
                                    del Setmain["Rprotqr"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protection Qr off")

                        elif text.lower() == "procancel:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rprotcancel"]:
                                    cl.sendMessage(msg.to, "was on")
                                else:
                                    Setmain["Rprotcancel"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to,"Protect Cancel on")

                        elif text.lower() == "procancel:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rprotcancel"]:
                                    cl.sendMessage(msg.to, msg._from,"","Unactiv")
                                else:
                                    del Setmain["Rprotcancel"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protect Cancel off")

                        elif text.lower() == "projoin:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["proJoin"]:
                                    cl.sendMessage(msg.to, "was on")
                                else:
                                    Setmain["proJoin"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to,"Protect Join on")

                        elif text.lower() == "projoin:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["proJoin"]:
                                    cl.sendMessage(msg.to, msg._from,"","Unactiv")
                                else:
                                    del Setmain["proJoin"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protect Join off")

                        elif text.lower() == "prokick:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rprotkick"]:
                                    cl.sendMessage(msg.to,"was on")
                                else:
                                    Setmain["Rprotkick"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protect kick on")

                        elif text.lower() == "prokick:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rprotkick"]:
                                    cl.sendMessage(msg.to, "Unactiv")
                                else:
                                    del Setmain["Rprotkick"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to, "Protect kick off")

                        elif text.lower() == "banlist" or text.lower() == 'banlist':
                            if msg._from in Fiaku or msg._from in Zie:
                              if Setmain["Rblacklist"] == {}:
                                cl.sendMessage(msg.to,"not user blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in Setmain["Rblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + "> " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"User in Blacklist \n"+ma+"\n %s Blacklist " %(str(len(Setmain["Rblacklist"]))))

                        elif text.lower() == "cban" or text.lower() == 'clearban':
                            if msg._from in Fiaku or msg._from in Zie:
                              Setmain["Rblacklist"] = {}
                              ragets = cl.getContacts(Setmain["Rblacklist"])
                              mc = "%i Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"done clear " +mc+ "Blacklist")    

                        elif text.lower() == "allprotect:on":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to in Setmain["Rprotqr"] or msg.to in Setmain["Rprotcancel"] or msg.to in Setmain["Rprotkick"] or msg.to in Setmain["Rprotinvite"]:
                                    cl.sendMessage(msg.to,"was hight all protection")
                                else:
                                    Setmain["Rprotqr"][msg.to] = True
                                    Setmain["Rprotcancel"][msg.to] = True
                                    Setmain["Rprotkick"][msg.to] = True
                                    Setmain["Rprotinvite"][msg.to] = True
                                    Setmain["proJoin"][msg.to] = True
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to,"AllProtection on")

                        elif text.lower() == "allprotect:off":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.to not in Setmain["Rprotqr"] or msg.to not in Setmain["Rprotcancel"] or msg.to not in Setmain["Rprotkick"] or msg.to not in Setmain["Rprotinvite"]:
                                    cl.sendMessage(msg.to,"UnProtection this Group")
                                else:
                                    del Setmain["Rprotqr"][msg.to]
                                    del Setmain["Rprotcancel"][msg.to]
                                    del Setmain["Rprotkick"][msg.to]
                                    del Setmain["Rprotinvite"][msg.to]
                                    del Setmain["proJoin"][msg.to]
                                    f=codecs.open('setting2.json','w','utf-8')
                                    json.dump(Setmain, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendMessage(msg.to,"AllProtection off")            

                        elif text.lower() == ".left":
                            if msg._from in Fiaku or msg._from in Zie:
                                if msg.toType == 2:
                                    x = cl.getGroup(msg.to)
                                    cl.leaveGroup(msg.to)

                        elif text.lower() == 'me':
                            if msg._from in Fiaku or msg._from in Zie:
                                cl.sendContact(msg.to,msg._from)

                        elif text.lower() == "respon":
                            if msg._from in Fiaku or msg._from in Zie:
                                ki.sendMessage(msg.to,"siap")
                                kk.sendMessage(msg.to,"siap")
                                kc.sendMessage(msg.to,"siap")
                                ks.sendMessage(msg.to,"siap")
                                ka.sendMessage(msg.to,"siap")
                                kb.sendMessage(msg.to,"siap")

                        elif text.lower() == ".sp":
                            if msg._from in Fiaku or msg._from in Zie:
                                start1 = time.time()
                                ki.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start1
                                ki.sendMessage(msg.to, "%s-s" % (elapsed_time))

                                start2 = time.time()
                                kk.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start2
                                kk.sendMessage(msg.to, "%s-s" % (elapsed_time))

                                start3 = time.time()
                                kc.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start3
                                kc.sendMessage(msg.to, "%s-s" % (elapsed_time))

                                start4 = time.time()
                                ks.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start4
                                ks.sendMessage(msg.to, "%s-s" % (elapsed_time))

                                start5 = time.time()
                                ka.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start5
                                ka.sendMessage(msg.to, "%s" % (elapsed_time))

                                start6 = time.time()
                                kb.sendMessage("u1bc853a4855bb690bb17b3ac42b8b05c", '.')
                                elapsed_time = time.time() - start6
                                kb.sendMessage(msg.to, "%s" % (elapsed_time))

                        elif "all cn:" in text.lower():
                            if msg._from in Fiaku or msg._from in Zie:
                                proses = text.split(":")
                                string = text.replace(proses[0] + ":","")
                                profile_AA = cl.getProfile()
                                profile_A = ki.getProfile()
                                profile_B = kk.getProfile()
                                profile_C = kc.getProfile()
                                profile_D = ks.getProfile()
                                profile_E = ka.getProfile()
                                profile_F = kb.getProfile()
                                profile_AA.displayName = string
                                profile_A.displayName = string
                                profile_B.displayName = string
                                profile_C.displayName = string
                                profile_D.displayName = string
                                profile_E.displayName = string
                                profile_F.displayName = string
                                cl.updateProfile(profile_AA)
                                ki.updateProfile(profile_A)
                                kk.updateProfile(profile_B)
                                kc.updateProfile(profile_C)
                                ks.updateProfile(profile_D)
                                ka.updateProfile(profile_E)
                                kb.updateProfile(profile_F)
                                cl.sendMessage(msg.to,"succes up to : {}".format(str(string)))

                        elif text.lower() == "up pictbot":
                            if msg._from in Fiaku or msg._from in Zie:
                                Setmain["Rfoto"][msg.to] = True
                                Setmain["Rfoto"][Amid] = True
                                Setmain["Rfoto"][Bmid] = True
                                Setmain["Rfoto"][Cmid] = True
                                Setmain["Rfoto"][Dmid] = True
                                Setmain["Rfoto"][Emid] = True
                                Setmain["Rfoto"][Fmid] = True
                                cl.sendMessage(msg.to,"send pict")

                        elif text.lower() == "cban" or text.lower() == 'clearban':
                            if msg._from in Fiaku or msg._from in Zie:
                              Setmain["Rblacklist"] = {}
                              ragets = cl.getContacts(Setmain["Rblacklist"])
                              mc = "%i Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"done clear" +mc+ "Blacklist")

                        elif text.lower() == "/relogin":
                            if msg._from in Fiaku or msg._from in Zie:
                                cl.sendMessage(msg.to, "waiting in progres....")
                                python3 = sys.executable
                                os.execl(python3, python3, *sys.argv)

                        elif text.lower() == "rechat":
                            if msg._from in Fiaku or msg._from in Zie:
                                try:
                                    ki.removeAllMessages(op.param2)
                                    ki.sendMessage(msg.to,"done")
                                    kk.removeAllMessages(op.param2)
                                    kk.sendMessage(msg.to,"done")
                                    kc.removeAllMessages(op.param2)
                                    kc.sendMessage(msg.to,"done")
                                    ks.removeAllMessages(op.param2)
                                    ks.sendMessage(msg.to,"done")
                                    ka.removeAllMessages(op.param2)
                                    ka.sendMessage(msg.to,"done")
                                    kb.removeAllMessages(op.param2)
                                    kb.sendMessage(msg.to,"done")
                                    cl.removeAllMessages(op.param2)
                                    cl.sendMessage(msg.to,"done")
                                except:
                                    pass        
                        elif text.lower() == ".inv":
                            if msg._from in Fiaku or msg._from in Zie:
                                try:
                                    bot = [Amid,Bmid,Cmid,Dmid,Emid,Fmid]
                                    cl.inviteIntoGroup(msg.to, bot)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ks.acceptGroupInvitation(msg.to)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif text.lower() == "masuk" or text.lower() == ".go":
                            if msg._from in Fiaku or msg._from in Zie:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif text.lower() == "pulang" or text.lower() == ".out":
                            if msg._from in Fiaku or msg._from in Zie:
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ks.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)

                        elif "tendang" in text.lower():
                            if msg._from in Fiaku or msg._from in Zie:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Fiazie:
                                        pass
                                    else:
                                        try:
                                            klist = [ki,kk,kc,ks,ka,kb]
                                            kicker = random.choice(klist)
                                            kicker.kickoutFromGroup(msg.to,[target])
                                            Setmain["Rblacklist"][target] = True
                                        except Exception as e:
                                            cl.sendMessage(msg.to, "Limit")

            #---------------- Fungsi Remote Command ------------------#
       
                        elif '/ti/g/' in msg.text.lower():
                            if msg._from in Fiaku or msg._from in Zie:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Setmain["Rautojoin"] == True:
                                        ra = cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ki.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kk.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kc.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ks.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        ka.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                        kb.acceptGroupInvitationByTicket(ra.id,ticket_id)
                                    else:    
                                        cl.sendMessage(msg.to,"autoJoin not activ")

    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
