Vagrant.configure("2") do |config|

  num_nodes = (ENV['NUM_NODES'] || 2).to_i

  config.vm.provider "libvirt" do |libvirt, override|
    libvirt.cpus = 2
    libvirt.memory = 4096
    libvirt.driver = 'kvm'
    override.vm.box = "centos/7"
  end

  config.vm.define "master" do |master|
    master.vm.hostname = "master"
    master.hostmanager.aliases = "osh311"
  end

  config.vm.define "infra" do |infra|
    infra.vm.hostname = "infra"
    infra.hostmanager.aliases = "backend-service.temperature.openshift.example.com"
  end

  num_nodes.times do |n|
    node_index = n+1
    node_name = "node-#{node_index}"
    config.vm.define "#{node_name}" do |node|
      node.vm.hostname = "#{node_name}"
    end
  end

end
