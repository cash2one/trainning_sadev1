##Linux常用监控指标
Author: Abner Kang

Email:abner.kang.dev@gmail.com
###1.内存
####1.1 监控信息的获取：free

	[root@master ~]# free
                total       used       free     shared    buffers     cached
	Mem:       8060468    4284216    3776252          0     342632    2187636
	-/+ buffers/cache:    1753948    6306520
	Swap:      8191992          0    8191992
	
**第一行是从系统的角度看内存的使用情况：（清晰起见，使用sys前缀）**
****
* sys.total：物理内存的总量
* sys.used：已经使用的内存的总量
* sys.free: 空闲的内存的总量

**从系统的角度看：sys.total  =  sys.used  + sys.free**
****
* sys.buffers:系统向磁盘写文件时先写进内存的缓冲就是这个区域
* sys.cached:系统读文件时，会预先读取一块供后续使用，就读进了这个区域
* 
**注：对系统而言，这两个区域不是必须的，仅仅为了加快IO的速度存在，因为磁盘是块设备，读取和写入都是按照块大小进行操作，这两个区域的存在有助于减少实际的IO次数**

**注：这两个区域解释了为什么打开一个大文件第二次读取的速度比第一次快很多。下面代码给出测试的方法**

	# echo 3 > /proc/sys/vm/drop_caches 强制释放掉所有的sys.cached
	1.读一个大文件，并记录时间
	2.关闭文件
	3.重读这个大文件，并记录时间

****

**第二行是从程序的角度看系统中可以使用的内存和已经使用的内存的情况：**
****
* user.used:程序看来已经使用的内存的总量
* user.free:程序看来系统中可以使用的内存的总量

**综合第一行和第二行得到：**

* user.used = sys.used - sys.buffers - sys.cached
* user.free = sys.free + sys.buffers + sys.cached
* sys.total = user.used + user.free

****
**第三行显示的是swap分区的使用情况：**
****

* swap.total:
* swap.used:
* swap.free:

****

####1.2 监控信息的获取：vmstat

	[root@master ~]# vmstat 1 3  #每秒统计1次，统计3次
	procs -----------memory----------    ---swap-— -----io---- --system-- -----cpu-----
 	r  b   swpd    free   buff   cache   si   so    bi    bo   in   cs    us sy  id wa st
 	0  0      0 3776068 342624 2186844    0    0     0     1    0    1     0  0 100  0  0
 	0  0      0 3776060 342624 2186844    0    0     0    40  322  420     0  1  99  0  0
 	0  0      0 3776060 342624 2186844    0    0     0     0  278  379     0  0  99  0  0
 	
**Procs（进程）**：

* r：运行队列中的进程数量
* b：等待IO的进程数量

**Memory（内存）**：

* swpd：使用的虚拟内存的大小
* free：可用的内存大小  从系统的角度看
* buff：用作缓冲的内存大小
* cache：用作缓存的内存大小  

**Swap：**

* si：每秒从交换分区写入内存的大小。  交换分区-->内存
* so：每秒写入交换区的内存大小。      内存-->交换分区

**IO：**

* bi：每秒读取的块数
* bo：每秒写入的块数

**System：**

* in：每秒的中断数（包含时钟中断）（interrupt）
* cs：每秒的上下文切换数 （context switch）

**CPU：**

* us：user time
* sy：system time
* id：idle time
* wa：等待IO时间
 	
####1.3 监控信息的获取：sar
	[root@master ~]# sar -r 1 3
	Linux 2.6.32-431.el6.x86_64 (master) 2015年12月09日 _x86_64_(4 CPU)

	16时23分20秒 kbmemfree kbmemused  %memused kbbuffers  kbcached  kbcommit   %commit
	16时23分21秒   3775936   4284532     53.15    342624   2186968   3179748     19.56
	16时23分22秒   3775936   4284532     53.15    342624   2186968   3179748     19.56
	16时23分23秒   3775936   4284532     53.15    342624   2186968   3179748     19.56

**下面四项和free显示的第二行是一致的：**
	
* kbmemfree:
* kbmemused:
* kbbuffers:
* kbcached:

* %memused:物理内存使用的百分比
* kbcommit:为了确保不溢出而需要的内存（RAM + swap）
* %commit:kbcommit/(RAM+swap)

****
	
####1.5 监控信息的获取：/proc/meminfo
	[root@master ~]# cat /proc/meminfo
	[High-Level Statistics]
	MemTotal:        8060468 kB   Total usable ram(physical ram minus a few reserved bits and the kernel binary code)
	MemFree:         3774712 kB   LowFree + HighFree
	Buffers:          342612 kB   Memory in buffer cache. mostly useless as metric nowadays
	Cached:          2186632 kB   Memory in the pagecache (diskcache) minus SwapCache
	SwapCached:            0 kB   Memory that once was swapped out, is swapped back in but still also is in the swapfile (if memory is needed it doesn't need to be swapped out AGAIN because it is already in the swapfile. This saves I/O)
	
	Active:          2818596 kB   最近经常被使用的内存，除非必要不会被换出
	Inactive:        1078444 kB   最近不经常使用的内存，非常可能被用于其他途径
	Active(anon):    1367952 kB
	Inactive(anon):    12116 kB
	Active(file):    1450644 kB
	Inactive(file):  1066328 kB
	
	Unevictable:           0 kB
	Mlocked:               0 kB
	
	SwapTotal:       8191992 kB
	SwapFree:        8191992 kB
	
	Dirty:                88 kB    等待被写回到磁盘的内存的大小
	Writeback:             0 kB    正在被写回到词牌的内存的大小
	AnonPages:       1367788 kB
	Mapped:            93896 kB    映射文件的大小
	Shmem:             12280 kB 
	Slab:             213808 kB    内核数据结构缓存
	SReclaimable:     133352 kB
	SUnreclaim:        80456 kB
	KernelStack:        5560 kB
	PageTables:        88184 kB
	NFS_Unstable:          0 kB
	Bounce:                0 kB
	WritebackTmp:          0 kB
	
	CommitLimit:    12222224 kB
	Committed_AS:    3181212 kB
	
	VmallocTotal:   34359738367 kB
	VmallocUsed:       28884 kB
	VmallocChunk:   34359701728 kB
	
	HardwareCorrupted:     0 kB
	AnonHugePages:    860160 kB
	HugePages_Total:       0
	HugePages_Free:        0
	HugePages_Rsvd:        0
	HugePages_Surp:        0
	Hugepagesize:       2048 kB
	DirectMap4k:        8180 kB
	DirectMap2M:     8380416 kB

****

###2.负载：load
关于负载：如果你的主机有两个4核心的处理器，那么负载为8时，表示处理器已经没有可以分配的资源了，如果低于这个值，说明系统还有空闲的资源可以分配。
####2.1.监控信息的获取：uptime

	[root@master ~]# uptime
 	16:36:57 up 122 days, 23:51,  9 users,  load average: 0.00, 0.00, 0.00
####2.2.监控信息的获取：top
	[root@master ~]# top
	top - 16:38:33 up 122 days, 23:52,  9 users,  load average: 0.00, 0.00, 0.00
	
####2.3.监控信息的获取：w
	[root@master ~]# w
 	16:55:53 up 123 days, 10 min,  9 users,  load average: 0.00, 0.00, 0.00

####2.4.监控信息的获取：/proc/loadavg
	[root@master ~]# cat /proc/loadavg
	0.00 0.00 0.00 1/693 10582

####2.5.监控信息的获取：sar
	
	[root@master proc]# sar -q 5 3
	Linux 2.6.32-431.el6.x86_64 (master) 2015年12月09日 _x86_64_(4 CPU)
	         runq-sz  plist-sz   ldavg-1   ldavg-5  ldavg-15
	17:11:55       0       695      0.00      0.01      0.00
	17:12:00       0       695      0.00      0.01      0.00
	17:12:05       0       696      0.00      0.01      0.00
	17:12:10       0       695      0.00      0.01      0.00
	
* runq-sz：运行队列的长度（等待运行的进程数）
* plist-sz：进程列表中进程（process）和线程（threads）的数量
* ldavg-1:
* ldavg-10:
* ldavg-15:


	
###3.CPU
####2.1.监控信息的获取：sar
	root@master proc]# sar -u 3 3 3秒采样一次，一共采样3次
	Linux 2.6.32-431.el6.x86_64 (master) 2015年12月09日 _x86_64_(4 CPU)

             CPU     %user     %nice   %system   %iowait    %steal     %idle
    17:03:59 all      0.25      0.00      0.25      0.00      0.08     99.42
    17:04:02 all      0.25      0.00      0.25      0.00      0.08     99.42
    17:04:05 all      0.17      0.00      0.25      0.08      0.00     99.50
    17:04:08 all      0.22      0.00      0.25      0.03      0.06     99.44

* %user: user time percent
* %nice: user  with nice time percent
* %system: system time percent
* %iowait: CPU等待磁盘IO导致空闲状态消耗的时间比例
* %steal: 虚拟化相关
* %idle: CPU空闲时间比例

####2.3.监控信息的获取：iostat
	[root@master ~]# iostat -c 3 3
	Linux 2.6.32-431.el6.x86_64 (master) 	2015年12月09日 	_x86_64_	(4 CPU)

	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
               0.17    0.00    0.17    0.03    0.07   99.57

	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
               0.25    0.00    0.25    0.00    0.08   99.42

	avg-cpu:  %user   %nice %system %iowait  %steal   %idle
               0.25    0.00    0.08    0.00    0.08   99.58
####2.2.监控信息的获取：top

	[root@master ~]# top
	top - 17:21:19 up 123 days, 35 min,  9 users,  load average: 0.00, 0.00, 0.00
	Tasks: 324 total,   1 running, 323 sleeping,   0 stopped,   0 zombie
	Cpu(s):  0.2%us,  0.2%sy,  0.0%ni, 99.5%id,  0.0%wa,  0.0%hi,  0.0%si,  0.0%st
	
* us: user time percent
* sy: system time percent
* ni: user with nice percent
* id: idle
* wa: iowait
* hi: hard interrupt
* si: soft interrupt
* st: steal










 