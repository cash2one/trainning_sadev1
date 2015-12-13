[TOC]
##Stage1开发总结：
**注：实现参考开源项目：[Open-Falcon](http://book.open-falcon.com/zh/intro/index.html )**

###一、需求收集
**任务：**设计实现一个主机监控的数据采集程序agent。

* 数据采集：主要采集平均负载、CPU使用率和内存使用
* 运行方式：在后台以一定周期进行数据采集

###二、技术调研
* 数据采集方式：主要调研了每种监控指标的意义和采集的方式，见详细描述文档[**linux监控指标采集**](https://github.com/sadev1/trainning_sadev1/blob/stage1/docs/linux监控信息采集.md)。（康景龙完成）
* 程序运行控制：监控程序一般作为后台程序运行，主要调研了supervisor。（通过让agent成为supervisor的子进程来清除agent和shell进程的父子关系，避免终端的退出导致程序的退出）（陶浩完成）

###三、技术选型
* 数据采集方式：**psutil**，主要考虑到不管使用任何shell的外部工具都无法做到全平台兼容，另外还需要解决有些主机上没有安装这些外部工具的问题，所以最终选择了psutil第三方库来做数据采集，对于有些平台上采集不到的数据在程序实现上做了兼容。
* 程序运行控制：使用supervisor管理agent进程，agent进程内部使用标准库sched实现周期性采集。

###四、实现方案
实现方案主要参考了小米的开源监控平台[Open-Falcon](http://book.open-falcon.com/zh/intro/index.html )**的实现。

**GitHub地址：**<https://github.com/open-falcon/agent>

####4.1.代码组织
	.
	├── agent.py
	├── deploy
	│   ├── run.sh
	│   └── supervisor.conf
	└── plugins
    	├── __init__.py
    	├── cpu.py
    	├── load.py
    	└── memory.py
    	
 为了后续方便添加其他监控指标，整体采用了插件式设计，添加新的插件时只需要按照插件内约定的monitor函数返回的数据格式实现相关插件，然后在__init__.py中配置相关插件，就可以实现监控数据的采集。
 
 **\_\_init\_\_.py:**
 
	# -*- coding: utf-8 -*-
	import cpu
	import memory
	import load
	'''
	在此处配置监控插件，请注意格式。
	配置前需要保证插件被导入到当前命名空间。
	'''

	monitor = {
    	'cpu': cpu.monitor,
    	'memory': memory.monitor,
    	'load': load.monitor,
	}
	
**cpu.py:**

![](/Users/Abner/Desktop/cpu.png)

* cpu_info：负责采集监控数据
* monitor：负责返回数据模型

**load.py:**

![](/Users/Abner/Desktop/load.png)


####4.2.数据模型：
强大的数据模型是后续开展前端展示和监控数据的查询的基础。本阶段我们对所有监控插件使用了统一的数据模型，如下所示：

	{
		'module_1':{
						metric-1:value,
						metric-2:value,
						...
					 }
		'module_2':{
						metric-1:value,
						metric-2:value,
						...
					}
		...
	}
		
**示例一：内存监控数据**
	
	$ python memory.py
	{'mem_swap_monitor': {'free': 1052508160L,
                      	  'percent': 2.0,
                      	  'sin': 8795193344L,
                      	  'sout': 277151744L,
                      	  'total': 1073741824L,
                      	  'used': 21233664L},
 	  'mem_vir_monitor': {'active': 3634704384L,
                     	  'available': 2884702208L,
                     	  'buffers': '',
                     	  'cached': '',
                     	  'free': 825602048L,
                     	  'inactive': 2059100160L,
                     	  'percent': 66.4,
                     	  'shared': '',
                     	  'total': 8589934592L,
                     	  'used': 7528722432L,
                     	  'wired': 1834917888L}
     }
     
     
 **下阶段服务端存储数据模型：**    
  

	{
    	metric: load.1min,          #监控指标
    	endpoint: open-falcon-host, #主机名或者IP地址
    	tags: idc=aws-sgp,group=az1,#选项，用户组、机房位置等，主要为了后续数据分片
    	value: 1.5,                 #监控值
    	timestamp: `date +%s`,      #时间戳
    	period：60s                 #数据采集周期
	}
	
###五、总结:
####5.1:工作分工
**康景龙：**

	1. 技术调研中监控指标的意义和采集方式（主要是基于shell外部工具和文件系统的采集方式）。
	2. 实现方案中数据模型的选定和插件式代码组织规范的制定。
	3. 编码中负责了第一版agent除了load以外的监控指标的采集。

**陶浩：**

	1.技术调研中监控指标的采集（主要是基于psutil的采集方式）
	2.技术调研中关于监控程序运行控制方式
	3.编码中负责实现了load监控指标的采集和agent主程序的重构以及supervisor对程序运行方式的控制。
	
####5.2：不足
	1.除了基本的三个监控指标，没有做其他监控指标的扩展。（后续应更详细调研常用的监控指标，重点了解各项监控指标的含义。）
	2.开发前期，没有邀请导师参与沟通。（许公子见谅）
	3.代码的分支管理目前没有做到开发和实现分离，应该在stage1分支上建立dev分支，每人分别基于dev建立自己的分支，测试完成后合并到dev分支，在stage1分支上线。
	4.没有写单独的测试模块（其实主要是实现功能比较简单，就直接在模块内简单测试了）
	
####5.3：说明
**关于延期：**
这个阶段康景龙同学正在毕业答辩，没有及时跟导师和陶浩同学沟通，导致延误了进度。

**关于分工：**
由于康景龙同学Python基础较弱，stage1的编码量不算很大，就由康景龙同学负责写原型，陶浩同学负责指导review，这个在提交日志中有详细体现。







