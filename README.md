# Bose-Soundbar-hacking-Python
Hack Bose sound bar with Python

here in this Blog I am going to share the power of python. soon I am also making a UI which people and researchers can use to PenTest IoT devices.

I want to Thank following people for contribution
CharlesBlonde

I have just made Library on top of what CharlesBlonde has done

# step1:  Discover The Speakers
D = Bose_Discover()
print(D.Find_Devices())

# step 2:
Note the IP address and lets starts Hacking we can run following attacks

Change Music
Set the volume
See Which song is Being played.
Run a Denial of Service Attack

c = Bose_Hack(ip="IP ADDRESS GOES HERE ")
print(c.status())
print(c.next_track())
print(c.denialofserviceattack())
