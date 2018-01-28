## 概述

算法练习网站1：https://leetcode.com/

算法练习网站2：https://www.hackerrank.com/

算法定义：https://zh.wikipedia.org/wiki/%E7%AE%97%E6%B3%95

为啥学习算法（algorithm）？

推荐算法 -> 机器学习

深度学习 - 艾尔法 GO  
视觉算法 - 人脸识别/无人驾驶

分治算法思想：归并排序，快速排序...
贪心算法思想：最小生成树...
动态规划思想：最短路径...
递归搜索思想：树形结构...

## 排序算法 O(nlogn) - O(n^2)

各排序算法的对比：https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95

### Selection Sort选择排序O(n^2)

a.从N2-Nn选择最小的，和N1个交换(找最小的放在第一个)；
b.N1不动，从N3-Nn选择最小的，和第N2个交换（然后，着最小的放在第二个）；
...

C语言实现时，两个for循环都要执行一遍；

```python
N = [55,6,77,88,9,9,90,5,8,6,9,7,2,3,1,4,44]
def sort(N):
    for i in range(len(N)):
            for j in range(i, len(N)):
                if N[i] > N[j]:
                    N[i], N[j] = N[j], N[i]
    return N
print(sort(N))
```

### Isertion Sort插入排序O(n^2)-扑克牌

a.N2<N1，二者交换；
b.N3<N2,二者交换;新N2<N1，二者交换；
c....

C语言实现时，近乎有序的数字排序效率较高，推荐！！；



```python
N = [55,6,77,88,9,9,90,5,8,6,9,7,2,3,1,4,44]
def sort(N):
    for i in range(1,len(N)):
            for j in range(i):
                if N[i] < N[j]:
                    N[i], N[j] = N[j], N[i]
    return N
print(sort(N))
```

### Bubble Sort冒泡排序 O(n) - O(n^2)

性能整体没有插入排序高，参考：https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F

```python
def Bubble(array):
    array_len=len(array)
    for i in range(0,array_len-1,1):
        for j in range(array_len-1,i,-1):
            if array[j]<array[j-1]:
                temp=array[j]
                array[j]=array[j-1]
                array[j-1]=temp
    return array
```

### Shell Sort希尔排序O(n^3/2)

由插入排序衍生出的Shell Sort希尔排序，时间复杂度O(n^3/2)更好。

### Merge Sort 归并排序

分解：对元数组N进行二分；然后在二分...最后经过log2n（2为底）层，即可分为单个元素一组。  
然后逐级向上比较合并。

归并：假如归并过程(合并两个有序的数组为一个有序的数组)时间复杂度能实现为O(n)，那么总的时间复杂度为O(nlogn)

可以通过增加O(n)的空间复杂度，来实现归并过程为O(n)，现在计算机的时间效率比空间效率重要的多！！

当运算量n=100000时，n^2(10^10) 时 nlogn(1660964) 的6020倍，1天对15年！！

参考：https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F#Python

```python
from collections import deque

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    def merge(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge(left, right)
```

### 快速排序（quick sort）

参考：https://zh.wikipedia.org/wiki/快速排序

O(n log n)期望时间，O(n2)最坏情况；对于大的、随机数列表一般相信是最快的已知排序

快速排序（英语：Quicksort），又称划分交换排序（partition-exchange sort），一种排序算法，最早由东尼·霍尔提出。在平均状况下，排序 n个项目要 O(nlogn)（大O符号）次比较。在最坏状况下则需要 O(n^2)次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 O(nlogn)算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。


步骤为：

1、从数列中挑出一个元素，称为"基准"（pivot），
2、重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
2、递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

```python
def quicksort(lst, lo, hi):
     if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p)
        quicksort(lst, p+1, hi)
    return

def partition(lst, lo, hi):
    pivot = lst[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    if lst[hi-1] < lst[i+1]:
        lst[i+1], lst[hi-1] = lst[hi-1], lst[i+1]
    return i+1
```

### 堆排序（Heap sort）

动态的调整序列的优先级。

二叉堆：https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E5%A0%86

特点：一个父亲两个儿子，而且父亲>子节点，而且是完全二叉树（从上到下，从左到右，只有最后一个节点可以只包含一个儿子）

参考：https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F

在堆的数据结构中，堆中的最大值总是位于根节点(在优先队列中使用堆的话堆中的最小值位于根节点)。堆中定义以下几种操作：

1、最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点  
2、创建最大堆（Build_Max_Heap）：将堆所有数据重新排序  
3、堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算  

插入（最后一个非叶子节点）：shift up - 形成最大堆；  
取出（第一个父节点）：shift down - 形成最大堆

将n个元素逐个插入到一个空堆中，算法复杂度时O(nlogn)

heapify的过程(直接把n个元素的数组变成堆，然后进行shift up/shift down形成最大堆)，算法复杂度为O(n)


### 排序算法比较

详细参考： https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95

        |平均时间复杂度|原地排序|额外空间|是否稳定排序
插入排序： O(n^2) | 是 | O(1) | 是 |
归并排序： O(nlogn) | 否 | O(n) | 是 |
快速排序： O(nlogn) | 是 | O(logn) | 否 |
堆排序： O(nlogn) | 是 | O(1) | 否 |

## 二分搜索树

参考：https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%8F%89%E6%A0%91

用途：查找、搜索

特征：一个父亲，两个儿子，左孩子<父亲<右孩子；且，左侧节点大于右侧节点；

二分查找法：前提-有序队列，

二分搜索树-遍历节点：深度优先遍历（前/中/后序遍历） 和 广度优先遍历

二分搜索树-删除节点：删除最大值节点，删除最小值节点，删除只有一个孩子的节点，删除具有两个孩子的节点

平衡二叉树（红黑树）：防止二叉树退化成链表

## 并查集 Union Find

参考：https://zh.wikipedia.org/wiki/%E5%B9%B6%E6%9F%A5%E9%9B%86

应用：高效的解决“连接问题”

Quick Find
Quick Union

## 图论 Graph Theory 

参考：https://zh.wikipedia.org/wiki/%E5%9B%BE%E8%AE%BA

点（节点）、线（边）

有向图、无向图

有权图、无权图

邻接表、邻接矩阵

遍历：深度优先、广度优先

最短路径

## 最小生成树

带权五向连通图

定义：所有V个点之间均有联通，找到V-1条边使得所有点联通，且费用最低。

应用：电缆布线图、网络设计、电路设计等等

参考：https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91

切分定理：给定任意切分，横切边中权值最小的边必然属于最小生成树。

最小生成树-Prim算法：先随机选一个点，当作横切的红色阵营，其他是蓝色阵营，找到权值最小的横切边，并把连接的点加入到蓝色阵营；一次类推（排除在同一阵营的边）...

最小生成树-Kruskal算法：把所有的边的权值排序，以此用权值最小的边连接，只要不构成环（使用Union Find判断），最终结果就是最小生成树。

## 最短路径

参考：https://zh.wikipedia.org/wiki/%E6%9C%80%E7%9F%AD%E8%B7%AF%E9%97%AE%E9%A2%98

定义：一个点到另一个点的最节约路径

应用：路径规划

最短路径树（图论里面的广度优先遍历）

dijkstra单源最短路径算法：前提-不能有负权边，

处理负权边

Bellman-Ford单源最短路径：前提-不能有负权环

## 总结

各种排序算法：

基础数据结构和算法的实现：堆、二叉树、图

基础数据结构的使用：链表、栈、队列、哈希表、图、Trie、并查表

基础算法：深度优先、广度优先、二分查找、递归...

基础算法思想：  

1、分治：归并排序、快速排序、树结构  
2、贪心：选择排序、堆、Kruskal、Prim  
3、递归回溯：树的遍历、图的遍历  
4、动态规划：Prim、Dijkstra  
