import subprocess
import optparse

def change_mac(interface,new_mac):
    print("[+] Changing MAC adress for"+interface+"to"+new_mac)
    subprocess.call(["ifcoming",interface,"down"])
    subprocess.call(["ifcoming",interface,"hw","ether",new_mac])
    subprocess.call(["ifcoming",interface,"up"])

parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface to change its Mac-adress")
parser.add_option("-m","--mac",dest="new mac",help="New Mac adress")

(options,arguments)=parser.parse_args()

change_mac(options.interface,options.new_mac)