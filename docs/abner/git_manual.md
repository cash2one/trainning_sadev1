###一、git概述
区别于svn，git是个分布式的代码版本控制系统。
在进行所有的操作之前，都需要设置一下个人信息，以区分不同提交者的身份

```
$ git config -global user.name "your name"
$ git config -global user.email "yourname@example.com"
```

###二、理解代码的位置

![图1 git 工作空间示意图](http://upload-images.jianshu.io/upload_images/1234226-fbbbe20e0ebe3fb1.jpeg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通常情况下，在分布式版本控制中，代码存放在三个重要的位置：远程仓库（Remote）、本地仓库（Repository）和当前工作空间（workkkspace）。

**通常的一次代码修改包含以下步骤：**

1. 通过fetch/clone将代码从远程仓库（Remote）下载到本地（Repository）
2. 通过checkout从本地仓库中找出需要修改的代码开始修改
3. git维护的index数据结构维护代码的变化状态
4. 通过add命令让index知道修改的内容
5. 通过commit命令将修改提交到本地仓库
6. 通过push命令将修改提交到远程仓库

#### 2.1 git clone：从远程仓库下载代码
clone ：将远程仓库下载到本地，指定目录名则使用指定的目录名，不指定则和远程仓库保持一致

```
$ git clone <版本库的网址> <本地目录名>
$ git clone https://github.com/jquery/jquery.git  #下载JQuery源码
```
#### 2.2 git remote：管理远程主机名
remote：通常情况下远程主机使用URL表示，不利于开发者记忆，可以使用remote命令给远程主机命名
下载代码库后，如果没有指定远程主机的名字，则默认为：**origin**

```
$ git remote  #列出这个仓库相关的所有远程主机名
origin

$ git clone -o jQuery https://github.com/jquery/jquery.git #使用-o选项指定这个代码库的远程主机名
$ git remote
jQuery

$ git remote -v #查看远程主机的地址
origin  git@github.com:jquery/jquery.git (fetch)
origin  git@github.com:jquery/jquery.git (push)

$ git  remote show <主机名> #查看远程主机的详细信息
$ git remote add <主机名> <网址> #添加远程主机
$ git remote rm <主机名> #删除远程主机
$ git remote rename <原主机名><新主机名>

```

####2.3 git fetch：同步本地代码库为最新状态
fetch：已经有clone可以拉取远程仓库的代码了，**为什么还需要fetch命令？**
原创解答：如果远程仓库只有你一个人使用的话，你使用clone和fetch都是等效的，但是版本控制就是为群体协作而生的，只有一种情况下，你需要使用fetch命令。如下描述：
当你和你的队友都clone了远程仓库的代码，你的队友修改完了并且push到了远程仓库，这个时候你的本地Repository和remote处于不同步的状态，你如果使用push提交代码，会提示错误，这个时候你就需要使用fetch同步你本地的Repository和remote然后再提交。

```
$ git fetch <远程主机名><分支名称> #默认情况下，帮你取回的是master分支，如果你要取回其他分支，请指定。
注：比较clone命令，fetch命令不再提供<本地目录名 >的选项，因为使用这个命令的时候一般本地目录都已经存在，仅仅是做了Repository和Remote的同步操作
 $ git fetch origin master #取回origin主机的master分支
```

通常情况下，取回了远程分支后，要读取操作远程分支就需要使用 <远程主机名/分支名>的格式

```
$ git branch -r #查看远程分支
origin/master

$ git branch -a #查看所有分支
* master
  remotes/origin/master

$ git checkout -b newBrach origin/master #在远程分支的基础上创建新分支

$ git merge origin/master #合并远程分支
``` 

####2.4  git push：同步本地Repository到Remote
push：本地分支所有的修改都已经提交到local Repository后，需要将更新同步到Remote Repository。
只有你进行了push操作后，你的队友从远程仓库下载代码才可以看到那你的更新。**所以本地修改更新完一定不能忘记push操作**

注：git push 基于分支进行操作，默认不推送tag，除非使用 --tags指定


```
$ git push <远程主机名> <本地分支名>:<远程分支名> #推送操作是用本地同步远程，所以后面的参数一定是<本地分支名：远程分支名>
注：如果省略远程分支名 ，通常表示你的本地分支名和远程分支名是一致的，如果不一致，比如你在本地修改了分支名，则在推送时一定要指定远程分支名，否则将会在远程创建新的分支

# git push origin master#表示将本地的master分支更新到远程主机 

通常情况下，我们要删除一个远程的分支是这样操作。
# git push origin --delete master
利用push的特性，我们使用一个空的分支去更新远程的特定分支，也可以达到删除的目的
# git push origin :master

如果我们本地的分支和远程的分支使用的命名是完全一致的，我们可以这样操作：
# git push  origin
如果本地只有一个分支，操作更加简单
# git push 

如果你的这个仓库关联了多个远程主机（使用git remote 可以查看），你还想不加任何参数使用git push怎么办？
解决方法：指定默认的远程主机
$ git push -u origin master #执行了这个操作后就不需要使用任何参数来使用git push了

最后一个问题：不使用任何参数的git push默认只推送当前分支，即simple模式，还有一种matching模式，会推送所有远程分支对应的本地分支。你可以通过修改配置文件的方式来选择自己需要的模式。
$ git config --global push.default.matching
或者
$ git config --global push.default.simple

那么在simple模式下能不能强制推送呢？也是可以的
$ git push --force origin #将本地所有的分支都推送到远程主机，如果该分支在远程主机不存在，就创建分支



```

####2.5 git pull ：获取远程分支同本地分支合并
实际中只有一种情况用到这个命令，当你和你的队友同时在本地操作同一个分支，他比你先提交，也就意味着此刻你的本地库比远程库要旧，这个时候你如果要push就会被拒绝，可以使用pull把这个分支最新代码拉下来。
从图示中就很容易看出来，这个命令直接从远程拿个分支到本地的工作空间和你正在进行操作的分支进行合并。

```
$ git pull <远程主机名><远程分支名>:<本地分支名> #注意比较这个命令和push的格式的区别
$ git pull origin next:master

$ git pull origin next #获取远程的next分支和当前工作空间中正在操作的分支合并
等价于：
$ git fetch origin
$ git merge origin/next
虽然也可以简单的使用git pull，但是并不建议这么做，需要的自己查手册吧
```

###三、理解代码的状态

![图2 git代码状态示意图](http://upload-images.jianshu.io/upload_images/1234226-1fe0b62d4aca96cf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

既然是版本控制，肯定要维护代码不同版本的状态，git是通过定义了四个不同的存储区域来维护代码状态的。
如图所示，自左向右存在4个不同区域，对应了代码的四个不同的新旧程度。

1. workspace：用户直接面对的空间就是workspace，这个空间和你操作任何普通目录时没有区别的，也不具备跟踪文件修改状态的功能，用户直接在这个空间修改代码，所以这个空间的代码状态最新。
2. index：普通目录不具备跟踪版本功能，index本质是个数据结构，维护指向不同的文件版本的索引，只有在该空间建立索引，才能跟踪文件的状态。
3. local Repository：本地仓库存储一次更新的完整版本。
4. remote Repository：远程仓库存储所有的软件版本。通常代码状态最旧。

**代码版本更新的过程为：workspace-> index -> local repository -> remote repository**
#### 3.1 workspace -> index ：为指定文件建立版本跟踪信息
workspace中的文件不具有任何版本信息，和普通目录一样，但是可以通过创建索引的形式在index中创建文件的版本信息。

文件修改后，我们通常想知道这次修改的具体内容，可以通过和历史版本的对比得到。

```
$ git diff <文件名> #列出工作空间中的指定文件和index中维护的文件不同，如果不指定，则会列出工作空间内所有被跟踪的文件同index中维护的版本的差异 
注意：不要在提交之后只用该命令，提交后workspace和index的状态已经同步了，这个命令是没有输出的
```

修改完成后，我们需要将修改，同步到index

```
$ git add <文件名> #为指定文件创建版本信息
```

#### 3.2 index -> local repository ：提交稳定的版本到本地仓库
通过将index中最新的版本提交的本地仓库实现一次完整版本的跟踪。
注：index跟踪每一次修改，local Repository跟踪每一个版本，仅仅是版本控制的粒度的大小不同

提交版本之前，可以通过和历史版本的对比查看更新的内容

```
$ git diff -cached
注意：不要在提交后使用这个命令，提交后index和local Repository的版本已经同步了，这个操作没有输出。
```

提交修改，更新本地代码库。

```
$ git commit <文件名>
```

#### 3.3 workspace -> local repository
**注意：只有一种情况可以这么操作，就是该文件已经使用git add在index中建立版本记录的时候可以实现这个状态的转移**

```
$ git diff HEAD  #查看工作空间中的代码和本地代码库的旧版本的相比更新的地方
```

直接从本地工作空间提交代码到本地代码库

```
$ git commit -a <文件名>
```

###四、理解分支
很多情况下，我们需要做一些类似与实验性的特性的开发，这个时候直接在主分支上进行操作不是很合适，我们可以基于主分支创建一个新的分支进行开发，如果开发通过了测试就可以合并到主分支；如果这个实验性分支不合适，就可以直接删除。以此降低开发对主分支的影响。

![图3. 一张图看懂分支.PNG](http://upload-images.jianshu.io/upload_images/1234226-13285a186ce8be71.PNG?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如上图所示，一般项目都会维护至少两条分支，master和dev，master可以理解为我们通常下载软件时使用的release版本，主要用于稳定版本的发布，一般的开发工作不在master上操作。

**开发流程：**
正常的开发流程是这个样的，每个开发者基于dev分支创建新的分支，开发完了以后将分支合并到dev分支，dev分支上的功能通常就是可以测试的了，dev分支打上完整的发布标签后测试团队就可以介入对这个版本进行测试，测试通过后就可以合并到master作为稳定版本进行发布。

**多人协作**：

1. 首先，可以试图使用 git push origin branch-name 推送自己的修改
2. 如果推送失败，则因为远程分支比你的本地代码要新，需要先用git pull 试图合并
3. 如果合并有冲突，则解决冲突，并在本地提交
4. 没有冲突或者解决了冲突后，再用 git push origin branch-name 推送
注：如果git pull 提示 “No tracking infomation”，则说明本地分支和远程分支的链接关系没有创建，用命令 git branch --set-upstream branch-name origin/branch-name

   

####4.1 分支操作：git branch

####4.2 分支间切换：git checkout

###五、总结   
回答好下面三个问题就可以基本掌握git了，下面的问题自己去了解吧。
####问题一：版本在哪里？（commit 和 tag的区别）####
tag只是commit的一个特殊的状态，可以认为是里程碑。
####问题二：什么是版本控制（HEAD是什么）？####
HEAD是指向你当前操作版本的分支
####问题三：如何实现任意版本的切换（log和reflog）？####
log记录了你当前操作版本之前的每一次提交的日志，reflog其实是真正的日志，记录每次操作，这个日志和文件系统的日志基本是一样的。