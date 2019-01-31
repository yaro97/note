# 最终webpack配置

## package.json

```json
{
    "name": "webapck-study",
    "version": "1.0.0",
    "description": " ",
    "main": "webpack.config.js",
    "dependencies": {
        "@babel/core": "^7.2.2",
        "@babel/preset-env": "^7.2.3",
        "babel-loader": "^8.0.0-beta.0",
        "bootstrap": "^3.4.0",
        "jquery": "^3.3.1"
    },
    "devDependencies": {
        "browser-sync": "^2.26.3",
        "clean-webpack-plugin": "^1.0.0",
        "css-loader": "^2.1.0",
        "file-loader": "^3.0.1",
        "html-webpack-plugin": "^3.2.0",
        "less": "^3.9.0",
        "less-loader": "^4.1.0",
        "node-sass": "^4.11.0",
        "sass-loader": "^7.1.0",
        "style-loader": "^0.23.1",
        "url-loader": "^1.1.2",
        "webpack": "^4.28.1",
        "webpack-cli": "^3.2.1",
        "webpack-dev-server": "^3.1.14"
    },
    "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "build": "webpack",
        "dev": "webpack-dev-server --open --port 3100 --contentBase src --hot",
        "sync": "browser-sync start --proxy localhost:3100"
    },
    "keywords": [],
    "author": "",
    "license": "ISC"
}

```
## webpack.config.js

```js
const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const CleanWebpackPlugin = require('clean-webpack-plugin')
module.exports = {
    entry: {
        index: './src/main.js' //单个入口
    },
    output: {
        filename: 'bundle.js', //指定输出的文件名
        path: path.resolve(__dirname, './dist/') //输出的绝对路径(用resolve解析出来的)
    },
    devtool: 'cheap-module-eval-source-map', //开发, 生产环境不推荐开启,或者推荐：cheap-module-source-map
    module: {
        rules: [
            { test: /\.js$/, exclude: '/node_modules/', use: { loader: 'babel-loader' } }, // es6相关loader
            { test: /\.css$/, use: ['style-loader?sourceMap=true', 'css-loader?sourceMap=true'] }, // css相关
            { test: /\.less$/, use: ['style-loader?sourceMap=true', 'css-loader?sourceMap=true', 'less-loader?sourceMap=true'] }, // less相关
            { test: /\.scss$/, use: ['style-loader?sourceMap=true', 'css-loader?sourceMap=true', 'sass-loader?sourceMap=true'] }, // scss相关
            { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader?limit=174562&name=[hash:8]-[name].[ext]' }, //处理图片url//参数单位为字节, < 174562 转换, >= 174562 不转换.
            { test: /\.(svg|eot|ttf|woff|woff2)$/, use: 'url-loader' } //处理字体url
        ]
    },
    plugins: [
        new CleanWebpackPlugin(['dist']), //build前删除dist
        new HtmlWebpackPlugin({
            template: path.join(__dirname, './src/index.html'), //根据那个模板生成内存中的html页面
            filename: 'index.html', //指定内存生成的html名称
        }),
    ],
    mode: 'development' // 'production' 'none' built-in optimizations accordingly.
}

```

## .babelrc

```conf
//.babelrc
{
    "presets": [
        ["@babel/preset-env", {
            "targets": {
                // The % refers to the global coverage of users from browserslist
                // "browsers": [">0.25%", "last 2 versions"]
                "browsers": [">50%", "last 2 versions"]
            }
        }]
    ]
}
```

# Webpack工作流概述

## 工作流简介

前端的发展:

1. 库时代:静态, dojo, jquery, kissy prototype...
2. 模块(MVC): Backbone.js , underscore.js, require.js, jquery...
3. MVVM: 单页面(Ajax+#), Angular(google), React(facebook), Vue(尤雨溪) -->都支持Webpack(同时支持AMD/Commonjs/ESM--ES6官网--抄袭python)

和gulp的关系:

- `gulp核心是工作流程控制,通过很多插件可以实现,编译/压缩/改名/混淆/ES6/base64...`
- `webpack核心是构建模块(符合AMD/CMD/ESM..规范),通过loader可以实现ES6/编译/压缩/处理图片/base64...`
- gulp中的很多任务,在wepack中通过loader都可以变相的实现:
- 如: 编译less/打包:
	- Webpack可以编译less,属于"奇淫技巧";
	- 首先需要在js文件中引入样式文件(import xxx.less/css);
	- 显示把less文件读入js文件;
	- 然后动态添加到head中(网站只有html和js文件);
	- 当然可以使用extract来提炼成单独的css文件.

概述:

- 工作流如: 
	- ES6编译, 打包...
	- Less/Sass -> CSS
	- CSS Autoprefixer 前缀自动补全
	- CSS 压缩合并
	- CSS Sprite 雪碧图合成
	- Retina @2x & @3x 自动生成适配
	- imagemin 图片压缩
	- JS 合并压缩
	- EJS 模版语言
	- ...
- 一种实现:
- webpack负责构建CMD模块，gulp负责编译less、合并css、混淆、更改base64。
- 主要思想就是webpack被gulp操作，webpack成为了gulp工作流中的一个环节。
	- `webpack要实时监听js文件的改变，如果有js文件发生变化了，此时就要重新生成bundle.js`。
	- `gulp要实时监听less文件的改变，如果有less文件发生变化了，此时就要重新生成all.css`。
	- 但是不优雅 - 需要开启两个cmd窗口,一个是gulp,一个是wepack
- 优雅的实现: 
	- gulp在指挥webpack工作--把webpack包装成gulp一个任务;
	- 此时要注意，所有的监听要交给gulp，webpack中不要安装任何的watch、实时更新的插件。
	- 把webpack当做一个含有babel功能的大构建器。

## 为什么使用webpack

网页中引入静态文件后产生的问题:
- 网页加载速度慢 <- 很多二次请求
- 需要处理复杂的依赖关系(web引用bootstrap,bootstrap引用jquery...)

如何解决上面的问题:
- 合并/压缩/精灵图/小图片的base64编码
- 使用RequireJS等解决依赖关系

如何完美实现上面的解决方案: 
- Gulp - 基于task任务的, 很多小任务组成任务流,一个任务解决一个难题.
- Wabpack - 基于整个项目进行构建: 

webpack的作用:
- Webpack能够处理js文件夹之间的依赖(解决jquery中的相关依赖)
- Webpack能够处理的JS的兼容问题(处理import 等语句)

什么是webpack:`是前端构建工具, 基于Node.js开发出来的前端工具`

## npm/静态资源/概念

npm安装:
- npm install nrm -g
- nrm ls
- nrm use cnpm/taobao(库)
- npm install xxx
- npm config list
- 说明: 
	- 建议使用nrm - 只是修改库而已,工具还是npm; 
	- 如果使用cnpm - 源修改为taobao, 工具也修改为cnpm工具,

前端常见静态资源:
- js: .js .jsx .coffee .ts
- css: .css .less .sass/.scss
- images: .jpg .png .gif .bmp .svg
- 字体: .svg .ttf .eot .woff .woff2
- 模板:  .ejs .jad .vue(这是webpack中定义组件的方式,推荐)

Webpack相关概念:
- chunk	块, 代码块
	 module	模块--虚拟后的
	 bundle	捆, 打包后的一捆代码
	 Entry	入口js文件(可以多个), 从入口文件开始遍历所有的依赖模块
	 Output	一个/多个JS文件,打包后形成的JS文件,供生产用
	 Loader	装载机, Webpack初衷只处理JS, 有了装载机,可以处理其他格式文件(模块), 常用的有编译类/样式类/文件类Loader
	 Plugins	与装载机的区别: 参与打包的整个过程,常常是优化/打包相关

# 初始化项目/配置

- 项目目录
![](http://ww1.sinaimg.cn/large/48356ef5ly1fzpxn22cnbj206504kq2s.jpg)

- 引用jquery
    - npm init -y //在项目根目录执行,初始化
    - npm i jquery -S  //安装jquery --save
    - <!-- 不推荐在html文件中引入任何包/css文件 -->
    - 只需要在index.html文件中引入 ../bundle.js即可(打包后的文件)

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <!-- 不推荐在html文件中引入任何包/css文件 -->
        <script src="../dist/bundle.js"></script>
    </head>
    <body>
        <ul>
            <li>这是第1个li</li>
            <li>这是第2个li</li>
            <li>这是第3个li</li>
            <li>这是第4个li</li>
            <li>这是第5个li</li>
        </ul>
    </body>
    </html>
    ```

- 入口文件main.js
    在这用es6语法引入相关文件即可

    ```js
    // main.js文件 --项目的js入口文件
    //导入jquery

    import $ from 'jquery' //ES6模块管理-推荐
    // const $ = require('jquery') //不推荐

    $(function () {
        $('li:odd').css('background-color', 'red')
        $('li:even').css('background-color', function () {
            return '#' + 'D97634'
        })
    })
    ```

- webpack.config.js配置

    ```js
    const path = require('path')
    module.exports = {
        entry: {
            index: "./src/main.js" //单个入口
        },
        output: {
            filename: 'bundle.js', //指定输出的文件名
            path: path.resolve(__dirname, "./dist/") //输出的绝对路径
        },
        module: {...},
     }

    ```

- webpack调用第三方loader机理分析
    1. 从入口entry文件开始,分析import语句;
    2. 遇到webpack不能处理的文件(后缀名), 便去调用第三方loader(匹配配置文件中的正则语法);
    3. 匹配成功的话,
        a. 调用执行相应的loader;
        b. 而且loader调用的顺序为: 从右到左/从下到上;
        c. 所有loader执行完毕后,把结果交给webpack打包/合并到bundle.js(output文件)中.
    4. 匹配不成功则报错.

# 编译ES6

## 安装babel相关

安装
- 官网: https://webpack.js.org/loaders/babel-loader/
- polyfill的官网: https://babeljs.io/docs/en/babel-polyfill
- `具体见官网`,下面只是参考

    ```sh
    - npm install -D babel-loader@7 babel-core babel-preset-env webpack 
    `切记.bablerc里面的配置也要使用对应最新的`
    - npm install --save @babel/polyfill
    ```

## 配置/使用

1. 使用上面的官网文档安装相关npm包;
2. 新建 .babelrc 文件,如下内容(具体见官网)

    ```conf
    //.babelrc

    {
        "presets": [
            ["@babel/preset-env", {
                "targets": {
                    // The % refers to the global coverage of users from browserslist
                    "browsers": [">0.25%", "last 2 versions"]
                }
            }]
        ]
    }
    ```

3. 新建 webpack.config.js 文件,如下内容,具体见官网

    ```js
    //webpack.config.js
    const path = require('path');
    module.exports = {
        mode: "production", // "production" | "development" | "none" built-in optimizations accordingly.
        
        // entry: './src/js/app.js',
        entry: './app.js', //入口--从哪儿开始分析模块依赖
        
        output: { //出口--输出文件
            filename: '[name].[hash:8].js', //输出的文件名--[name]值entry中的那么
            // filename: 'bundle.js',
            path: path.resolve(__dirname, '') //输出的路径
        },
        
        module: { //使用了哪些loader(模块)
            rules: [{ //定义规则
                test: /\.js$/, //检测哪些文件--正则
                exclude: '/node_modules/', //排除那些文件不检查
                use: {
                    loader: 'babel-loader' //使用babel-loader
                }
            }]
        }
    }
    ```

4.  (在 entry js文件 最上面 中添加) 

    ```js
    import '@babel/polyfill'
    ```

## 相关说明

1. webpack只能处理一部分ES6语法, 很多ES6甚至ES7语法需要第三方loader来处理 -- 把高级的语法编译成低级的语法后,再交给webpack打包到bundle.js中.
2. webpack.config.js中配置时,需要排除掉node_modules目录.
3. 把babel相关的配置独立到 .babelrc 文件中 --`json文件,记得符合json规范(无注释/双引号)`.

## Babel/Babel Presets--语法上的转换

1. babel-core 只是内核
2. babel-loader 官网是和webpack配合的loader
3. babel-preset-env  是指定预设的编译版本
	- babel只是一个编译器,我们需要为他指定预设的编译版本:
		- ES2015
		- ES2016
		- ES2017
		- env(常用): 包括前面三个以及 latest
		- babel-preset-react(自定义的一些)
		- [更多](https://babeljs.io/docs/en/presets)

## polyfil函数/方法的转换

`@babel/polyfill` 前面三个只是ES6语法上的转化,函数/方法(Generator/Set/Map/Array的新方法....)还需要另外的插件
- [polyfill的官网](https://babeljs.io/docs/en/babel-polyfill): 
    - 垫片/垫桌子 --各个浏览器对ES6的支持不同,所以我们需要个垫片平衡下.
    - 全局垫片 - 把所有的新API在全局里面进行定义 -> 会污染全局变量;
    - `为开发应用准备` - 如网站等等...不适合框架的开发,如开发vue/react等等
    - 使用: 
        - `polyfill的安装版本需要和前面三个的配套--使用最新的官网`;
        - 安装见官网: 
        - `import '@babel/polyfill'`  (在js入口文件中引入)
- [Babel Runtime Transform官网](https://babeljs.io/docs/en/babel-plugin-transform-runtime)
    - 局部垫片 -> 不会污染全局 <- 只在局部添加新的变量;
    - `为开发框架而准备` - 比如你开发一个框架给别人使用;
    - 安装使用见官网;

# webpack-dev-server

## webpack-dev-server介绍

- `npm i webpack-dev-server -D`
- 本地安装 -> 无法直接执行 webpack-dev-server 命令 -> 需要在package.json中scripts中配置
- 切记: webpack-dev-server 打包的bundle.js文件`在内存中(快!)` - > 默认通过 `服务器/ 根目录可以映射访问(硬盘中并没有)`, 所以, index.html引用地址需要修改为 /bundle.js 
- 修改代码会自动编译,且刷新服务器! - `但是各个终端不会同步操作` -> `使用browser-sync代理`

## webpack-dev-server使用

- 方式一(`推荐`): package.json中scripts中配置: 
    ```
    "dev": "webpack-dev-server --open --port 3000 --contentBase src --hot"
    ```
	- --open 自动打开浏览器
	- --contentBase 设置内存中的虚拟服务器的虚拟目录, 默认是项目根目录
	- --hot 开启热刷新
		- 样式: 只要有此选项,样式的修改便可以热刷新 -> `页面不刷新便能重载修改后的样式`.
		- js文件: 修改JS文件会只编译修改后的内容, 生成 `hot-update.js等文件, 然后以补丁的方式追加到页面`, -> 但是`页面还是会刷新才能重载修改后的JS内容`.如果`也需要热更新, 只需要在入口文件 main.js 的最后面,追加如下内容`:

            ```js
            if (module.hot) {
                module.hot.accept()
            }
            ```
        
		> 另外, 还可以在accept中指定回调函数 -> `太麻烦 -> vue-cli等脚手架自动实现`了
- 方式二(不推荐-太麻烦): 在配置文件webpack.config.js中添加:

    ```conf
    devServer: {
        contentBase: "src",//指定内存中托管的根目录
        port: 3000,
        compress: true, //启用服务器压缩
        open: true, //自动打开浏览器
        hot: true //启动热更新
    },
    ```

	- 但是如此开启hot热更新只是第一步,还需要两步:
	- 第二步: 引入webpack: `const webpack = require("webpack"); //不需要下载,webpack自带`
	- 第三步: 在插件中开启: `plugins: [ new webpack.HotModuleReplacementPlugin() ]`

# browser-sync

## 说明

- Link: https://www.browsersync.io/
- 作用: 可实现及时刷新页面的功能;而且可以实现多个终端,同时调试

## 基本使用

- 安装

    ```
    cnpm install browser-sync -g
    cnpm install browser-sync -D
    ```

- 独立运行:

    ```bash
    browser-sync start --server --files "**/*" 
    # 从当前目录开启一个服务器,并监听所有文件
    --server,-s Run a Local server
    --files, -f File paths to watch
    ```

- 两个端口:
	- 默认的3000端口是调试页面
	- 30001端口是UI配置页面
- 注意:
	- 多终端同步执行,必须声明html5头部

## 配合webpack

1. 配合(`代理`)Webpack Dev Server(`推荐`)
	- 优点: 使用Webpack Dev Server 内存运行和热刷新, 使用 browser-sync 的各终端同步.
	- 缺点: 需要开启两个cmd窗口: 一个开启webpack dev server, 一个用于代理webpack dev server.
	- 原理:use browser-sync proxy the output from the Webpack Dev Server (让 browser-sync `代理 Webpack Dev Server` 的服务器的输出目录 -- `内存中,不是编译后的目录`)
	- 实现: 
		- 首先, 配置 Webpack Dev Server  在3100端口启动 

            ```json
            "scripts": {
                "dev": "webpack-dev-server --open --port 3100 --contentBase src --hot"
            },
            ```

		- 然后, 只需要在命令行运行如下命令即可:

            ```sh
		    browser-sync start --proxy localhost:3100
            ```

		    也可以配置到scripts: -- 还是需要另开一个cmd窗口 -- 两个服务都不能后台 -> 无法使用 `&&` 顺序启动

            ```json
		    "scripts": {
                "sync": "browser-sync start --proxy localhost:3100"
            },
            ```

2. 与Webpack Dev Server并列运行(不推荐),
	- 缺点: 开启webpack dev server服务的同时, 还得编译到硬盘,然后再用browser-sync监视硬盘文件.
	- 原理: 用 webpack命令(watch) - 实时编译项目;  用browser-sync监视编译后的目录
	- 实现: 
		a. 也可以开两个cmd窗口实现;
		b. 使用webpack插件`browser-sync-webpack-plugin`实现;

# html读入内存

> 把磁盘中的html文件也放入内存中

- `npm i html-webpack-plugin -D`
- 引入: `const HtmlWebpackPlugin = require("html-webpack-plugin")`
- 在插件中开启: 

    ```js
    plugins: [
        new HtmlWebpackPlugin({ //创建一个在内存中生成的html页面的插件
            template: path.join(__dirname, './src/index.html'), //根据那个模板生成内存中的html页面
            filename: "index.html", //指定内存生成的html名称
        }),
    ],
    ```

- 当使用了`html-webpack-plugin`插件之后,`./src/index.html`中不再需要手动引用js `<script src="/bundle.js"></script>`, 插件会自动帮我们引用(引用路径也会自动计算)
- 即, 该插件有两个作用: 
	- 自动在内存中根据指定模板页面生成一个内存中的页面;
	- 自动把打包好的bundle.js追加到页面中.
- 另外, 该插件支持更多参数 - 更多见官网

    ```js
    new HtmlWebpackPlugin({//创建一个在内存中生成的html页面的插件
        template: path.join(__dirname, './src/index.html'), //
        filename: "index.html", //指定内存生成的html名称
        title: "xxx培训", //在模板中使用ejs模板语法读取
        hash: true, //add hash to all included scripts and CSS files.
        chunks: ['index']//指定entry中对应的页面-及引入的JS文件
        minify: { //上线前压缩html
            removeAttributeQuotes: true, //去除属性的双引号
            collapseWhitespace: true
        }
    }),
    ```

- 还可以生成多个html文件/页面 - 只需要在插件中再 new 一个对象即可

    ```js
	new HtmlWebpackPlugin({ // 创建另一个html对象->生成一个独立的html文件->多页面(多出口)
	    filename: 'a.html', //生成的html名称, 默认是index.html
	    template: './src/index.html', //如果没有template会自动生成个空的 html
	    //自动把上面生成的js文件引入
	    title: "xxx培训", //在模板中使用ejs模板语法读取
	    hash: true,
	    chunks: ['a']//指定entry中对应的页面-及引入的S文件
	    // ...
	}),
    ```

	这还需要在entry/output中设置对应多页面入/出口:

    ```js
	entry: {
	    //多个页面,
	    index: "./src/js/app.js" //单个入口
	    a:['./src/js/a.js', './src/js/b.js'] //多个入口
	},
	output: {
	    //出口--输出文件
	    // filename: 'bundle.[hash:8].js', //指定输出的文件名
	    filename: "[name].js", //多页面必须使用[name]
	    path: path.resolve(__dirname, "dist/js/") //输出的绝对路径(用resolve解析出来的)
	},
    ```

# css/less/scss

## css样式相关

- 新建css文件`/src/css/index.css`, 输入样式
- 不推荐在`/src/index.html`中引入 -> 又回到了起点 - css引入会发送二次请求过多;
- 在`/src/main.js`中引入: `import './css/index.css'`  -需要css相关loader
	> webpack默认只能打包处理js类型的文件, 非js类型文件都需要对应的loader(加载器)
- `npm i style-loader css-loader -D`
- 在`webpack.config.js`配置文件中新增 module 节点对象 -> rules属性(数组) -> 所有第三方文件的匹配/处理规则:

    ```js
    // css相关loader
    { test: /\.css$/, use: ['style-loader', 'css-loader'] },
    ```

## less文件的处理

- 新建less文件`/src/css/index.less`, 输入样式
- 在/src/main.js中引入: `import './css/index.less'`  -需要less相关loader
- `npm i less-loader -D`
- `npm i less -D`
	> less是less-loader的内部依赖,不需要显式的配置
- 在rules里面追加:

    ```js
    // less相关loader
    { test: /\.less$/, use: ['style-loader', 'css-loader', 'less-loader'] },
    ```

## scss文件的处理

- 新建scss文件`/src/css/index.scss`, 输入样式
- 在/src/main.js中引入: `import './css/index.scss'`  -需要less相关loader
- `npm i sass-loader -D`
- `npm i less -D`
	> sass是less-loader的内部依赖,不需要显式的配置
- npm i node-sass -D
- 在rules里面追加:

    ```js
    // scss相关loader
    { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] },
    ```

# css中的url-图片/字体

## url-loader-图片url

- 默认情况下,`webpack无法处理css文件中的url地址`, 无论是图片,还是字体相关的url

- 在/src/css/index.scss中添加: `background: url('../images/Snipaste_2019-01-06_19-11-04.png')`;会报错

- `npm i url-loader -D ` 
- `npm i file-loader -D` 
	> file-loader是url-loader的内部依赖,不需要显式配置

- 在rules里面追加: 

    ```js
    //处理图片url路径loader
    { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader' }
    ```

- 默认url-loader会把所有的图片都转换为base64编码, 如果需要限制小图片转换,需要添加limit参数,如下:

    ```js
    //处理图片url路径loader
    { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader?limit=174562' }
    //参数单位为字节, < 174562 转换, >= 174562 不转换.
    ```

- url-loader还会把图片的名称用hash自动重命名,如不愿意,可以添加选项

    ```js
    { test: /\.(jpg|png|gif|bmp|jpeg)$/, use: 'url-loader?limit=174562&name=[name].[ext]' }
    ```

	- 但是不建议用原名: 如: 网页引用A, B 两个文件夹中的 两张boy.jpg图片(名称相同,但是内容不同),打包后的文件夹会在一个文件夹,后者会把前者覆盖掉. 两个图片的引用都是后者.
	- 如果是hash构建的名称则不会出现这个问题.

- 如果: 想保持原来的名称又怎么样呢? 如下配置(添加8位hash值): 

    ```js
    use: 'url-loader?limit=174562&name=[hash:8]-[name].[ext]'
    ```

## url-loader-字体url

- `npm i bootstrap@3 -S`
- 网站: https://v3.bootcss.com/components/
- `/src/css/index.html`中添加`<span class="glyphicon glyphicon-search" aria-hidden="true"></span>`
- 同样, 不建议在index.html中引入 bootstrap文件, 在`/src/css/main.js`中引入

    ```js
    // 注意: 如果要通过路径的形式,引用node_modules中的相关文件,可以直接省略'node_modules'
    import 'bootstrap/dist/css/bootstrap.css'
    ```

- bootstrap@3中的字体图标网页中无法显示, 原因也是`bootstrap.css`中url的问题;

    ```js
    //处理字体文件url路径loader
    { test: /\.(svg|eot|ttf|woff|woff2)$/, use: 'url-loader' }
    ```

# 清理dist

`npm install clean-webpack-plugin --save-dev`

```js
const CleanWebpackPlugin = require('clean-webpack-plugin')
plugins: [
    new CleanWebpackPlugin(['dist']),
    ...
]
```

# Source Map

## 背景

开启webpack-dev-server之后,会发现如下问题:
- 控制台中js的出错的位置为打包后的JS文件 -> 无法得知源文件的出错位置;
- css全部显示在style标签中 -> 无法得知源文件的出错位置.

## 使用方式

在`module.exports中添加一项`即可
`devtool: 'cheap-module-eval-source-map',`
- JS调试的话,上面的配置就可以了,
- 如果还要`调试css/less/scss, 还需要在相应的loader中添加选项`:

    ```js
    { test: /\.css$/, use: ['style-loader?sourceMap=true', 'css-loader?sourceMap=true'] }, // css相关
    { test: /\.less$/, use: ['style-loader?sourceMap=true', 'css-loader?sourceMap=true', 'less-loader?sourceMap=true'] },// less相关
    ```

    > 注意: `貌似开启选项 singleton: true (只引用一个style标签)会影响sourceMap功能`

## 模式的选择

- 注意: `开启 Source Map会造成打包后的文件很大`.
- devtool有很多模式, 选择建议如下:
	- 开发环境推荐：cheap-module-eval-source-map
	- 生产环境推荐：cheap-module-source-map （这也是下版本 webpack 使用-d命令启动 debug 模式时的默认选项）
	- 原因如下：
		- `a. 使用 cheap 模式可以大幅提高 souremap 生成的效率。`大部分情况我们调试并不关心列信息，而且就算 sourcemap 没有列，有些浏览器引擎（例如 v8） 也会给出列信息。
		- `b. 使用 eval 方式可大幅提高持续构建效率。`参考官方文档提供的速度对比表格可以看到 eval 模式的编译速度很快。
		- `c. 使用 module 可支持 babel 这种预编译工具`（在 webpack 里做为 loader 使用）。
		- `d. 使用 eval-source-map 模式可以减少网络请求`。这种模式开启 DataUrl 本身包含完整 sourcemap 信息，并不需要像 sourceURL 那样，浏览器需要发送一个完整请求去获取 sourcemap 文件，这会略微提高点效率。而生产环境中则不宜用 eval，这样会让文件变得极大。

# 其他内容

## 代码分割/公共代码

目的:
- 代码分割 -> 按需加载
- 提高加载速度-用户体验好

介绍:
- 官网: https://webpack.js.org/guides/code-splitting/
- 版本4中 使用SplitChunksPlugin 代替 CommonsChunkPlugin 插件
- webpack通过下面三种方式来达到以上目的
	- Entry Points: 多入口分开打包
		- 如果入口 chunks 之间包含重复的模块，那些重复模块都会被引入到各个 bundle 中。
		- 这种方法不够灵活，并且不能将核心应用程序逻辑进行动态拆分代码。
	- Prevent Duplication:去重，抽离公共模块和第三方库
	- Dynamic Imports:动态加载


## 懒加载

优点:
- 不需要一次性下载N多代码;
- 瞬间加载需要的代码 - 提升用户体验;

实现:
- 方式一: webpack Methods内置的方式;
	- require.ensure https://webpack.js.org/api/module-methods/#require-ensure
	- require.include https://webpack.js.org/api/module-methods/#require-include
- 方式二:ES2015 Loader spec
	- 动态inport() -> 返回 Promise对象 ->import().then

## CSS提取/前缀/压缩

说明:
- webpack的作用之一便是: 减少二次请求 -- 这提取了css有增加了二次请求
- `可以在项目的js文件中引入css文件(感觉有点怪)`; --> 还是gulp流程清楚
- `然后用webpack把js文件中的css代码渲染到页面中(没有单独的css文件) -> 内部样式`.
- 通过loader编译less/sass;
- 提取CSS代码 ->`把js中的css再提取成单独的 css文件 -- 何必呢`?

需要的npm包:
- `ExtractTextWebpackPlugin`
- `postcss-loader autoprefixer`
- `purify-css glob`

## 静态资源的拷贝

copy-webpack-plugin

## TreeShaking

说明:
- TreeShaking表面意思 - 摇树 -> 把多余的代码去掉;
- 使用场景:
	- 常规优化 - 日常优化项目
	- 只引入第三方库的一个功能 - 却需要引入整个库

JS Tree Shaking:
- 使用的库/及代码中很多对象/方法都是没有用到的(如Jquery里面的很多对象/方法) -> 不应该被用户下载 -> 去除
- 使用工具: `Webpack.optimize.uglifyJS插件 -> GULP 也可以`
- 官网: https://github.com/mishoo/UglifyJS

CSS Tree Shaking:
- 有些css样式在DOM中没有响应类/ID, -> 废弃的CSS样式 ->不应该被用户下载  -> 去除
- 使用的工具: `Purify CSS  -> GULP 也可以`
- 官网: https://github.com/purifycss/purifycss

## 图片处理

CSS中引入图片:
- 如何在Webpack中引入图片并处理?
- 实现: file-loader

自动合成雪碧图:
- 多张图片合成一张 -> 减少大小/http请求
- 实现: postcss-sprites

图片压缩:
- 图片再压缩一下
- 实现:img-loader

Base64编码:
- 如果图片太小不需要压缩,可以使用Base64编码
- 实现:url-loader

retina处理: ...

## 处理文字

CSS中引入字体:
- 如何在Webpack中引入图片并处理?
- 实现: file-loader

Base64编码:
- 使用Base64编码减少体积
- 实现:url-loader

## 第三方JS库(CDN)

场景:
- 第三方JS库在CDN上
- 第三方JS库在本地项目中

处理:
- wepack.providePlugin
- imports-loader

## 分析打包结果

## 优化打包速度

## 长缓存优化

- 给代码填上版本号,并告诉浏览器进行相应的缓存,用户访问时优先从本地获取;
- 如果版本号更改,在重新请求服务器;


# Gulp

## 概述

- gulp(狼吞虎咽)、grunt不涉及CMD模块的编译，它们不是构建的工具，就是工作流工具,监听/控制工作流程,解放琐碎的工作。
    > gulp is a toolkit for automating painful or time-consuming tasks in your development workflow, so you can stop messing around and build something.

- 官网：http://gulpjs.com/

- gulp本身只是个空壳,需要`[各种插件]`来实现各种功能.

- 插件网址:
    - 建议:(有排名) https://www.npmjs.com/
    - 不建议:(最终还是链接到npm官网) https://gulpjs.com/plugins/

- 准备工作: Tips: `使用 -S 和 -D 代替 --save 和 --save-dev`。

    ```js
    // 1. 全局安装 gulp： 方便全局使用gulp命令
    npm install --global gulp

    // 2. 安装开发依赖（devDependencies）：项目中需要依赖这个包
    npm install --save-dev gulp

    gulp -v
    gulp --tasks, -T  打印任务(依赖图)

    // 3. 在项目根目录下创建一个名为 gulpfile.js 的文件：
    touch gulpfile.js

    // 4.写入如下内容
    var gulp = require('gulp');
    gulp.task('default', function() {
        // 将你的默认的任务代码放在这
    });
    ```

## browser-sync

- 说明:
    - Link: https://www.browsersync.io/
    - 作用: 可实现及时刷新页面的功能;而且可以实现多个终端,同时调试

- 基本使用:
    - 安装
        `npm install browser-sync -g`
    - 独立运行:

        ```
        browser-sync start --server --files **/* 
        //从当前目录开启一个服务器,并监听所有文件
        --server,-s Run a Local server
        --proxy, -p F代理其他服务器,不能和--server同用
        --files, -f File paths to watch
        ```
    - 两个端口:
        - 默认的3000端口是调试页面
        - 30001端口是UI配置页面
    > 注意: 多终端同步执行,必须声明html5头部

- 配合gulp:

    ```js
    // 静态服务器
    function server(done) {
        browserSync.init({
            server: { baseDir: './dist' }
        });
        done();
    }

    //或者代理Nginx的服务器
    function server(done) {
        browserSync.init({
            server: {
                proxy: "yourlocal.dev" 
                //或者 127.0.0.1
                //可以把Nginx中部署的站点代理过来
                //通过browserSync更能更好的调试80端口
            }
        });
        done();
    }
    ```
## 配置sample

见百度网盘: `全部文件>others>编程-源文件>gulpfile.js`

## 常用插件

搜索技巧:
- https://www.npmjs.com/ 搜索 "gulp-" 按照Optimal/popularity...等排名
- https://gulpjs.com/plugins/ 官网的没有排名的选项... ^_^

browser-sync:
- 开启服务器.
- 具体见上一节

webpack-stream:
- 作用: 在gulp中操作Webpack. Run webpack as a stream to conveniently integrate with gulp.
- Links: https://www.npmjs.com/package/webpack-stream
- 推荐指数：★★★★★

del:
- 作用: 删除文件/文件夹
- Links: https://www.npmjs.com/package/del
- 推荐指数：★★★★★

gulp-rename:
- 作用: 重命名文件
- Links: https://www.npmjs.com/package/gulp-rename
- 推荐指数：★★★★★

gulp-if:
- 作用: 在pipe流中添加if判断
- Links: https://www.npmjs.com/package/gulp-if
- 推荐指数：★★★★★

gulp-concat:
- 作用: 把多个js文件合并成一个
- Links: https://www.npmjs.com/package/gulp-concat
- 推荐指数：★★★★★

gulp-uglify:
- 作用: 上线之前压缩JS文件
- Links: https://www.npmjs.com/package/gulp-uglify
- 推荐指数：★★★★★

gulp-sourcemaps:
- 作用: 处理JS时，生成SourceMap
- Links: https://www.npmjs.com/package/gulp-sourcemaps
- 推荐指数：★★★★

gulp-less:
- 作用: 将less文件编译成css
- Links: https://www.npmjs.com/package/gulp-less
- 推荐指数：★★★★★

gulp-autoprefixer:
- 作用: 使用Autoprefixer来补全`浏览器兼容的css`。
- Links: https://www.npmjs.com/package/gulp-autoprefixer
- 推荐指数：★★★★★

gulp-concat-css:
- 作用: 合并css。
- Links: https://www.npmjs.com/package/gulp-concat-css
- 推荐指数：★★★★★

gulp-csso:
- 作用: 上线之前压缩JS文件--自动合并属性
- Links: https://www.npmjs.com/package/gulp-csso
- 推荐指数：★★★★★
- 还有类似的插件: gulp-csso...

gulp-css-base64:
- 作用: converts all data found within a stylesheet (those within a url( ... ) declaration) into base64-encoded data URI strings. This includes images and fonts.
- Links: https://www.npmjs.com/package/gulp-css-base64
- 推荐指数：★★★★★

gulp-htmlmin:
- 作用: 压缩html(去除空格...)
- Links: https://www.npmjs.com/package/gulp-htmlmin
- 推荐指数：★★★★★

gulp-imagemin:
- 作用: 压缩图片
- Links: https://www.npmjs.com/package/gulp-imagemin
- 推荐指数：★★★★★

gulp-cached:
- 作用: keeps an in-memory cache of files. This means you only process what you need and save time + resources.
- Links: https://www.npmjs.com/package/gulp-cached
- 推荐指数：★★★★★

gulp-rev:
- 作用: 静态文件名->hash文件名 Static asset revisioning by appending content hash to filenames unicorn.css → unicorn-d41d8cd98f.css
- Links: https://www.npmjs.com/package/gulp-rev
- 推荐指数：★★★★★
- 扩展: 这个过程叫做 revision(修正/修改)。如果你有一个名字是 main.js 的脚本，且有 cache 头，浏览器就会对他进行缓存，下次再访问时文件如果尚在缓存期内就直接读取缓存，而非再次从网络加载，提升页面的访问速度。文件修改后,hash值会更改,便会再次从网络加载.

gulp-rev-collector:
- 作用: 上面的rev工具修改名称后,通过这个工具把html中引用的css/js文件地址对应修改
- Links: https://www.npmjs.com/package/gulp-rev-collector
- 推荐指数：★★★★★

gulp-filter:
- 作用: Enables you to work on a subset of the original files by filtering them using glob patterns. When you're done and want all the original files back you just use the restore stream.
- Links: https://www.npmjs.com/package/gulp-filter
- 推荐指数：★★★★★

