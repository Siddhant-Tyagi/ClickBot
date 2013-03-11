import socks
import socket
import os
import cookielib
import mechanize
from random import *
from time import *
import TorCtl
conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="123")

def create_mac():
    f = open("mac",'r')
    li = f.readlines()
    for i in range(0,len(li)):
        li[i] = li[i].strip("\n")
    shuffle(li)
    mac_list = li


def visit(url):
    #NewMAC()
    NewTorIP()
    #import socks
    #import socket
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    #import urllib2
    #import cookielib
    #import mechanize
    #def visit(url):
    unvisited = []
    count = 0
    #visited = []
    agent = choice(user_agent)
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_referer(True)
    br.set_handle_redirect(True)
    br.set_handle_robots(False)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [("Content-type", "text/html; charset=utf-8")]
    br.addheaders = [('User-agent', agent)]
    r = br.open(url)
    count = count + 1
    #visited.append(url)
    for l in br.links(url_regex='scionfrssite.blogspot'):
        unvisited.append(l)
    sleep(randrange(12,35))
    print "length: " + str(len(unvisited))
    for i in range(0,randrange(1,len(unvisited))):
        br.follow_link(unvisited.pop(randrange(0,len(unvisited))))
        count = count + 1
        print count
        sleep(randrange(12,25))
    cj.clear()
    br.close()

def NewTorIP():
    TorCtl.Connection.send_signal(conn, "NEWNYM")


def NewMAC():
    r = choice(mac_list)
    cmd = "sudo ifconfig eth1 hw ether " + r
    os.system(cmd)
    

def user_agent_list():
    f = open("user_agents",'r')
    us_ag = f.readlines()
    for e in range(0,len(us_ag)):
        us_ag[e] = us_ag[e].strip("\n")
    f.close()
    return us_ag
    #agent_list = us_ag

user_agent = user_agent_list()


#def main():
#    clicks = rawinput("Number of external clicks")
#    clicks = int(clicks)
#    internal_clicks = 0
#    us_ag = user_agent_list()
#    url = ??
#    for i in range(1,clicks):
#        agent = choice(us_ag)
#        visit(url, agent)

#if __name__ == '__main__':
#      main()
