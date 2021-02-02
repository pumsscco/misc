# C源代码目录
集中放置全部的c代码，可能是书中的范例，也可能是自己的项目或脚本的代码

* 近期会以场景系列目录中的怪物以及其行踪信息的分析为主，兼带NPC的信息，可参考gameobj.gob的golang版分析代码；**终级目标是多线程，并发处理500个以上的文件**

## 怪物信息分析
已经完成了全部的字段分析，规划按下面的模式来

char *props 
"AABPedestrian_MST_run_max_speed: 200.0, 3"

最开始的四个字节，为记录数
## 信息头
每条记录，行为之前的部分，可以称之为头部，此部分大小固定，核心就是其id，模式，初始坐标，以及其具体怪物ID
## 怪物行为字段分析
怪物行为分两大类，一类比较复杂，一类比较简单

* 目前看来，绝大部分字段只有两个参数，且均为整数
* 复杂行为以**MSTINFO_Behavior**的第二参数为1，做为标志
其中GroupName与PathWayID的第一个参数为字符串，而ExpectTime/WaitTime/max_force/max_speed，则参数1为浮点数；
pathfollow带4个参数
* 简单行为则**MSTINFO_Behavior**的4个参数固定为0 0 1 1

以下为二类行为共有的属性字段

* BufferCache, combat_pos, pursuit_speed, script_func
* combat_pos比较特殊，数量不定，因此要结合下一个字段是否仍含有combat_pos来判定此段结束与否
* pursuit_speed参数1也为浮点数；
* 每条记录按说是以script func为结束字段，但实际上该字段有可能没有
在max_pursuit_speed处理结束后，需要备份文件指针位置，然后读取下一个字段，确认其为script，否则，回退指针，进入下一条记录的处理

* script func的处理，
