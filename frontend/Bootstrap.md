# 容器

- 流体容器`.container-fluid`: `width=auto`(width的默认值)
- 固定容器`.container`:(三个阈值,四个状态)
    - 窗口>1200px(lg 大屏PC) 版心width:1170px(1140+槽宽)
    - 窗口>992px(md 中屏PC) 版心width:970px(940+槽宽)
    - 窗口>768px(sm 平板) 版心width:750px(720+槽宽)
    - 窗口<768px(xs 移动手机) 版心width:auto

    > 我们一般使用固定容器!    
    > 100%表示为子元素宽度为父元素宽度的100%, 设置margin/padding会撑开子元素;
    > auto表示子元素宽度=父元素宽度-margin-padding-width

- 栅格系统
    - 栅格必须用容器包裹, 一个容器N行
    - 一行总共12列
    - 列可以排序/偏移/嵌套
    - 列排序是只能顺序写: lg > md > sm > xs 尾部可以省略,中间不能跳过(中间即使不需要排序,也要写`col-md-pull-0`)
    
    ```html
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <link rel="stylesheet" href="./css/bootstrap.css">
        <style>
            .container {
                background-color: pink;
            }
            
            div[class|="col-lg"] {
                border: 1px solid #000;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-lg-10">col-lg-10</div>
                <div class="col-lg-2">col-lg-2</div>
            </div>
            <div class="row">
                <div class="col-lg-3">col-lg-3</div>
                <div class="col-lg-6">col-lg-6</div>
                <div class="col-lg-3">col-lg-3</div>
            </div>
        </div>
    </body>
    ```

# 栅格系统源码分析

- 固定容器&流体容器的公共样式
    ```less
    margin-right: auto;
    margin-left: auto;
    padding-left: 15px;
    padding-right: 15px;
    ```
- 固定容器的特定样式
    ```less
    @media (min-width: @screen-sm-min) {
      width: @container-sm;
    }
    @media (min-width: @screen-md-min) {
      width: @container-md;
    }
    @media (min-width: @screen-lg-min) {
      width: @container-lg;
    }
    // 尺寸必须从小到大,顺序不可变
    ```
- 行
    ```css
    margin-left: -15px;
    margin-right: -15px;
    ```
- 列
    - 公共样式: `.make-grid-columns()`:
        ```less
        .col-xs-1,.col-sm-1,.col-md-1,.col-lg-1,
        .col-xs-2,.col-sm-2,.col-md-2,.col-lg-2,
        ...
        .col-xs-12,.col-sm-12,.col-md-12,.col-lg-12 {
          position: relative;
          min-height: 1px;
          padding-left: 15px;
          padding-right: 15px;
        }
        ```
    - .make-grid(xs):
        ```less
        //float和width(1~12)
        .float-grid-columns(@class);
          * .col-xs-1,.col-xs-2, ... .col-xs-12 {
          *   float: left;
          * }
        .loop-grid-columns(@grid-columns, @class, width); //列宽
          * .col-xs-12 {
          *   width: 12/12;
          * }          
          * .col-xs-11 {
          *   width: 11/12;
          * } 
          * ...         
          * .col-xs-1 {
          *   width: 1/12;
          * }
        //left和right:列排序(0~12)
        .loop-grid-columns(@grid-columns, @class, pull); //列排序
        .loop-grid-columns(@grid-columns, @class, push); //列排序
        //margin-left:列偏移(0~12)
        .loop-grid-columns(@grid-columns, @class, offset); //列偏移
        ```

# 自定义栅格系统

修改源码中的`grid.less`中的`.col-xs-n`为`.yaro-col-xs-n`, 并把相关的less重新编译成一个单独的css文件即可.

# 响应式工具

通过设置不同的类,可以控制元素在特定尺寸屏幕上的显示/隐藏

![响应式工具.png](https://i.loli.net/2019/03/10/5c847e44f0d84.png)

# 栅格盒模型设计的精妙之处

BootStrap盒模型的介绍:
- 容器两边具有15px的padding;
- 行  两边具有-15px的margin;
- 列  两边具有15px的padding;

这么设计的原因:
- 为了避免列之间的内容挤在一起,设计了槽宽;
- 为了维护槽宽30px,列两边必须有15px的padding;
- 为了能使列里面嵌套行,行两边必须有-15px的margin,否则,嵌套后的盒子槽宽为(15+30)px;
- 为了让容器能包裹住行,容器两边必须有15px的padding,否则,行会溢出到容器外面;

# BootStrap实例

步骤如下:
- 网站实现步骤: 首先使用UI库打底, 然后自己微调;
- 在官网查找相应的`组件(静态)/插件(动态)`拼凑目标网站;
- 在官网查找`全局CSS样式`处理细节;
- 一些UI库无法完成的功能,自己实现;

其他说明:
- 使用BootStrap的轮播图时,如果需要img响应式,查找其提供的`全局CSS样式`,也可自己添加`img {width: 100%}`样式;
- 设置/调整div大小等数据时,不建议使用BootStrap自带的类,建议添加自己的的类(如:`yaro-xxx`);


# BootStrap定制化

如果需要修改槽宽/配色等, 可以自定义:

- 方法1(不推荐): 修改源码->重新编译:
    1. 修改源码中`less/variables.less` 中相关变量;
    2. 使用`Koala`等工具编译:编译入口文件`bootstrap.less`(会自动合并其他需要`import`的less文件);
    3. 只使用入口文件`bootstrap.less`生成的`bootstrap.css`即可;
    
    > 缺点: 修改了源码;
    
- 方法2(推荐): 新建文件,引入源码入口文件,编译;
    1. 新建文件`yaro.less`文件,写入如下内容:
        ```less
        @import "../less/bootstrap.less"; // 引入入口文件
        @grid-gutter-width: 200px; // 重写(槽宽)变量
        ```
    2. 使用`Koala`等工具直接编译`yaro.less`文件;
    3. 只使用入口文件`yaro.less`生成的`yaro.css`即可;
- 方法3: 覆盖原来的样式;
    遇到一些小的修改,自己书写样式覆盖原来的样式即可;
