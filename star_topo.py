from mininet.topo import Topo


class Star_Topology(Topo):
    def build(self):

        # Creating hosts
        host1 = self.addHost("h1")
        host2 = self.addHost("h2")
        host3 = self.addHost("h3")
        host4 = self.addHost("h4")
        host5 = self.addHost("h5")

        # Creating switch
        switch1 = self.addSwitch("s1")

        # Creating links between host and switch
        self.addLink(host1, switch1)
        self.addLink(host2, switch1)
        self.addLink(host3, switch1)
        self.addLink(host4, switch1)
        self.addLink(host5, switch1)


# Creating a dict for initializing the topology
topos = {"star_topo": (lambda: Star_Topology())}
