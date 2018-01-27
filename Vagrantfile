# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "centos/7"
  config.vm.box_check_update = true
  config.vm.synced_folder ".", "/vagrant", disabled: false 
  config.vm.hostname = "goldengirl"

  # provision VBOX with some extra sauce
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.cpus = 2
    vb.memory = "2048"
  end

  # update and get epel-release
  config.vm.provision "shell", inline: <<-SHELL
    yum update -y
    yum install epel-release -y
  SHELL
  
  # cleanup default stuff -- we'll add it be back 
  # when we need it
  config.vm.provision "shell", inline: <<-SHELL
    systemctl stop postfix
    systemctl disable postfix
    yum remove postfix -y
    systemctl stop chronyd
    systemctl disable chronyd 
    yum remove chrony -y
  SHELL
  
  # docker installation
  config.vm.provision "shell", inline: <<-SHELL
    yum install -y yum-utils device-mapper-persistent-data lvm2
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum-config-manager --disable docker-ce-edge
    yum install docker-ce -y
    systemctl enable docker
    systemctl start docker
    curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
  SHELL

  # adaptive system tuning daemon
  config.vm.provision "shell", inline: <<-SHELL
    yum install tuned -y
    service tuned start
    chkconfig tuned on
  SHELL
 
  # Basic admin / monitoring tools 
  config.vm.provision "shell", inline: <<-SHELL
    yum install git -y
    yum install vim -y
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
    yum install bind-utils -y
    yum install mlocate -y; updatedb
  SHELL
  
  # Basic security tools
  config.vm.provision "shell", inline: <<-SHELL
    yum install rkhunter -y
    yum install lynis -y 
    yum install audit audit-libs -y
    yum install fail2ban -y
  SHELL
  
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
  
  # golang
  config.vm.provision "shell", inline: <<-SHELL
    wget https://dl.google.com/go/go1.9.3.linux-amd64.tar.gz
    tar -C /usr/local -xzf go1.9.3.linux-amd64.tar.gz
    export PATH=$PATH:/usr/local/go/bin
    export GOPATH=$HOME/golang-projects
    export GOROOT=/usr/local/go
    export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
    echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
    echo "export PATH=$PATH:/usr/local/go/bin" >> /home/vagrant/.bashrc
    echo "export GOPATH=$HOME/golang-projects" >> ~/.bashrc
    echo "export GOPATH=$HOME/golang-projects" >> /home/vagrant/.bashrc
    echo "export GOROOT=/usr/local/go" >> ~/.bashrc
    echo "export GOROOT=/usr/local/go" >> /home/vagrant/.bashrc
    echo "export PATH=$GOPATH/bin:$GOROOT/bin:$PATH" >> ~/.bashrc
    echo "export PATH=$GOPATH/bin:$GOROOT/bin:$PATH" >> /home/vagrant/.bashrc
    sed -i -e 's/root/vagrant/g' /home/vagrant/.bashrc
    git clone https://github.com/fatih/vim-go.git ~/.vim/pack/plugins/start/vim-go
    curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
    echo "call plug#begin()" >> ~/.vimrc
    echo "	Plug 'fatih/vim-go'" >> ~/.vimrc
    echo "call plug#end()" >> ~/.vimrc
    echo "let g:go_version_warning = 0" >> ~/.vimrc
    echo "syntax on" >> ~/.vimrc
    echo "set ruler" >> ~/.vimrc
    echo "set nu" >> ~/.vimrc
    echo "set noswapfile" >> ~/.vimrc
    echo "filetype on" >> ~/.vimrc
    echo "filetype indent on" >> ~/.vimrc
    go env
    go version
  SHELL

  # Add dockerfiles
  config.vm.provision "file", source: "dockerfiles", destination: "$HOME/dockerfiles"
end
