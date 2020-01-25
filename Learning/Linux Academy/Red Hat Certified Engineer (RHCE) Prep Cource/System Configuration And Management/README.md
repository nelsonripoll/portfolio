# Red Hat Certified Engineer (RHCE) Prep Cource

## System Configuration and Management Labs

### Systemctl Notes

#### Start and Enable

When you start a service, it will be running until the system is powered down or
 rebooted, the service will no longer be running. You have to enable the service
 so that it persists through a reboot. Example given with the **firewalld**
 service.

```
# systemctl start firewalld
# systemctl enable firewalld
Created symlink /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service → /usr/lib/systemd/system/firewalld.service.
Created symlink /etc/systemd/system/multi-user.target.wants/firewalld.service → /usr/lib/systemd/system/firewalld.service.
```

#### Stop and Disable
To undo the actions of start and enable, you can stop and disable. Stopping a
 service will only stop it until it is started or until the system is rebooted
 (assuming the service has been enabled).

```
# systemctl stop firewalld
# systemctl disable firewalld
Removed /etc/systemd/system/multi-user.target.wants/firewalld.service.
Removed /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service.
```

#### Restart and Reload
To restart a running service, you can use the restart command. If the application
 in question is able to reload its configuration files, you can use the reload
 command without having the service stop. If you do not know if the service can
 reload its configuration, you can use the reload-or-restart command.

```
# systemctl restart firewalld
# systemctl reload firewalld
# systemctl reload-or-restart firewalld
```

#### Status
Checking the status of a service will provide you with the service state, the 
 cgroup hierarchy, and the first few log lines.

```
# systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; disabled; vendor preset: enabled)
   Active: active (running) since Sat 2020-01-25 09:49:20 CST; 27s ago
     Docs: man:firewalld(1)
  Process: 6429 ExecReload=/bin/kill -HUP $MAINPID (code=exited, status=0/SUCCESS)
 Main PID: 5454 (firewalld)
    Tasks: 3 (limit: 26213)
   Memory: 30.6M
   CGroup: /system.slice/firewalld.service
           └─5454 /usr/libexec/platform-python -s /usr/sbin/firewalld --nofork --nopid

Jan 25 09:49:20 DESKTOP-CDAHF4O.lan1 systemd[1]: Starting firewalld - dynamic firewall daemon...
Jan 25 09:49:20 DESKTOP-CDAHF4O.lan1 systemd[1]: Started firewalld - dynamic firewall daemon.
...
```

#### Mask and Unmask

Masking a service will make it completely unstartable, automatically or manually,
 by linking it to **/dev/null**.

```
# systemctl mask firewalld
Created symlink /etc/systemd/system/firewalld.service → /dev/null.
# systemctl list-unit-files | grep firewalld
firewalld.service       masked 
# systemctl unmask firewalld
Removed /etc/systemd/system/firewalld.service.
```


### Configure IPv4 and IPv6 Addresses

#### IPv4 vs IPv6

Internet Protocol version 4 (IPv4) is the fourth version of the Internet Protocol
 (IP). Version 6 (IPv6) is the most recent and was created to address the
 long-anticipated problem of IPv4 address exhaustion. IPv4 addressed may be
 represented in any notation expressing a 32-bit interger value. They are mostly
 written in dot-decimal notation, which consists of four octets of the addressed
 expressed individually in decimal numbers and separated by periods. For example,
 the quad-dotted IP address 192.0.2.235 represents the 32-bit decimal number
 3221226219, which in hexadecimal format is 0xC00002EB. 
 
 IPv6 addresses are represented as eight groups, separated by colons, of four 
 hexadecimal digits.  The full representation may be simplified by several 
 methods of notation; for example, 2001:0db8:0000:0000:0000:8a2e:0370:7334 
 becomes 2001:db8::8a2e:370:7334.  
 
The main advantage of IPv6 over IPv4 is its larger address space. The length
 of an IPv6 address is 128 bits, compared with 32 bits in IPv4. The address
 space therefore has 3.4*10<sup>38</sup> addresses (approximately 340 undecillion).


#### Configuring IP Addresses

Using the NetworkManager command line interface, users can manually set and test
 both IPv4 and IPv6 connections.  Run **nmcli con show** to view the names of 
 your network devices. We need to make sure NetworkManager manages the network 
 card we are using. Open up and edit the network script for your network device, 
 the name will be based on what **ifconfig** returns. In my example, my device 
 name is *eth1* and the script is located at **/etc/sysconfig/network-scripts/ifcfg-eth1**. 
 Change the line `NM_CONTROLLED=no` to `NM_CONTROLLED=yes`. If the line is not 
 found, add it.  Now you can start (or restart if it was already running) the 
 NetworkManager service.

```
# ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 9001
        inet 10.0.0.131  netmask 255.255.255.0  broadcast 10.0.0.255
        inet6 fe80::4:90ff:fe8f:4de1  prefixlen 64  scopeid 0x20<link>
        ether 02:04:90:8f:4d:e1  txqueuelen 1000  (Ethernet)
        RX packets 55538  bytes 81688165 (77.9 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3319  bytes 388114 (379.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        ether 02:5f:59:dd:5d:99  txqueuelen 1000  (Ethernet)
        RX packets 22  bytes 1342 (1.3 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 96  bytes 8192 (8.0 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 96  bytes 8192 (8.0 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# vim /etc/sysconfig/network-scripts/ifcfg-eth1
# systemctl start NetworkManager
```

We need a new connection to work with a device, you can use the 
 **nmcli con add** command. Run **nmcli con show** to see the created connection. 
  Afterwards, we can configure it with the IP addresses.

```
# nmcli con add con-name eth1 type ethernet ifname eth1
Connection ‘eth1’ (************************************) successfully added.
# nmcli con show
NAME    UUID                                  TYPE      DEVICE
eth1    ************************************  ethernet  eth1
```

Configure the IPv4 address:

```
# nmcli con mod eth1 ipv4.addresses 192.168.10.100/24
# nmcli con mod eth1 ipv4.method manual
```

Configure the IPv6 address:

```
# nmcli con mod eth1 ipv6.addresses fddb:fe2a:ab1e::c0a8:64/64
# nmcli con mod eth1 ipv6.method manual
```

```
# nmcli con show eth1 | grep "ipv[4|6]\.addresses"
ipv4.addresses:                         192.168.10.100/24
ipv6.addresses:                         fddb:fe2a:ab1e::c0a8:64/64
```

To ensure that the connection is configured properly, we bring up the connection
 and use the **ping** command:

```
# nmcli con up eth1
# ping -I eth1 192.168.10.100
# ping6 -I eth1 fddb:fe2a:ab1e::c0a8:64
```

### Route IP Traffic by Creating Static Routes

### Use Network Teaming or Bonding to Configure Aggregated Network Links

### Configure a System to Authenticate Using Kerberos

### Configure an iSCSI Target and Initiator

### Firewall Configuration

### Kernel Runtime Parameters

### Network Configuration
