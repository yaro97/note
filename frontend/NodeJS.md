# 概述

## 为什么学习Node.js

企业需求:
- 具有服务端开发经验更好
- Front-end & back-end
- 全栈(干)工程师
- 基本网站开发能力
    - 服务端
    - 前端
    - 运维部署

## Node.js是什么

- Node.js® is a JavaScript runtime built on [Chrome's V8 JavaScript eng](https://developers.google.com/v8/).
	- `不是一门语言`;
	- `不是库,不是框架`;
	- `是JS运行时(runtime)的环境`;
	- 简单来讲就是:`Node.js可以解析和执行JS代码`;
	- 以前只有浏览器可以解析执行JS代码;
	- 也就是说现在的JS可以完全脱离浏览器来运行,这一切都归功于:Node.js;
	- 构建于Chrome V8引擎之上:
		- 代码只是具有特定格式的字符串;
		- 引擎可以识别,解析,执行;
		- Chrome V8引擎是目前公认的解析执行JS代码最快的;
		- Node的作者吧V8引擎移植出来,开发了一个独立的运行时环境;
- 浏览器中的JS:
	- EcmaScript
		- 基础语法
		- 分支/循环
		- 函数
		- 对象
	- BOM
	- DOM
- Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient.
	- event-driven事件驱动
	- non-blocking I/O model 非阻塞IO模型(异步)
	- 轻量/高效
- Node.js' package ecosystem , npm, is the largest ecosystem  of open source libraries in the world.
	- 类似于python 的pip工具,可以安装很多开源的包;
	- npm install jquery

## JS与Node.js区别

- 二者的环境不同
	- JS是基于浏览器的JavaScript(前端JS)
	- Node.js是基于服务器的JavaScript(后端Node.js)
- 二者的语法相同,组成不同:
	- JavaScript
		- ECMAScript(语法基础:语法,数据类型,内置对象...)
		- DOM(操作页面元素的方法)
		- BOM(操作浏览器的方法)
	- Node.js
		- ECMAScript(语法基础:语法,数据类型,内置对象...)
		- OS(操作系统)
		- fs(文件系统)
		- net(网络系统)
		- database(数据库)

## Node.js能做什么

1. Web服务器后台
2. 命令行工具(类似于git <- 使用C开发)
	- npm
	- hexo
- 对于前端工程师来说,接触最多的就是他的命令行工具:
	- webpack
	- gulp
	- npm

## 需要哪些知识

- html
- CSS
- JS
- 简单的命令行操作
- 具有服务端开发经验更佳

## 一些资源

- <深入浅出Node.js>
	- 偏底层/原理
	- 没有任何实战内容
- <Node.js权威指南>
	- API讲解
	- 也没有业务, 没有实战
- Node入门: https://www.nodebeginner.org/index-zh-cn.html
- Javascript标准参考教程 - 阮一峰
- Node官方API
- CNODE社区: http://cnodejs.org

## 本课程能学到啥?

- B/S编程模型
	- 任何服务端技术B/S编程模型都是一样的,和语言无关;
	- Node只是作为我们学习B/S编程模型的工具而已;
- 模块化编程
	- RequireJS
	- SeaJS
	- CSS也支持 `@import('文件路径')`
	- 以前认知的JS只能通过script编程来加载;
	- 所谓模块化编程: 在Node中可以像`@import`一样来引用加载JS脚本文件.
- Node常用API
- 异步编程
	- 回调函数
	- Promise
	- async
	- generator
- Express Web开发框架
- Ecmascript6
	- 在课程中穿插讲解;
	- 他只是一个新的语法而已.
- 学习Node不可可以帮助打开服务端黑盒子,同事帮助你学习前端高级内容,如
	- vue
	- react
	- angular...

## 起步

- 安装
	- node -v
	- npm -v
- 运行文件
	- node xxx.js

