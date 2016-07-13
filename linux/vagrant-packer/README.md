# vagrant-packer play

## create vagrant boxes for virtualbox from scratch
(this example uses ubuntu14.04 iso)

### install software
- get vagrant, virtualbox
- brew install packer

### build vagrant box for virtualbox

1. packer build ubuntu1404.json (~15min)
2. vagrant box add ubuntu1404 build/ubuntu-14.04-amd64.box
3. create Vagrantfile (vagrant init) & open it
4. set: config.vm.box = "ubuntu1404"
5. vagrant up

### build with jenkins
1. wget [http://mirrors.jenkins-ci.org/war/latest/jenkins.war](http://mirrors.jenkins-ci.org/war/latest/jenkins.war)
2. java -jar jenkins.war
3. browse [http://localhost:8080](http://localhost:8080)
4. click "New Item"
5. Name: "vagrant image"
6. click "Freestyle project"
7. click OK
8. add Build Step, Execute Shell
9. add your packer build command, like you did on terminal before
9. save Project
10. click "Build Now"
11. go to "Dashboard"
12. click on your Build
13. find the Button "Console Output"
14. watch
15. more steps like exporting the box file to a http server

### more infos about build process
- ubuntu1404.json maintains build process 
 - iso image location
 - boot parameters
 - includes preseed.cfg
 - calls shell scripts after basic linux installation
 - set "headless" value to "false" to watch the installation
 - if you build with jenkins/script, headless should be "false"
- http/preseed.cfg inserts install instructions for debian installer
 - timezone
 - user login
 - partition setup
 - until installation is complete
- scripts/vagrant.sh
 - add ssh key
 - add vagrant user to sudoers
- scripts/vboxguest.sh
 - install virtualbox guest addons
- scripts/packages.sh
 - install dep packages you need
- scripts/compact.sh
 - makes vagrant image smaller (always last step)

## plugins for vagrant (optional)
- sync virtual guest addons with virutualbox
 - vagrant plugin install vagrant-vbguest (installs global)

## links
- [http://kappataumu.com/articles/creating-an-Ubuntu-VM-with-packer.html](http://kappataumu.com/articles/creating-an-Ubuntu-VM-with-packer.html)
- [https://help.ubuntu.com/community/InstallCDCustomization](https://help.ubuntu.com/community/InstallCDCustomization)
- [https://github.com/ChiperSoft/Packer-Vagrant-Example](https://github.com/ChiperSoft/Packer-Vagrant-Example)