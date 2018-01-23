# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.box_check_update = true
  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.hostname = "goldengirl"

  # config.vm.network "forwarded_port", guest: 80, host: 8080
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.cpus = 2
    vb.memory = "2048"
  end

  # update, get release
  config.vm.provision "shell", inline: <<-SHELL
    yum update -y
    yum install epel-release -y
  SHELL
  
  # cleanup time
  config.vm.provision "shell", inline: <<-SHELL
    systemctl stop postfix
    systemctl disable postfix
    yum remove postfix -y
    systemctl stop chronyd
    systemctl disable chronyd 
    yum remove chrony -y
  SHELL

  # adaptive system tuning daemon
  config.vm.provision "shell", inline: <<-SHELL
    yum install tuned -y
    service tuned start
    chkconfig tuned on
  SHELL
 
  # Network hardening
  # need to edit /etc/sysctl.conf so the settings are persistent
  config.vm.provision "shell", inline: <<-SHELL
    # Avoid a smurf attack
    sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1
    # Turn on protection for bad icmp error messages
    sysctl -w net.ipv4.icmp_ignore_bogus_error_responses=1
    # Turn on syncookies for SYN flood attack protection
    sysctl -w net.ipv4.tcp_syncookies=1
    # Turn on and log spoofed, source routed, and redirect packets
    sysctl -w net.ipv4.conf.all.log_martians=1
    sysctl -w net.ipv4.conf.default.log_martians=1
    # No source routed packets here
    sysctl -w net.ipv4.conf.all.accept_source_route=0
    sysctl -w net.ipv4.conf.default.accept_source_route=0
    # Turn on reverse path filtering
    sysctl -w net.ipv4.conf.all.rp_filter=1
    sysctl -w net.ipv4.conf.default.rp_filter=1
    # Make sure no one can alter the routing tables
    sysctl -w net.ipv4.conf.all.accept_redirects=0
    sysctl -w net.ipv4.conf.default.accept_redirects=0
    sysctl -w net.ipv4.conf.all.secure_redirects=0
    sysctl -w net.ipv4.conf.default.secure_redirects=0
    # Don't act as a router
    sysctl -w net.ipv4.ip_forward=0
    sysctl -w net.ipv4.conf.all.send_redirects=0
    sysctl -w net.ipv4.conf.default.send_redirects=0
    # Turn on execshield for reducing worm or other automated remote attacks 
    sysctl -w kernel.exec-shield=1
    sysctl -w kernel.randomize_va_space=1  
    # Disable IPV6
    sysctl -w net.ipv6.conf.default.disable_ipv6=1
    sysctl -w net.ipv6.conf.all.disable_ipv6=1
    # Increase system file descriptor limit    
    sysctl -w fs.file-max=65535
    # Allow for more PIDs (Prevention of fork() failure error message) 
    sysctl -w kernel.pid_max=65536
    # Tuning Linux network stack to increase TCP buffer size. 
    # Set the max OS send buffer size (wmem) and receive buffer size (rmem) to 12 MB for queues on all protocols.
    sysctl -w net.core.rmem_max=8388608
    sysctl -w net.core.wmem_max=8388608
    # Value to set for queue on the INPUT side when incoming packets are faster then the kernel process on them. 
    sysctl -w net.core.netdev_max_backlog=5000
    # For increasing transfer window, enable window scaling
    sysctl -w net.ipv4.tcp_window_scaling=1
    # Disconnect dead TCP connections after 1 minute
    sysctl -w net.ipv4.tcp_keepalive_time=60
    # Wait a maximum of 5 * 2 = 10 seconds in the TIME_WAIT state after a FIN, to handle
    # any remaining packets in the network.
    sysctl -w net.netfilter.nf_conntrack_tcp_timeout_time_wait=10
    # How long to keep ESTABLISHED connections in conntrack table
    # Should be higher than tcp_keepalive_time + tcp_keepalive_probes * tcp_keepalive_intvl )
    sysctl -w net.netfilter.nf_conntrack_tcp_timeout_established=300
    sysctl -w net.netfilter.nf_conntrack_generic_timeout=300 
    # Allow a high number of timewait sockets
    sysctl -w net.ipv4.tcp_max_tw_buckets=2000000
    # Timeout broken connections faster (amount of time to wait for FIN)
    sysctl -w net.ipv4.tcp_fin_timeout=10
    # Let the networking stack reuse TIME_WAIT connections when it thinks it's safe to do so
    sysctl -w net.ipv4.tcp_tw_reuse=1
    # Determines the wait time between isAlive interval probes (reduce from 75 sec to 15)
    sysctl -w net.ipv4.tcp_keepalive_intvl=15
    # Determines the number of probes before timing out (reduce from 9 sec to 5 sec)
    sysctl -w net.ipv4.tcp_keepalive_probes=5
  SHELL
  
  # Basic admin / monitoring tools 
  config.vm.provision "shell", inline: <<-SHELL
    yum install htop -y
    yum install ncdu -y
    yum install powertop -y
    yum install dnstop -y
    yum install iftop -y
    yum install jnettop -y
    yum install atop -y
    yum install apachetop -y
    yum install mytop -y
    yum install iotop -y
    yum install sysstat -y
    yum install saidar -y
    yum install procps-ng -y
    yum install nmon -y
    yum install bmon -y
    yum install iptraf-ng -y
    yum install tcpdump -y
    yum install quota -y
    yum install vnstat -y
    yum install nload -y
    yum install arpwatch -y
    yum install dropwatch -y
    yum install util-linux -y
    yum install net-tools -y
    yum install aide -y
    yum install wget -y
    yum install mlocate -y; updatedb
  SHELL
  
  # Basic security tools
  config.vm.provision "shell", inline: <<-SHELL
    yum install rkhunter -y
    yum install lynis -y 
    yum install audit audit-libs -y
    yum install fail2ban -y
  SHELL
  
  # FTP Server
  # config.vm.provision "shell", inline: <<-SHELL
  #   yum install proftpd proftpd-utils
  #   # systemctl start proftpd
  #   # systemctl restart proftpd 
  #   systemctl enable proftpd
  # SHELL
  
  # SSL Support
  # https://wiki.centos.org/HowTos/Https
  # config.vm.provision "shell", inline: <<-SHELL
  #   yum install mod_ssl openssl -y 
  # SHELL

  # Lock down cron
  config.vm.provision "shell", inline: <<-SHELL
    touch /etc/cron.allow
    chmod 600 /etc/cron.allow
    awk -F: '{print $1}' /etc/passwd | grep -v root > /etc/cron.deny
  SHELL
 
  # Restricting Root
  config.vm.provision "shell", inline: <<-SHELL
    echo "tty1" > /etc/securetty
    chmod 700 /root
  SHELL
end
