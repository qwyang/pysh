# pysh
a project to place your python and shell scripts

== [[configuration for git]] ==

=== basic config ===
  git clone https://github.com/qwyang/pysh.git
  git config --global user.email "yangqunwei@huawei.com"
  git config --global user.name "qunwei"
  git config --global core.editor vim

=== usefull help ===
  git config -l --global
  git ls-files
  git ls-files -d
  git ls-files -d | xargs git checkout
