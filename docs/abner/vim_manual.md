**Author：Abner Kang**

**Email：abner.kang.dev@gmail.com**

**声明：**本手册只是为了帮助大家快速上手，并非学习指南，需要进一步学习的可以参考[《vim实用技巧》](https://pragprog.com/book/dnvim2/practical-vim-second-edition)

###一、为什么是VIM？
首先，我只是新手，不太懂vimrc的语法，只懂得一些简单的配置，为了方便大家上手我有意避开vimrc的设置，选择了[spf13-vim](http://vim.spf13.com/)这个vim的一个发行版帮助大家快速上手，关于VIM的命令只介绍常用的，目的仅仅是帮助大家快速上手。
最后，说下我为什么放弃IDE，在学校的时候，我没有用过IDE之外的编辑器，甚至离开了IDE就不会写代码了，工作后我最初选择的IDE是PyCharm，写的第一个不到1000行的代码在部署的时候就出问题了，原因是tab缩进的问题，花了很多不必要时间来解决这个问题，所以我后来选择了VIM。

**最后：大型软件的组织开发，我还是推荐使用IDE,至今没有见过JAVA程序员使用VIM的。如果不是实在没有很好的选择，请使用IDE。**

###二、VIM的安装
安装需要讲的只有一句话，注意spf13使用的vim版本，如果你的版本不够，请自己更新把系统的vim命令link到你最新的版本，否则lua脚本会报一大堆的错误。

```
➤  brew install vim --override-system-vi --with-lua --HEAD
➤  git clone https://github.com/spf13/spf13-vim.git 
➤  cd spf13-vim
➤  sh bootstrap.sh   #安装spf13-vim
```

###三、VIM的模式
任何一个编辑器，我们用的最多的功能，无非就是**复制、粘贴、删除，查找，替换**，除了这四个核心功能剩下的就是编辑，对于编辑我们只需要掌握快速找到或者定位我们需要编辑的内容就OK，本质还是**查找**，最后附加的功能就是**撤销、重复**。

####1.Normal Mode
####2.Command Mode
####3.Visual Mode
####4.Insert mode

###四、SPF13的插件介绍
首先关于spf13-vim的配置文件，我只讲其中一段。

```
    " The default leader is '\', but many people prefer ',' as it's in a standard
    " location. To override this behavior and set it back to '\' (or any other
    " character) add the following to your .vimrc.before.local file:
    "   let g:spf13_leader='\'
    if !exists('g:spf13_leader')
        let mapleader = ',' #手册中所有的<leader>在这个配置中就是',' 当然你也可以重新映射，所以我复制了那三行注释。
    else
        let mapleader=g:spf13_leader
    endif

```
这段代码的意思是下文所有的leader都映射为键盘上的','。

####1.NERDTree
vim中我需要的第一个插件是类似于目录树的东西，可以帮助我迅速在相关目录中查找需要的文件，NERDTree就是这个插件。

开启的快捷键：leader + e 或者 ctrl + e

开启后的效果如下图：

![NERDTree](http://upload-images.jianshu.io/upload_images/1234226-733d69601584ba3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

开启了这个插件后就可以使用第三部分中介绍的各种技巧随意操作了。

####2.ctrlp：快速查找需要编辑的文件
其实这个插件是fuzzy find的升级版
开启快捷键：<c-p>   (Ctrl+p)

![Ctrlp](http://upload-images.jianshu.io/upload_images/1234226-60a84f26b37cf82e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

开启这个插件后，在下方就会显示一个当前目录下的文件列表，在最下面一行可以使用文件名或者正则模糊查询需要编辑的文件。

####3.NERDCommenter：快速给代码添加注释
这个插件主要用于快速给代码添加注释或者清除代码的注释，建议在Visual模式下先选中代码，然后进行添加或者清除注释的操作。


开启快捷键：leader + cc


####3.Tagbar：快速定位需要查看的类或者方法
还记得eclipse中按下ctrl就可以跳转到类的定义或者实现的地方的功能吧，这个插件干的就是这么件事。

其次这个插件还继承了ctags可以提供函数的快速预览

开启ctags快捷键：leader + tt

![Ctags](http://upload-images.jianshu.io/upload_images/1234226-0342e2a712a33dcc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这样就可以快速浏览文件中定义的各个函数和类了。

实际开发中，除了这个概览，还需要能够快速定位到指定类或者方法的定义的位置，就需要配合ctags了。

具体操作如下：

1. 将光标移动到你需要查看的类名上，然后Ctrl+]
2. 查看完了后可以使用Ctrl+T返回

**注意：要使用这个功能，你必须使用ctags生成你使用语言的tags，否则会提示找不到源代码，关于ctags的使用我不详细展开了。**

以Python为例：

```
─Abner@Abners-MacBook-Pro.local ~/homework/flask  ‹master*›
╰─➤  find ./ -type f  |egrep "\.py$" > source.list #找到当前目录下所有以.py结尾的python文件
─Abner@Abners-MacBook-Pro.local ~/homework/flask  ‹master*›
╰─➤  ctags -R --language-force=python  -L source.list -o tags #根据这些Python文件生成ctags文件

```
下面就可以快乐的使用查找对象定义等功能了

