# -*- mode: ruby -*-
# vi: set ft=ruby :
Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-jessie64"

  # Ansible provisioner.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision_vagrant.yml"
  end

end
