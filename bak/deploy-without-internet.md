# 快速部署的解决方案
在中远临时代理周琦的两天里，深切感受到一个极其痛苦的问题－－－－－－如何在客户的机器完全不能上网的情况下，安装自己公司的产品

* 自己之前也碰到过，比如在海通证券部署时，就出现过这个问题
为了彻底解决此问题，自己想到的一个思路，就是完全用docker部署，单纯的docker-compose部署

## 思路
**核心思路是全程离线**

1， 首先要在自己的环境下，用一台虚拟机，编号vm1（host-only），部署一下最小化安装的系统，与客户提供的系统完全一样，以中远为例，使用centos7.6，minimal，不要再安装任何软件

* 估计装个vim-minimal不成问题

2，创建另一台虚拟机，编号vm2，网络无论是nat，还是bridge，都行，版本也是centos-7.6 minimal，

3， 在vm2上，先用离线模式，安装docker，然后使用Dockerfile等，compose等手段，部署好系统，最后把构建好的镜像，全部用docker save下载下来，在vm1上，用docker load上传上去，然后跑docker-compose就行了，估计稍加修改，就可以跑起来了

4，最后一步，再确认此方案可行后，接下来就是优化镜像的大小了


