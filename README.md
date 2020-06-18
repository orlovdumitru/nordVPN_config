
terminal interface connecting to NordVPN using OpenVPN. Allow user select from over 11k vpns offered by NordVPN

https://support.nordvpn.com/Connectivity/Linux/1047409422/How-can-I-connect-to-NordVPN-using-Linux-Terminal.htm
1) OpenVPN must be installed:
    sudo apt-get install openvpn

2) navigate to openvpn folder and create a nordVPN folder
    cd /etc/openvpn
    sudo mdir nodrVPN
    cd nordVPN

3) get a list of nodVPN:
    sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip

4) unzip donwloaded file:
    sudo unzip ovpn.zip

5) remove zip file:
    sudo rm ovpn.zip

6) now nordVPN will have over 11k files, need to be sorted:
    sudo python3 file_manager.py

7) all folders will have 2 letter characters to change to country name use country_codes.py:
    sudo python3 country_codes.py

8) connect to vpn:
    python3 run.py

if vpn need to be stoped run [python3 run.py] and will offer option to kill all [openvpn] important to know if system go to sleep and vpn was not stoped, after sleep sesion may result in not internet connection error do a [python3 run.py] and select to kill all openvpns