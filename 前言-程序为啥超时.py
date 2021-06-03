

序言: 
大家在刷LeetCode时经常会遇到"超出时间限制"
一般系统判定的超时时间为1s,LeetCode上面的题目基本上都是1s

=== 1 从电脑配置上面看计算机性能

(1)配置 cpu
 2.7G Hz 奔腾 双核 i5
 1Hz = 1/s

(2)计算
 1G Hz = 1000MHz(兆赫)
 1MHz = 1百万赫兹
 1GHz = 10亿Hz  表示cpu 1s可以运行10亿次
 而2.7G加上双核就是  10亿 * 2.7 * 2 = 54 亿
 理论上该计算机 1s 可以运行54亿次

(3)计算机底层运行逻辑
eg: 
1 cpu执行一次完成的乘法，需要设计到寄存器的使用，还有其他数据处理的操作
2 cpu也要执行计算机其他进程的任务，我们的程序只是其中一个罢了

(4)总结
需要实际测试一下才知道1s真正执行多少次操作 (理论是54亿次)

=== 2 测试一下计算机的运行速度

算法基本上设计 O(n),O(n^2),O(nlogn)这几种时间复杂度

def function1(n):
    k = 0
	for i in n:
		k += 1 

def function2(n):
	k = 0
	for i in n:
		for j in n:
			k += 1

def function3(n):
	k = 0 
	for i in n:
		while j < i:
			j = j * 2
			k += 1

import time
def test_time(n)
	start = time.time()
	function1(n)
	function2(n)
	function3(n)
	end = time.time()
	return end - start

测试结果:
(1) 以function1  O(n) 为例
n = 1 * 10^8 
time = 197ms
n = 1 * 10^9
time = 1946ms
n = 5 * 10^8
time = 972ms

1s = 1000ms
当n = 5 * 10^8 时,运行时间为1s

(2)根据O(n) 预估 O(n^2)运行时间为1s时n的取值
5 * 10^8 开平方等于 22300
测试function2 O(n^2)
当n = 22500 时，time = 987ms (接近1s)

(3)根据O(n) 预估O(nlogn)运行时间为1s时n的取值
计算后得知 n = 2 * 10^7
测试function3 O(nlogn)
当n = 2 * 10^7 时，time = 981ms (接近1s)


=== 3 总结:
(1) 估计准确，时间复杂度之间的关系和运行时长成线性关系，说明时间复杂度可以等价于运行时长来判定程序运行时间。
(2) 由上述的结果可以看出，LeetCode达到 O(n)基本上可以通过，如若未通过，则需要 O(logn)
(3) O(n^2) >> O(nlogn) >> O(n) >> O(logn) >> O(1) , 最高只能到 O(nlogn)，LeetCode可以通过。
(4) 写程序时就要考虑到时间复杂度为 O(n)的一些解法









