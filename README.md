# pysh
a project to place your python and shell scripts

## basic config for vim
    vim ~/.vimrc:
    set ts=4
    set expandtab
    
## basic config for git
    git clone https://github.com/qwyang/pysh.git
    git config remote.origin.url git@github.com:qwyang/pysh.git
    git config --global user.email "yangqunwei@huawei.com"
    git config --global user.name "qunwei"
    git config --global core.editor vim
    git config --global push.default simple

## useful help for git
    git config -l --global
    git ls-files
    git ls-files -d
    git ls-files -d | xargs git checkout
    git config core.eol crlf
    git config core.autocrlf true
    git archive --format tar.gz -o abc.tar.gz HEAD

## other information
    IDE for shell and py: pycharm
    Online Editor for markdown: http://mahua.jser.me/
    markdown introduction: http://blog.csdn.net/skykingf/article/details/45536231
