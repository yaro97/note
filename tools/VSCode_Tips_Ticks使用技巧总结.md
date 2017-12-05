# VSCode 使用技巧总结

## Tips & Ticks

- 记得常用 palette;

- 善用Welcome窗口：Help-Wlecome；

- Alt+Z Toggle Word Wrap;

- User配置针对VSCode软件；Workspace配置针对工作区（项目），项目下会有个 `.vscode`的配置文件夹；

- 配置使用Syncing插件GList同步（Ctrl+Shift+P）。

- Keybinding 可以单独设置，可以通过插件使用其他IDE/Editor的，可以在设置页面右键检查Conflicts；

- 全项目搜索：Ctrl+Shift+F； Ctrl+Shift+J可以自定义；

- 善用 python code snippets，最好自己收集适合自己的；

- VSCode 中 Python 相关点参考：https://code.visualstudio.com/docs/python/python-tutorial

- 版本控制参考：https://code.visualstudio.com/docs/editor/versioncontrol

- VSCode快捷键参考：https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf

- Pycharm（JetBrain）快捷键参考：https://resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf

## Multi-Cursor Editing:

Shift+Alt+UpArrow or Shift+Alt+DownArrow
Ctrl+Click to add a cursor anywhere.
Ctrl+Shift+L.定位到所有相同的字段.

## IntelliSense：

- Tab/Enter 插入提示的代码；
- 特殊字符触发，如 `.` 等；
- Ctrl+Space 手动触发；
- 触发单元以图形表示，有函数/方法、变量、类、模块、属性、值、关键字、等等；

## Line Actions

- Ctrl+Shift+Alt+DownArrow or Ctrl+Shift+Alt+UpArrow ：Copy a line and insert it above or below the current position.
- Alt+UpArrow and Alt+DownArrow Move an entire line or selection of lines up or down respectively.
- Delete the entire line with Ctrl+Shift+K.

## Rename Refactoring

- F2 or 右键 可以方便的重命名 function name or variable name，所有变量同时改变；

## Refactoring via Extraction

- 概念：想把某个变量、代码段单独提取出来，比如把某个变量提取成全局变量，方便我们后期维护（只修改全局变量即可）；
- Press Ctrl+. 或者点击小灯泡（the little light bulb ），会自动提取，并引用；

## Formatting

- Ctrl+Shift+I 全文格式化
- Ctrl+K Ctrl+F 选中部分格式化
- 也可以右键

## Code Folding

- Ctrl+Shift+[ / ] Fold and Unfold.
- 也可以点击左边gutter的 +/- icons
- Ctrl+K Ctrl+0 Fold all sections
- Ctrl+K Ctrl+J Unfold all
- Ctrl+K Ctrl+n 可以指定折叠代码levels；

## Errors and Warnings

- F8 消灭“波浪号” - 错误提示

## Go to Symbol/Definition/Implementation

- Ctrl+Shift+O Navigate symbols inside a file,也可以 Ctrl+P 之后输入 “@” 符号；
- F12 快速定位到函数的定义；
- Ctrl+F12 快速定位到函数的调用；
- Ctrl+Click jump to the definition ；Ctrl+Alt+Click open the definition to the side with .

## Code Navigation

- Ctrl+P 快速打开项目中的文件
- Ctrl+Tab 切换已打开的窗口；
- Ctrl+PageDown/PageUp 切换已打开的窗口
- Ctrl+Alt+- and Ctrl+Shift+- 快速的在 File and Edit Locations 切换，快速切换到刚刚编辑的位置；


## Split Windows

- Ctrl+\ Split the active editor into two或者右上角的按钮.
- Ctrl + click on a file in the Explorer.
- Open to the Side from the Explorer context menu on a file.
- Ctrl+Enter in the Quick Open (Ctrl+P) file list.
- Drag and drop a file to the either side of the editor region.
- Ctrl+1/2/3 左/中/右editor group切换.
- Shift+Alt+1 默认切换是水平/垂直分隔窗口，当然可以使用“View: Toggle Editor Group Vertical/ Layout”命令

