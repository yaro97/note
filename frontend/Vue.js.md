# 概述

## 什么是vue

- Vue.js 是目前最火的一个前端框架，React是最流行的一个前端框架（React除了开发网站，还可以开发手机App， Vue语法也是可以用于进行手机App开发的，需要借助于Weex）
- Vue.js 是前端的`主流框架之一`，和Angular.js、React.js 一起，并成为前端三大主流框架！
- Vue.js 是一套构建用户界面的框架，`只关注视图层`，它不仅易于上手，还便于与第三方库或既有项目整合。（Vue有配套的第三方类库，可以整合起来做大型项目的开发）
- 前端的主要工作？主要负责MVC中的V这一层；主要工作就是和界面打交道，来制作前端页面效果；

## 为什么学习框架

- 企业为了提高开发效率：在企业中，时间就是效率，效率就是金钱；
	> 企业中，使用框架，能够提高开发的效率；
- 提高开发效率的发展历程：原生JS -> Jquery之类的类库 -> 前端模板引擎 -> Angular.js / Vue.js（能够帮助我们减少不必要的DOM操作；提高渲染效率；双向数据绑定的概念【通过框架提供的指令，我们前端程序员只需要关心数据的业务逻辑，不再关心DOM是如何渲染的了】）
- 在Vue中，一个核心的概念，就是让用户不再操作DOM元素，解放了用户的双手，让程序员可以更多的时间去关注业务逻辑；
- 增强自己就业时候的竞争力
	- 人无我有，人有我优
	- 你平时不忙的时候，都在干嘛？

## 框架 VS 库

- 框架：是一套完整的解决方案；对项目的侵入性较大，项目如果需要更换框架，则需要重新架构整个项目。
	> node 中的 express - 项目启动后 不易切换
- 库（插件）：提供某一个小功能，对项目的侵入性较小，如果某个库无法完成某些需求，可以很容易切换到其它库实现需求。
	1. 从Jquery 切换到 Zepto
	2. 从 EJS 切换到 art-template

## MVC和MVVM区别

- MVC 是后端的分层开发概念；
- MVVM是前端视图层的概念，主要关注于 视图层分离，也就是说：MVVM把前端的视图层，分为了 三部分 Model, View , VM ViewModel
- 为什么有了MVC还要有MVVM
![](http://ww1.sinaimg.cn/large/48356ef5ly1fzq35gjql9j211d0f1jt6.jpg)

# v-cloak/text/html/bind/on

- {{}} 插值表达式可以在标签的内部部分插入vue的数据;
- v-cloak可以解决 {{}} 的闪烁问题(网络不好会加载 {{}} )

    ```js
    [v-cloak] {
        display: none;
    }
    <p v-cloak>{{msg}}</p>
    ```
- v-text 会把标签内所有的内容替换为vue的数据, 没有闪烁的问题
- v-html 会把vue的数据解析为html代码
- v-bind 绑定属性
- v-on 绑定事件

- 跑马灯案例

    ```js
    <div id="app">
        <input type="button" value="浪起来" @click="lang">
        <input type="button" value="低调" @click="didiao">
        <h4>{{msg}}</h4>
    </div>
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                msg: '猥琐发育,别浪~~!',
                intervalID: null
            },
            methods: {
                lang() {
                    if (!this.intervalID) {
                        console.log(this.msg);
                        this.intervalID = setInterval(() => {
                            this.msg = this.msg.substring(1) + this.msg[0]
                        }, 200)
                    }
                },
                didiao() {
                    clearInterval(this.intervalID) //只是清理定时器,并没有改变intervalID的值
                    this.intervalID = null
                }
            },
        })
    </script>
    ```

# 事件修饰符

- .stop 阻止冒泡 -- 点击inner不会触发outer(默认是先触发inner再触发outer)
- .prevent 阻止默认事件 -- 阻止a链接的跳转
- .capture 添加事件侦听器时使用事件捕获模式  
    - 给outer添加修饰符, 点击inner,先触发outer,再触发inner; 
    - 如果是三层(1,2,3)-1是最里层, 绑定到3的话,点击1,会以次触发3,2,1, 点击2的话,会以次触发3,2
    - 如果是三层(1,2,3)-绑定到2的话,点击1,会以次触发1,3,2
- .self 只有该元素本身才能触发;
    - 但是`不会阻碍事件的冒泡/捕获`, 如: 三层(1,2,3),`2层添加self修饰符,2只能由自身触发,但还是会传播1和3之间的事件`.
- .once 自身只能触发一次, 
    - 但是:,还是会产生事件, 如:  三层(1,2,3), 1上面绑定了once,`多次点击1后, 2,3还是会受1的影响`.
    - 而且`1上面的所有事件都只能触发一次`,如: @click.prevent.once(与事件的书写顺序无关), 点击之后,prevent也失效了;
- 事件修饰符可以链式编程, 如: @click.stop.once.self

    ```html
    <div id="app">
        <div @click.capture="largerHandler">
            <div class="inner" @click.self="divHandler">
                <input type="button" value="戳它" @click.once="btnHandler">
            </div>
        </div>
        <a href="http://www.baidu.com" @click.prevent.once="aHandler">百度</a>
    </div>
    ```


# v-model(双向绑定)

- 之前的绑定都是单向的: model -> view
- 而v-model是双向的: model <-> view
- view中能输出数据的都是表单元素;
- 注意: v-model 后面不需要冒号:value 

```html
<input type="text" v-model="msg">
```
- 简单计算器

```html
<div id="app">
    <input type="text" v-model="n1">
    <select name="" id="" v-model="opt">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
    </select>
    <input type="text" v-model="n2">
    <input type="button" value="=" @click="calc">
    <input type="text" v-model="ret">
</div>
<script>
var vm = new Vue({
    el: '#app',
    data: {
        n1: 0,
        n2: 0,
        opt: '+',
        ret: 0
    },
    methods: {
        calc() {
            // this.ret = eval(this.n1 + this.opt + this.n2) //歪门邪道
            switch (this.opt) {
                case '+':
                    this.ret = parseFloat(this.n1) + parseFloat(this.n2)
                    break;
                case '-':
                    this.ret = parseFloat(this.n1) - parseFloat(this.n2)
                    break;
                case '*':
                    this.ret = parseFloat(this.n1) * parseFloat(this.n2)
                    break;
                case '/':
                    this.ret = parseFloat(this.n1) / parseFloat(this.n2)
                    break;
            }
        }
    }
})
</script>
```

# 使用样式

## 使用class

```html
<div id="app">
    <!-- 原始的html方式 -->
    <h1 class="red thin">这是一个很大的h1,很大很大</h1>
    <!-- 使用数组 -->
    <h1 :class="['red', 'thin']">这是一个很大的h1,很大很大</h1>
    <!-- 数组中使用三元表达式 -->
    <h1 :class="['red', flag?'active':'']">这是一个很大的h1,很大很大</h1>
    <!-- 数组中使用对象 -->
    <h1 :class="['red', {active: flag}]">这是一个很大的h1,很大很大</h1>
    <!-- 使用对象 -->
    <h1 :class="{italic: true, active: flag}">这是一个很大的h1,很大很大</h1>
</div>
```

- 有上面四种方式:
- **注意**: 
	- JS中对象的属性可以使用引号,也可以不使用;
	- 但是如果属性中含有 短横线(-) 必须使用引号

## 内联样式

也可以通过行内样式定义样式

```html
<div id="app">
    <!-- 直接在元素上通过 :style 的形式，书写样式对象 -->
    <h1 :style="{color: 'red', 'font-size': '40px'}">这是一个善良的H1</h1>
    <!-- 也可以把对象定义在 data中,直接引用,-->
    <h1 :style="h1StyleObj">这是一个善良的H1</h1>
    <!-- 引用多个,用数组即可 -->
    <h1 :style="[h1StyleObj, h1StyleObj2]">这是一个善良的H1</h1>
</div>
```

# v-for和key属性

v-for可以迭代数组/对象/数字

```html
<!-- 遍历数组 -->
<li v-for="(item, index) in list" :key="index">{{index}}-{{item.}}</li>
<!-- 遍历对象 -- index基本不用 -->
<div v-for="(val, key, index) in users" :key="index">{{val}}-{{key}}-{{index}}</div>
<!-- 遍历数字 从1 - 10 -->
<p v-for="i in 10">这是第 {{i}} 个P标签</p>
```

- 注意: 2.2.0+ 的版本里，当在组件中使用 v-for 时，`:key 是必须而且唯一`的。而且`:key的值可以是number/string`, 不能是其他类型.
- 原因: 当 Vue.js 用 v-for 正在更新已渲染过的元素列表时，它默认用 “就地复用” 策略。如果数据项的顺序被改变，Vue将不是移动 DOM 元素来匹配数据项的顺序， 而是简单复用此处每个元素，并且确保它在特定索引下显示已被渲染过的每个元素。为了给 Vue 一个提示，以便它能跟踪每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一 key 属性。

# v-if/v-show

1. 二者都是控制标签的显示和隐藏.
2. v-if是dom节点的删除增加, -> 切换性能消耗高 -> 适合运行时条件不大可能改变(如: 元素永远不被用户看到)
3. v-show是通过display:none实现的 -> 初始渲染消耗高 -> 适合频繁切换

```html
<h3 v-if="flag">这是v-if控制的</h3>
<h3 v-show="flag">这是v-show控制的</h3>
```

# 过滤器

## 概述

过滤器可以用在两个地方：双花括号插值和 v-bind 表达式 (后者从 2.1.0+ 开始支持)。过滤器应该被添加在 JavaScript 表达式的尾部，由“管道”符号指示：

```html
<!-- 在双花括号中 -->
{ { message | capitalize } }
<!-- 在 `v-bind` 中 -->
<div v - bind: id="rawId | formatId">< /div> 
```

## 私有过滤器

可以在一个组件的选项中定义`本地过滤器`--filters

```js
filters: {
    capitalize: function(value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
    }
}
```

## 全局过滤器

也可以定义`全局过滤器`, 但是`全局过滤器必须先定义后引用--定义在Vue实例前面` -- filter

```js
Vue.filter('dateFormat', function(dateStr) {
    let dt = new Date(dateStr)
    let y = dt.getFullYear()
    let m = dt.getMonth()
    let d = dt.getDate()
    return `${y}-${m}-${d}`
})
```

## 注意事项

- 过滤器可以接受多个参数,`第一个参数为过滤器(|)前面的data,后面的参数为自定义`,数量不限

    ```js
    {{ message | filterA('arg1', arg2) }}
    ```

    > 这里，`filterA` 被定义为接收三个参数的过滤器函数。其中 `message` 的值作为第一个参数，普通字符串 `arg1` 作为第二个参数，表达式 `arg2` 的值作为第三个参数。

- 如果私有过滤器和全局过滤器同名, 优先调用私有过滤器
- 过滤器可以串联

    ```js
    {{ message | filterA | filterB }}
    ```

# 按键修饰符

基本使用:
- [官网](https://cn.vuejs.org/v2/guide/events.html#%E6%8C%89%E9%94%AE%E4%BF%AE%E9%A5%B0%E7%AC%A6): 
- 可以捕获按键操作

    ```html
    <input v-on:keyup.13="submit">
    <!-- 记住所有的 keyCode 比较困难，所以 Vue 为最常用的按键提供了别名： -->
    <input @keyup.enter="submit">
    ```

Vue内置的按键别名:
- .enter
- .tab
- .delete (捕获“删除”和“退格”键)
- .esc
- .space
- .up
- .down
- .left
- .right

也可自定义其他按键的别名:

```js
// 可以使用 `v-on:keyup.f1`
Vue.config.keyCodes.f1 = 112
```

# 自定义指令

> 说明: 除了核心功能默认内置的指令 (v-model 和 v-show)，Vue 也允许注册自定义指令。

全局/局部自定义指令:

```js
// 注册一个全局自定义指令 `v-focus`
Vue.directive('focus', {
    // 当被绑定的元素插入到 DOM 中时……
    inserted: function(el) {
        // 聚焦元素
        el.focus()
    }
})
//局部自定义指令
directives: {
    color: {
        // 指令的定义
        inserted: function(el) {
            el.tyle.color = 'red'
        }
    }
}
```

> 同过滤器, 全局指令也必须写在Vue实例的前面;
> 定义时不需要前缀 v- ,使用时需要;
> 上面的定义指令在使用时不用指定绑定的值

```html
<input type="text" id="txt" v-focus v-color">
```

钩子函数:
- 一个指令定义对象可以提供如下几个钩子函数 (均为可选)：
- `bind是在内存`中操作, 然后 `insert 到DOM`中, 然后`在DOM中update`.
	- `bind：`(`常用于CSS样式相关的操作`)只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置。
	- `inserted：`(`常用于JS行为相关的操作`)被绑定元素插入父节点时调用 (仅保证父节点存在，但不一定已被插入文档中)。
	- `update`：所在组件的 VNode 更新时调用，但是可能发生在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 (详细的钩子函数参数见下)。
	- 还有 componentUpdated 和 unbind --用的较少

钩子函数参数:
- 钩子函数会传入以下参数: 
	- el - 绑定的元素 - 除了这个参数,1
	- binding - 一个1:
		- name - 指令名-不含 v- 前缀
		- value  - 1,例如：`v-my-directive="1 + 1"` 中，绑定值为 2。
		- expression' - 指令绑定的值(字符串),例如 `v-my-directive="1 + 1"`中，表达式为 "1 + 1"。
		- arg - `传给指令的参数`,可选。例如 `v-my-directive:foo` 中，参数为 "foo"。
		- 还有modifiers oldValue 等,见[官网](https://cn.vuejs.org/v2/guide/custom-directive.html)
	- vnode 和 oldVnode,见[官网](https://cn.vuejs.org/v2/guide/custom-directive.html)

        ```js
        <input type="text"v-color="['blue', 800, '30px']">
        Vue.directive('style', function(el, binding) {
            el.style.color = binding.value[0]
            el.style.fontWeight = binding.value[1]
            el.style.fontSize = binding.value[2]
        })
        ```

        > 指令可以绑定任意合法的JS表达式 - 上面绑定了一个数组

钩子函数的简写:
- 在很多时候，你可能想在 bind 和 update 时触发相同行为(同时定义这两个钩子函数)，而不关心其它的钩子。可以这样写:

    ```js
    Vue.directive('color-swatch', function(el, binding) {
        el.style.backgroundColor = binding.value
    })
    ```

# 生命周期

生命周期过程:
- new Vue()
- 初始化事件/生命周期
- beforeCreate()
- 初始化data/methods
- created()
- 在内存中渲染模板
- beforeMount()
- 把内存中的模板挂载到页面
- mounted()
- beforeUpdate() <- 内存中的数据改变
- 内存中虚拟DOM重新渲染, patch页面
- updated() -- 页面更新后
- beforeDestroy <- 调用vm.$destroy()
- 卸载watchers/子组件/事件监听器..
- destroyed()  -- vm实例销毁后

概述:
- 什么是生命周期：从Vue实例创建、运行、到销毁期间，总是伴随着各种各样的事件，这些事件，统称为生命周期！
- 生命周期钩子：就是生命周期事件的别名而已；
- 生命周期钩子 = 生命周期函数 = 生命周期事件
- 主要的生命周期函数分类：
	- 创建期间的生命周期函数：
		- beforeCreate：实例刚在内存中被创建出来，此时，还没有初始化好 data 和 methods 属性
		- created：实例已经在内存中创建OK，此时 data 和 methods 已经创建OK，此时还没有开始 编译模板
		- beforeMount：此时已经完成了模板的编译，但是还没有挂载到页面中
		- mounted：此时，已经将编译好的模板，挂载到了页面指定的容器中显示
	- 运行期间的生命周期函数：
		- beforeUpdate：状态更新之前执行此函数， 此时 data 中的状态值是最新的，但是界面上显示的 数据还是旧的，因为此时还没有开始重新渲染DOM节点
		- updated：实例更新完毕之后调用此函数，此时 data 中的状态值 和 界面上显示的数据，都已经完成了更新，界面已经被重新渲染好了！
	- 销毁期间的生命周期函数：
		- beforeDestroy：实例销毁之前调用。在这一步，实例仍然完全可用。
		- destroyed：Vue 实例销毁后调用。调用后，Vue 实例指示的所有东西都会解绑定，所有的事件监听器会被移除，所有的子实例也会被销毁。

> 说明: 比如: 如果在methods中定义了请求Ajax的函数, 应该在created 钩子中调用该方法 -- 尽早;

# get/post/jsonp

背景: 之前使用jquery实现三种请求, 但是vue不推荐操作DOM, 所以jQuery就...

实现:
- Vue可以通过 [vue-resource](https://github.com/pagekit/vue-resource) 第三方插件实现 -- `依赖 vue,引用时注意在vue后面引用`. 
- 还可以使用 [axios](https://github.com/axios/axios) (貌似不支持jsonp,需要另外一个jsonp插件)
-  vue-resource 发送post请求是通过如下选项[模拟表格的post请求](https://github.com/pagekit/vue-resource/blob/develop/docs/http.md#config)(有些post请求限制只能表格发起):
    ```
    emulateJSON | boolean | Send request body as application/x-www-form-urlencoded content type
    ```
- vue-resource的[configuration](https://github.com/pagekit/vue-resource/blob/develop/docs/config.md#configuration)中还可以定义请求网址的根路径, 上面的模拟表格的post请求也可以通过[configuration](https://github.com/pagekit/vue-resource/blob/develop/docs/config.md#configuration)实现.

# 动画

## 概述

- Vue 在`插入、更新或者移除 DOM 时，提供多种不同方式的应用过渡效果`。包括以下工具：
	- 在 CSS 过渡和动画中自动应用 class
	- 可以配合使用第三方 CSS 动画库，如 Animate.css
	- 在过渡钩子函数中使用 JavaScript 直接操作 DOM
	- 可以配合使用第三方 JavaScript 动画库，如 Velocity.js
- 注意区分 过渡`transition`  /  动画`animation` 

## 单元素/组件的过渡

1. 基本实现(css内置的transition/animation): 
	- 首先需要目标元素设置 条件渲染 (使用 v-if) 或 条件展示 (使用 v-show); -- 元素需要先有 进入/离开 行为.
	- 然后需要把目标元素用 `<transition name="fade">...</transition>` 包裹;
	- 再次需要在style标签内设置.fade-enter-active, .fade-leave-active 的transition 和.fade-enter, .fade-leave-to 对应的样式.

    ```html
    <style>
        .v-enter, .v-leave-to {
            opacity: 0;
            transform: translateX(100px)
        }
        .v-enter-active, .v-leave-active {
            transition: all .4s ease;
        }
    </style>
    ===============
    <div id="app">
        <input type="button" value="toggle" @click="flag=!flag">
        <transition>
            <h3 v-if="flag">这是一个H3</h3>
        </transition>
    </div>
    ===============
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                flag: false,
            },
        })
    </script>
    ```

    > `<transition>`中name属性值需要和style中类名前缀对应,默认是 `v-`

- 过渡的类名
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzq41ck7xsj20xc0got9a.jpg)

- css过渡
	- 常用的过渡都是使用 CSS 过渡。如:

        ```css
        /* 可以设置不同的进入和离开动画 */
        /* 设置持续时间和动画函数 */
        .slide-fade-enter-active {
            transition: all .3s ease;
        }
        .slide-fade-leave-active {
            transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
        }
        .slide-fade-enter, .slide-fade-leave-to {
        /* .slide-fade-leave-active for below version 2.1.8 */
            transform: translateX(10px);
            opacity: 0;
        }
        ```
	
- css动画
	- CSS 动画用法同 CSS 过渡，区别是在动画中 v-enter 类名在节点插入 DOM 后不会立即删除，而是在 animationend 事件触发时删除。如:
        ```css
        .bounce-enter-active {
            animation: bounce-in .5s;
        }
        .bounce-leave-active {
            animation: bounce-in .5s reverse;
        }
        @keyframes bounce-in {
            0% {
                transform: scale(0);
            }
            50% {
                transform: scale(1.5);
            }
            100% {
                transform: scale(1);
            }
        }
        ```
	
2. 自定义过渡的类名 -- 第三方 CSS 动画库，如 Animate.css 结合
	- 需要引入 Animate.css(CSS transition实现) 第三方库不在需要定义 style 标签中的样式, 
	- 只需要简单的定义 enter-active-class  leave-active-class ..即可实现复杂的css transition动画.如:

        ```html
        <link href="https://cdn.jsdelivr.net/npm/animate.css@3.5.1" rel="stylesheet" type="text/css">
        
        <div id="example-3">
            <button @click="show = !show">
                Toggle render
            </button>
            <transition
                name="custom-classes-transition"  //如果不需要额外在style标签中定义样式,可以省略,
                enter-active-class="animated tada"
                leave-active-class="animated bounceOutRight"
            >
                <p v-if="show">hello</p>
            </transition>
        </div>
        ```

- 显性声明过渡持续时间
	- 通常,vue自动得出过渡完成的时机/持续时间;
	- 也可以用 <transition> 组件上的 duration 属性定制一个显性的过渡持续时间 (以毫秒计)

        ```html
        <transition :duration="1000">...</transition>
        // 你也可以定制进入和移出的持续时间：
        <transition :duration="{ enter: 500, leave: 800 }">...</transition>
        ```
        
3. 使用钩子函数 -- 半场动画
	- 可以动过钩子函数更细节的控制动画;
	- 钩子函数中的逻辑可以很自由,也可以调用第三方动画库,如Velocity.js (通过定时器实现动画);
	- 如下一个案例 - 小球半场动画: 

        ```html
        <style>
            .ball {
                height: 20px;
                width: 20px;
                background-color: red;
                border-radius: 50%
            }
        </style>
        ===========
        <div id="app">
            <input type="button" value="快到碗里来" @click="flag=!flag">
            <transition
                @before-enter="beforeEnter"
                @enter="enter"
                @after-enter="afterEnter">
                <div class="ball" v-show="flag"></div>
            </transition>
        </div>
        ==========
        <script>
            var vm = new Vue({
                el: '#app',
                data: {
                    flag: true,
                },
                methods: {
                    // el 是要执行动画的那个DOM对象
                    beforeEnter(el) { // 动画进入之前的回调
                        el.style.transform = 'translate(0, 0)'
                    },
                    enter(el, done) { // 动画进入完成时候的回调
                        el.offsetWidth //虽然这句话没意义, 但是不写的话,出不来动画
                        // 可以理解为el.offsetWidth 会强制动画刷新
                        // 其他的offset系列也可: top/left...
                        el.style.transform = 'translate(150px, 450px)'
                        el.style.transition = 'all 1s ease'
                        done(); 
                        //这里的done,就是afterEnter函数的引用
                        //在enter/leave钩子函数中必须传入done,且调用, 否则会有小问题
                    },
                    afterEnter(el) { // 动画进入完成之后的回调
                        this.flag = !this.flag;
                    }
                }
            })
        </script>
        ```

	    > - 上述代码中的this.flag = !this.flag;有两个作用: 1. 控制小球的显示/隐藏, 2. 直接跳过后半场动画, 让flag直接变成false, 再次点击按钮的时候,flag的值才是false到true,如此往复,一直执行前半场动画;
	    > - Vue通过钩子函数把一个完成的动画拆分为两部分, 如果不把flag取反, 后面的动画(虽然没有效果)依然会执行.

## 多元素/组件的过渡

## 列表过渡

- 前面的过渡都是关于
	- 单个节点
	- 同一时间渲染多个节点中的一个
- 那么,如何同时渲染整个列表呢? 比如使用 `v-for` ？在这种场景中，使用 `<transition-group> `组件。这个组件有如下特性: 
	- 不同于 <transition>，它会以一个真实元素呈现：默认为一个 `<span>`。你也可以通过 tag 特性更换为其他元素。
	- [过渡模式](https://cn.vuejs.org/v2/guide/transitions.html#%E8%BF%87%E6%B8%A1%E6%A8%A1%E5%BC%8F)不可用，因为我们不再相互切换特有的元素。
	- 内部元素 总是需要 提供唯一的 `key` 属性值。
1. 列表的进入/离开
	- 现在让我们由一个简单的例子深入，进入和离开的过渡使用之前一样的 CSS 类名。

        ```html
        <head>
            <script src="./node_modules/vue/dist/vue.js"></script>
            <style>
                .list-item {
                    display: inline-block;
                    margin-right: 10px;
                }
                .list-enter-active,
                .list-leave-active {
                    transition: all 1s;
                }
                .list-enter,
                .list-leave-to
                /* .list-leave-active for below version 2.1.8 */
                    {
                    opacity: 0;
                    transform: translateY(30px);
                }
            </style>
        </head>
        <body>
            <div id="list-demo" class="demo">
                <button @click="add">Add</button>
                <button @click="remove">Remove</button>
                <transition-group name="list" tag="p">
                    <!-- 生成的所有的span标签被p标签包裹 -->
                    <span v-for="item in items" v-bind:key="item" class="list-item">
                        {{ item }}
                    </span>
                </transition-group>
            </div>
            <script>
                new Vue({
                    el: '#list-demo',
                    data: {
                        items: [1, 2, 3, 4, 5, 6, 7, 8, 9],
                        nextNum: 10
                    },
                    methods: {
                        randomIndex: function() {
                            return Math.floor(Math.random() * this.items.length)
                        },
                        add: function() {
                            this.items.splice(this.randomIndex(), 0, this.nextNum++)
                        },
                        remove: function() {
                            this.items.splice(this.randomIndex(), 1)
                        },
                    }
                })
            </script>
        </body>
        ```

	- 只需要在设置appear `<transition appear><!-- ... --></transition>` 便可以实现目标第一次出现时便有动画,详情见官网: [初始渲染的过渡](https://cn.vuejs.org/v2/guide/transitions.html#%E5%88%9D%E5%A7%8B%E6%B8%B2%E6%9F%93%E7%9A%84%E8%BF%87%E6%B8%A1).

2. 列表的排序过渡
	- `<transition-group>` 组件还有一个特殊之处。不仅可以进入和离开动画，还可以改变定位。要使用这个新功能只需了解新增的 `v-move` 特性，它会在元素的改变定位的过程中应用。像之前的类名一样，可以通过 `name` 属性来自定义前缀，也可以通过 `move-class` 属性手动设置。

        ```html
        <style>
            /* v-move 和 v-leave-active 结合使用，能够让列表的过渡更加平缓柔和： */
            .v-move {
                transition: all 0.8s ease;
            }
            .v-leave-active {
                position: absolute;
            }
        </style>
        ```

	- `v-move` 对于设置过渡的切换时机和过渡曲线非常有用，你会看到如下的例子：

        ```html
        <head>
            <script src="./node_modules/vue/dist/vue.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.14.1/lodash.min.js"></script>
            <style>
                .flip-list-move {
                    transition: transform 1s;
                }
            </style>
        </head>
        <body>
            <div id="flip-list-demo">
                <button @click="shuffle">Shuffle</button>
                <transition-group name="flip-list" tag="ul">
                    <!-- name 属性决定style中的前缀 -->
                    <li v-for="item in items" :key="item">
                        {{ item }}
                    </li>
                </transition-group>
            </div>
            <script>
                new Vue({
                    el: '#flip-list-demo',
                    data: {
                        items: [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    },
                    methods: {
                        shuffle: function() {
                            this.items = _.shuffle(this.items)
                        }
                    }
                })
            </script>
        </body>
        ```

# 组件

## 概述

组件的目的: 组件的出现，就是为了拆分Vue实例的代码量的，能够让我们以不同的组件，来划分不同的功能模块，将来我们需要什么样的功能，就可以去调用对应的组件即可；
- 模块化(Node)： 是从代码逻辑的角度进行划分的；方便代码分层开发，保证每个功能模块的职能单一；
- 组件化(Vue)： 是从UI界面的角度进行划分的；前端的组件化，方便UI组件的重用；

## 创建组件的方式-全局

Vue创建全局组件使用 Vue.component 方法, 组件中模板的定义有三种方式:
- 方式一: 使用 Vue.extend方法：
- 注意: `tempale中的html只能有一个root标签, 不能放两个同级的标签.`

```html
<div id="app">
        <my-com-a></my-com-a>
    <!-- 标签不能使用大写字母, 驼峰命名需要用短横线替换 -->
</div>
<script>
    // 1. 创建组件模板对象
    var com1 = Vue.extend({
        template: '<h3>这是使用extend创建的组件</h3>'
    })
    // 2. 通过模板对象注册组件
    Vue.component('myComA', com1)
    // 或者把1, 2 步 合成一步
    Vue.component('myComA', Vue.extend({
        template: '<h3>这是使用extend创建的组件</h3>'
    }))
    var vm = new Vue({
        el: '#app', //不可省略
    })
</script>
```

- 直接字符串(省略Vue.extend)：

```js
Vue.component('myComA', {
    template: '<h3>这是使用extend创建的组件</h3>'
})
var vm = new Vue({
    el: '#app', //不可省略
})
```

- 将模板字符串，定义到template或者script标签中：

```html
<body>
    <div id="app">
        <my-com-a></my-com-a>
    </div>
    <!-- 在 #app的外面书写 -->
    <template id="tmp1">
        <!--或者使用 <script type="text/x-template" id="tmp1"> -->
        <div>
            <h3>这是第三种定义组件的方式,有代码提示</h3>
            <h4>好用</h4>
        </div>
    </template>
    <script>
        Vue.component('myComA', {
            template: '#tmp1' /* 这里写html没有智能提示*/
        })
        var vm = new Vue({
            el: '#app', //不可省略
        })
    </script>
</body>
```

## 局部组件

- 上面创建的是全局组件 - 所有vue实例都能使用
- 可以创建局部组件(`components`) - 类似于局部 filters/directives

```html
<body>
    <div id="app">
        <my-com-a></my-com-a>
    </div>
    <!-- 在 #app的外面书写 -->
    <template id="tmp1">
        <div>
            <h3>这是第三种定义组件的方式,有代码提示</h3>
            <h4>好用</h4>
        </div>
    </template>
    <script>
        var vm = new Vue({
            el: '#app', //不可省略
            data: {},
            components: {
                myComA: {
                    template: '#tmp1'
                }
            }
        })
    </script>
</body>
```

## 组件中的data

1. `root组件/实具有 el 属性 -> 指向自己控制的html模板`;
2. `子组件的具有template属性 -> 指向自己控制的html模板`;
3. `除了上面两点不同: 子组件可以具有root组件其他所有的属性`;

> 注意: root组件中的data是一个对象, `子组件中的data必须是一个函数且返回一个对象(函数的闭包) `-> 多次子组件的调用时data的数据彼此独立. 如下便没有形成闭包,多个组件的引用相互影响

```html
<div id="app">
    <counter></counter>
    <counter></counter>
</div>

<template id="tmp1">
    <div>
        <input type="button" value="点我+1" @click="increment">
        <h4>count的值为{{count}}</h4>
    </div>
</template>

<script>
    var countObj = { count: 0 }
    Vue.component('counter', {
        template: '#tmp1',
        data: function() {
            return countObj /* 如此便没有函数的闭包 */
        },
        methods: {
            increment() {
                this.count++
            }
        }
    })
    var vm = new Vue({
        el: '#app', //不可省略
        data: {}
    })
</script>
```

![](http://ww1.sinaimg.cn/large/48356ef5ly1fzq4bflzacj203m04lt9a.jpg)

## 组件切换

- 方式一: if/ else-if 只能切换两个组件

```html
<body>
    <div id="app">
        <input type="button" value="登录" @click="flag=true">
        <input type="button" value="注册" @click="flag=false">
        <login v-if="flag"></login>
        <register v-else-if="!flag"></register>
    </div>
    <script>
        Vue.component('login', {
            template: '<h3>登录组件</h3>',
        })
        Vue.component('register', {
            template: '<h3>注册组件</h3>',
        })
        var vm = new Vue({
            el: '#app', //不可省略
            data: {
                flag: true
            }
        })
    </script>
</body>
```

- 方式二:使用 <component :is="comName"></component>

```html
<body>
    <div id="app">
        <a href="javascript:;" @click.prevent="comName='login'">登录</a>
        <a href="javascript:;" @click.prevent="comName='register'">注册</a>
        <!-- component是占位符,具体值是is后面的值 -->
        <component :is="comName"></component><!-- 组件名称是字符串 -->
    </div>
    <script>
        Vue.component('login', {
            template: '<h3>登录组件</h3>',
        })
        Vue.component('register', {
            template: '<h3>注册组件</h3>',
        })
        var vm = new Vue({
            el: '#app', //不可省略
            data: {
                comName: 'login'
            }
        })
    </script>
</body>
```

- 总结: 目前为止用的的Vue提供的标签有:
        - component
        - template
        - transition
        - transition-group

## 组件的切换/过渡动画

上面实现了组件的切换,过于突兀, 也可以添加[组件过渡动画](https://cn.vuejs.org/v2/guide/transitions.html#%E5%A4%9A%E4%B8%AA%E7%BB%84%E4%BB%B6%E7%9A%84%E8%BF%87%E6%B8%A1);

```html
<style>
    .x-enter,
    .x-leave-to {
        opacity: 0;
        transform: translate(150px, 0)
    }
    .x-enter-active,
    .x-leave-active {
        transition: all 0.5s ease;
    }
</style>
=======
<body>
    <div id="app">
        <a href="javascript:;" @click.prevent="comName='login'">登录</a>
        <a href="javascript:;" @click.prevent="comName='register'">注册</a>
        <transition name="x" mode="out-in"> 
                <!-- 动画的模式为前一个先out,后一个再in -->
            <component :is="comName"></component>
        </transition>
    </div>
    <script>
        Vue.component('login', {
            template: '<h3>登录组件</h3>',
        })
        Vue.component('register', {
            template: '<h3>注册组件</h3>',
        })
        var vm = new Vue({
            el: '#app', //不可省略
            data: {
                comName: 'login'
            }
        })
    </script>
</body>
```

# 组件的传值

## 父组件->子组件 传递数据

- Vue中,默认情况下: 子组件无法访问父组件的数据, 反之亦然.
- 如果希望子组件访问父组件的数据, 需要:
	1. 调用子组件时`通过v-bind传值`;
	2. 在子组件中通过`props属性接收(数组)`;
	3. 在子组件中使用(就相当于自己的属性,可以用this.xxx调用);

```html
<body>
    <div id="app">
        <!-- 1.调用子组件的时候传值 -->
        <com1 :pxx="msg"></com1>
    </div>
    <!-- 3.子组件中可以调用pxx -->
    <template id="com1">
        <h3 @click="show">我是子组件com1 -- {{pxx}}</h3>
    </template>
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                msg: '父组件的msg'
            },
            methods: {},
            components: {
                com1: {
                    template: '#com1',
                    props: ['pxx'],// 2. 子组件接受父组件的数据
                    data() {
                        return {
                            msg: '子组件的msg'
                        }
                    },
                    methods: {
                        show() {
                            console.log(this.pxx)
                        }
                    }
                }
            }
        })
    </script>
</body>
```

- 注意: 
	- 通过绑定的形式把父组件的数据传递过来的同时, `可以指定一个的变量名(如: pxx)接收`.
	- `该变量(pxx)存放在子组件的props数组中, 是只读的,` data是r/w的;
	- `子组件不能在自己的data中再定义与该变量(pxx)相同的变量`;
	- `子组件可以通过 this.pxx 访问该变量`.

## 父组件->子组件 传递方法

- 上面是父组件->子组件传递数据, 用同样的方式也可以传送方法;
- 我们通常使用另一种方式:
	1. 调用子组件是通过 v-on传值: `<com1 @pxx="pshow"></com1>`
	2. 子组件内部通过`this.$emit('pxx', 要传递的数据)`方式，来调用父组件中的方法，`要传递的数据`为父组件pshow的相关参数.

## 子组件 -> 父组件 传递数据

**原理**：父组件将方法的引用，传递到子组件内部，`子组件在内部调用父组件传递过来的方法`，同时把`要发送给父组件的数据，在调用方法的时候当作参数传递进去`；

## $refs

- 父元素想访问子元素的数据/方法可以通过$refs, 这个方法更简单,详细见下一节
- 由于Vue不支持操作DOM, 那么如何获得DOM元素呢?
- 通过给相应的DOM节点添加属性`<h3 ref="myh3">哈哈,今天天气真好</h3>`, 可以通过`this(vm).$refs`获取很方便获取DOM节点;
- 同样的方式我们也可以`给子组件添加 ref 属性, 获得子组件.然后进而获得子组件的数据/方法...`

```html
<body>
    <div id="app">
        <input type="button" value="获取元素" @click="getElement">
        <h3 ref="myh3">
            <p>哈哈,今天天气真好</p>
        </h3>
        <login ref="login"></login>
    </div>
    <script>
        var vm = new Vue({
            el: '#app',
            data: {},
            methods: {
                getElement() {
                    console.log(this.$refs);
                    console.log(this.$refs.myh3);
                    console.log(this.$refs.myh3.innerText);
                    console.log(this.$refs.myh3.innerHtml);
                }
            },
            components: {
                login: {
                    template: '<h3>登录组件</h3>'
                }
            }
        })
    </script>
</body>
```

# 传值案例-列表评论


