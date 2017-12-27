# Pycharm Tips Ticks使用技巧总结

## Tips & Ticks

- 快捷键参考： - Pycharm（JetBrain）快捷键参考：https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf

## Productive Coding

- code completion, code inspection, quick fixes, code refactoring(重构), language injection(python可以返回html) 等等
- ctrl+shift+y  重新加载文件
- ctrl+shift+a 命令菜单
- ctrl+J 选择代码块 snippets,设置：live Templates 可以自定义
- ctrl+alt+L  格式化代码
- tab 鼠标在行中缩进的话，选择部分文字即可；
- alt+enter 万能补全：
  - 自动创建没有的函数。
  - 不需要import，直接使用，然后alt + enter 自动导入；
  - 自动缩进
  - 转变literal字典到constructor字典（设置-intentions）；
  - 在创建类时，自动创建实例的属性（self.name=name）;
  - inject language or reference（注入其他语言），可以返回html；

ctrl+alt+m 在class中把code转变成method，(refactor-extract method)

>代码重构（英语：Code refactoring）指对软件代码做任何更动以增加可读性或者简化结构而不影响输出结果。
软件重构需要借助工具完成，重构工具能够修改代码同时修改所有引用该代码的地方。

ctrl+Q/shift+F1 可以快速的查看 Quick Documentation/External Documentation（View菜单）

## Code Navigation

### file Navigation

- Ctrl+Shift+n  快速搜索文件（Navigate菜单）；
- Ctrl+n  快速搜索Class（Navigate菜单）；
- Ctrl+Shift+Alt+n  快速搜索Symbol（Navigate菜单）；
- Ctrl+E 最近打开的文件（View菜单）；
- 可以把常用的文件添加到Favorite（文件菜单）；
- 项目列表的文件夹-右键，可以搜索相应文件的内容，从而定位文件；
- shift shift 可以搜索所有东西（可以提前选择要搜索的对象）

## code structure Navigation

- Ctrl+B 或者 Ctrl+单击 ： 查看 declaration ；
- Alt+F7 右键（find usage） 查看usage；
- F11 添加标签（针对于line of code）

## Pycharm command Navigation

- Pycharm命令太多，可以使用Ctrl+Shift+A，快速输入命令；
- Alt+(1~9 ) 可以快速定位到工具窗口（View菜单）

## Debugging

- 错误track到最后一行；
- Shift+F10运行
- Shift-F9 Debug

## Testing

## Customizing

- codeglance