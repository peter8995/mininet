#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Host
from mininet.cli import CLI
from mininet.link import TCLink, Intf
from mininet.log import setLogLevel, info
from subprocess import call

def myNetwork():

    net = Mininet()
    h2 = net.addHost('h2')
    h1 = net.addHost('h1')

    info( '*** Add links\n')    
    net.addLink(h1, h2)

    info( '*** Starting network\n')
    net.build()

    CLI(net)
    net.stop()

if name == 'main':
    setLogLevel( 'info' )
    myNetwork()
