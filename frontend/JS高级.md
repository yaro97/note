# JS高级

## 基本概念复习

### 重新认识JS

- JavaScript 是什么
    - 解析执行：轻量级解释型的，或是 JIT 编译型的程序设计语言
    - 语言特点：动态，头等函数 (First-class Function)
    - 又称函数是 JavaScript 中的一等公民
    - 执行环境：在宿主环境（host environment）下运行，浏览器是最常见的 JavaScript 宿主环境
    - 但是在很多非浏览器环境中也使用 JavaScript ，例如 node.js
    - 编程范式：基于原型、多范式的动态脚本语言，并且支持面向对象、命令式和声明式（如：函数式编程）编程风格
- JavaScript 与浏览器的关系
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzosvt4p4zj20ds0bw3zt.jpg)
- JavaScript 的组成
    1. Ecmascript  描述了该语言的语法和基本对象
    2. DOM  描述了处理网页内容的方法和接口
    3. BOM  描述了与浏览器进行交互的方法和接口
    
- JavaScript 可以做什么
    > Any application that can be written in JavaScript, will eventually be written in JavaScript. 凡是能用 JavaScript 写出来的，最终都会用 JavaScript 写出来

    -  [知乎 - JavaScript 能做什么，该做什么？](https://www.zhihu.com/question/20796866)
    -  [最流行的编程语言 JavaScript 能做什么？](https://github.com/phodal/articles/issues/1)
- JavaScript 发展历史
    [JavaScript 标准参考教程 - JavaScript 语言的历史](http://javascript.ruanyifeng.com/introduction/history.html)
    - JavaScript 的诞生
    - JavaScript 与 Ecmascript 的关系
    - JavaScript 与 Java 的关系
    - JavaScript 的版本
    - JavaScript 周边大事记

### 相关概念

- 语法
    - 区分大小写
    - 标识符
    - 注释
    - 严格模式
    - 语句
- 关键字和保留字(将来可能会升级为关键字,如:int)
- 变量
- 数据类型
    - typeof 操作符
    - Undefined
    - Null
    - Boolean
    - Number
    - String
    - Object
- 操作符
- 流程控制语句
- 函数

### JS中的数据类

avaScript 有 **5 种简单数据类型**：`Undefined、Null、Boolean、Number、String` 和 **1 种复杂数据类型**: `Object` 。
- 基本类型（值类型）
    - Undefined
    - Null
    - Boolean
    - Number
    - String
- 复杂类型（引用类型）
    - Object
    - Array
    - Date
    - RegExp
    - Function
    - 基本包装类型:**允许非对象类型调用相应的方法,临时创建,用过作废**
        - Boolean
        - Number
        - String
    - 单体内置对象
        - Global
        - Math
- 类型检测
    - `typeof 对象类型全部都是Object`
    - `instanceof`
    - `Object.prototype.toString.call() 对象更详细`
- 值类型和引用类型在内存中的存储方式（画图说明）
    - 值类型按值存储
    - 引用类型按引用存储
- 值类型复制和引用类型复制（画图说明）
    - 值类型按值复制
    - 引用类型按引用复制
- 值类型和引用类型参数传递（画图说明）
    - 值类型按值传递
    - 引用类型按引用传递
- 值类型与引用类型的差别
    - 基本类型在内存中占据固定大小的空间，因此被保存在栈内存中
    - 从一个变量向另一个变量复制基本类型的值，复制的是值的副本
    - 引用类型的值是对象，保存在堆内存
    - 包含引用类型值的变量实际上包含的并不是对象本身，而是一个指向该对象的指针
    - 从一个变量向另一个变量复制引用类型的值的时候，复制是引用指针，因此两个变量最终都指向同一个对象
- 小结
    - 类型检测方式
    - 值类型和引用类型的存储方式
    - 值类型复制和引用类型复制
    - 方法参数中 值类型数据传递 和 引用类型数据传递

### JS执行过程

JavaScript 运行分为两个阶段：
- 预解析
    - 全局预解析（所有变量和函数声明都会提前；同名的函数和变量函数的优先级高）
    - 函数内部预解析（所有的变量、函数和形参都会参与预解析）
        - 函数
        - 形参
        - 普通变量
- 执行
    - 先预解析全局作用域，然后执行全局作用域中的代码，
- 在执行全局代码的过程中遇到函数调用就会先进行函数预解析，然后再执行函数内代码。

## JS面向对象编程

### 面向对象(OOP)介绍

- 什么是对象
    - Everything is object （万物皆对象）
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzot6osq9jj20fz08vthy.jpg)
    - 一切具体的事物都是对象.对象有类创建,或者说对象的父级是类.如:小明, 小军...都是对象,具有特征(肤色/身高/体重/性别...)和行为(吃饭/睡觉/学习/玩...); 而小明,小军都是属于 "人"这个类.
    - 具体特指的某个事物,有特征(属性)和行为(方法).
    - ECMAScript-262 把对象定义为：无序属性的集合，其属性可以包含基本值、对象或者函数。
    - **Note**: JS现阶段不是面向对象的语言,而是基于对象的语言,我们使用JS来模拟面向对象.

- 编程思想
    根据需求,抽象出相关的对象,总结对象的特征和行为,把特征变成属性，行为变成方法,然后定义(js)构造函数,实例化对象,通过对象调用属性和方法,完成相应的需求.
- 什么是面向对象
    - **目的: 提高代码的开发效率和可维护性**。
    - 定义: 面向对象编程 —— Object Oriented Programming，简称 OOP ，是一种编程开发思想。 它将真实世界各种复杂的关系，抽象为一个个对象，然后由对象之间的分工与合作，完成对真实世界的模拟。
    - 解析: 在面向对象程序开发思想中，每一个对象都是功能中心，具有明确分工，可以完成接受信息、处理数据、发出信息等任务。因此，面向对象编程具有灵活、代码可复用、高度模块化等特点，容易维护和开发，比起由一系列函数或指令组成的传统的过程式编程（procedural programming），更适合多人合作的大型软件项目。
    - 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。 
    - 面向对象与面向过程：
        - 面向过程就是亲力亲为，事无巨细，面面俱到，步步紧跟，有条不紊
        - 面向对象就是找一个对象，指挥得到结果
        - 面向对象将执行者转变成指挥者
        - 面向对象不是面向过程的替代，而是面向过程的封装
    - **面向对象的特性**：
        - `封装性`-重用的内容封装,方便重复利用;
        - `继承性`(类和类之间的关系);
        - `[多态性]`-同一个行为,针对不同的对象,产生不同的效果.
    - **封装的概念**: `语句 --> 函数 + 属性-->对象 --> 文件 -- > 文件夹(框架)`
    - 扩展阅读：
        - [维基百科 - 面向对象程序设计](https://zh.wikipedia.org/wiki/%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1)
        - [知乎：如何用一句话说明什么是面向对象思想？](https://www.zhihu.com/question/19854505)
        - [知乎：什么是面向对象编程思想？](https://www.zhihu.com/question/31021366)

- JS面向对象的基本体现
    - JS中没有类(class)的概念,所以不是基于类的语言.
    - JS通过`自定义构造函数模拟类`,实例化对象(或叫做创建对象),称之为基于类的语言.
    - JS可以通过原型/拷贝实现`继承`.
    - JS不实现多态性.

### 创建对象的三种方式

- 方法一: 调用`系统构造函数Object`创建（=实例化）对象，Object为系统构造函数。

    ```js
    var person = new Object();
    person.name = 'lisi';
    person.age = 35;
    person.job = 'actor';
    person.sayHi = function () {
    console.log('Hello,everyBody');
    };
    ```

    - **延伸: 工厂函数创建对象**：系统的Object构造函数每创建一个对象，都要重复写一遍相应的属性，所以可以借用函数，复用重复代码。

        ```js
        function createObj(name, age) {
            let obj = new Object()
            //添加属性, 方法
            obj.name = name
            obj.age = age
            obj.sayHi = function () {
                console.log('我叫' + this.name + '今年' + this.age)
            }
            return obj // 必需
        }
        // 创建/实例化对象
        let per1 = createObj('小芳', 20)
        per1.sayHi()
        ```

- 方法二: `自定义构造函数`创建对象（传值灵活，创建不同对象）：

    - 自定义构造函数创建对象（传值灵活，创建不同对象）：
        - 函数和构造函数的“`约定`”表象区别是：`构造函数名的首字母大写`，告诉其他程序员，这不是普通函数；
        - 函数和构造函数的“`约定`”用途区别：`普通函数是用来调用的，构造函数是用来创建对象的`。
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzotytziwij20hz074thy.jpg)
        - 自定义构造函数，其实就是再工厂函数的基础上，省略了`var this=new Object() `和 `return this`;
        - 用自定义构造函数创建对象时(`var per1 = new Person(...)`)，new在执行时做了四件事（参考工厂函数）：

            ```
            a. 在内存中申请一块空闲空间，存储创建的新对象；
            b. 把当前对象赋值给this；
            c. 设置this对象的属性和方法；
            d. 把this这个对象返回。
            ```

    - 自定义构造函数与工厂函数创建对象的区别
        - 共同点:都是函数, 都可以创建对象, 都可以传入参数.
        - 不同点:

            |              | 工厂模式                 | 自定义构造函数 |
            | ------------ | ------------------------- | -------------- |
            | 函数名首字母 | 小写 person               | 大写 Person    |
            | new关键字    | 有                        | 无             |
            | 返回值       | 有                        | 无             |
            | 当前对象     | var obj =   new Object(); | this           |
            | 创建对象     | 直接调用函数              | 需要new关键    |

- 方法三: `字面量创建对象`（无法传值：一次性对象）
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzou1guf56j20bm0akthy.jpg)

- 三种方式的区别
    - 调用系统`Object()`----->创建出来的对象都是Object类型的,不能很明确的指出这个对象是属于什么类型
    - 字面量的方式`{}`----->只能创建一个对象(一次只能创建一个)
    - `工厂模式`创建对象----->只是为了推出---->自定义构造函数的方式
    - `自定义构造函数`(优化后的工厂模式)

### 构造函数-实例对象

- 实例对象和构造函数的关系
    - 实例对象是通过构造函数("类")来创建的---创建的过程叫实例化(`instance`)
    - 如何判断对象是不是这个数据类型?
        1. `console.log(dog.constructor == Animal);`
        2. `console.log(dog instanceof Person);`
    - 尽量使用第二个方法判断,因为实例对象中没有直接`constructor`属性,是查找的`_proto_`属性(指向`构造函数的prototype对象`),才有`constructor`属性的.

- 构造函数的问题
    - 在构造函数中定义的属性/方法,当实例化时,实例对象的属性/方法都是在自己的空间中存在的;如果创建多个实例对象,这些属性/方法都会在独立的空间中存在,浪费内存空间.
    - 如下:可以把函数(方法)放置在构造函数外面解决重复申请内存的问题:

        ```js
        function myEat() {
            console.log("吃大榴莲");
        }
        var myEat = 10;
        function Person(name, age) {
            this.name = name;
            this.age = age;
            this.eat = myEat;
        }

        var per1 = new Person("小白", 20);
        var per2 = new Person("小黑", 30);
        console.dir(per1);
        console.dir(per2);
        console.log(per1.eat == per2.eat);//true
        ```

    - **NOTE**: 这种外置函数(方法),可以解决重复申请内存的确定,但是有可能引起变量的覆盖(没有封装在一起, 外面的变量/函数可能冲突).
    - 最优方法: 通过原型来解决---------数据共享,节省内存空间(原型作用之一,另一个是实现继承)

- 通过原型解决数据共享问题
    - 如果构造函数创建的实例对象具有共同是属性/方法,我们可以通过原型来添加,实现数据共享.

    ```js
    function Person(name, age) {
        this.name = name;
        this.age = age;
    }
    //通过原型来添加方法,解决数据共享,节约内存空间
    Person.prototype.eat = function () {
        console.log("我喜欢吃大榴莲");
    };
    var p1 = new Person("小红", 20);
    var p2 = new Person("小红", 30);
    console.log(p1 == p2);//false 不是同一个对象
    console.log(p1.eat == p2.eat)//true 同一个方法
    console.dir(p1);//可以得知eat方法不在p1对象中,而是在p1的__proto__属性的下面.
    ```

- 体验面向JS对象编程
    - 案例:点击按钮改变div的多个样式

    ```js
    //创建构造函数
    function ChangeStyle(btnObj, dvObj, json) {
        this.btnObj = btnObj;
        this.dvObj = dvObj;
        this.json = json;
    }
    //为构造函数的原型添加方法
    ChangeStyle.prototype.init = function () {
        //保存实例对象的this为that
        var that = this;
        this.btnObj.onclick = function () {//按钮点击事件
            for (var key in that.json) {
                that.dvObj.style[key] = that.json[key];
            }
        };
    };
    //实例化对象,改变多个属性(点击一个对象,改变另一个对象的多个样式)
    var json = {"backgroundColor": "red", "width": "300px", "height": "300px", "opacity": "0.5"};
    var cs = new ChangeStyle(my$("btn"), my$("dv"), json);
    cs.init();
    ```

### 原型

- 原型介绍
    JS规定: 
    1. 每个函数(含构造函数)都有一个 `prototype` 属性，指向另一个对象。 这个对象的所有属性和方法，都会被构造函数的实例继承. so, 我们可以把所有对象实例需要共享的属性和方法直接定义在 `prototype` 对象上。
    2. 每个对象(实例对象/`prototype`对象)都有一个 `__proto__`原型, 而`prototype`对象还含有一个 constructor 属性,指向其对应的构造函数.
    3. 对象是由构造函数(类似于python中的"类")创建的, 每个对象都有一个 `__proto__`原型,这个原型最终指向其构造函数的`prototype`对象(可以这么理解:  **`__proto__`原型是`prototype`原型对象的快捷键**).
    4. 实例对象优先查找自己的属性/方法; 如果没有,进而查找 `__proto__`原型(`prototype`对象)的属性/方法.
    5. **原型(对象)的作用有**:
        a. **数据共享(避免重复开辟内存空间)**;
        b. **实现继承**.
        > 二者的最终目的都是:**`节约空间`**.

- 构造函数、实例、原型三者之间的关系
    - 构造函数可以实例化成对象;
    - (构造)函数中有一个属性叫 `prototype`, 该属性是一个对象;
    - 构造函数的原型对象(`prototype`)中有一个 constructor 构造器(构造函数),这个构造器指向的是其所在的原型对象所在的构造函数.
    - 实例对象的原型 (`__proto__`) 指向创建该实例对象的构造函数中的原型对象.
    - 所有实例都直接或间接继承了原型对象的成员(函数/方法...)
    - 实例对象优先访问自己的属性/方法; 也可以访问其构造函数的原型对象 (`prototype`) 中的方法.
    - `prototype`供程序员使用,是标准属性;`__proto__` 供浏览器使用,是非标准属性(有些浏览器不支持)。
    - 实例对象使用原型的方法:per.`__proto__`.eat();, __proto__不是标准属性,可以省略:per.eat();. 
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoubzd00wj20j40bhdgc.jpg)
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzouc5n8lvj20l309xdh9.jpg)

- 一次性为原型对象添加多个成员
    - 前面我们一条语句为原型设置一个属性/方法,太过麻烦;
    - 我们可以直接把所有属性/方法包装成对象,直接赋值给原型对象即可.
    - 但是, 切记莫忘了设置原型对象的构造器constructor属性.

        ```js
        function Student(name, age, sex) {
            this.name = name;
            this.age = age;
            this.sex = sex;
        }
        //简单的原型写法
        Student.prototype = {
            //必须手动修改构造器的执行,否则会没有这个属性
            constructor: Student,
            height: "188",
            weight: "55kg",
            study: function () {
                console.log("学习好开心啊");
            }
        };
        //实例化对象,并初始化
        var stu = new Student("段誉", 20, "男");
        stu.study();
        ```

- 原型中的方法/属性之间也可以相互调用
  
    ```js
    //构造函数中this(实例对象))的方法/属性之间可以相互调用
    //同样,原型中的方法/属性之间也可以相互调用
    function Animal(name, age) {
        this.name = name;
        this.age = age;
    }

    //原型中添加方法
    Animal.prototype.eat = function () {
        console.log("动物吃东西");
        this.play();//这里的this指Animal.prototype,最终实例化后还是被实例对象调用
    };

    Animal.prototype.play = function () {
        console.log("动物完东西");
    }
    ```

- 实例对象使用属性/方法 优先访问实例对象,然后再查找原型对象
    - 实例对象使用的属性/方法,优先在实例对象中查找,找到则使用,找不到再查找__proto__指向的原型对象中,找到则使用,找不到,则:属性显示undefined,方法报错.
    - 如:Array Number Date String 等构造函数创建的实例对象,相关的方法都在原型中.

    ```js
    function Person(age, sex) {
        this.age = age;
        // this.sex=sex;
        this.eat = function () {
            console.log("构造函数中的吃");
        }
    }

    // Person.prototype.sex ="女";
    Person.prototype.eat = function () {
        console.log("原型对象中的吃");
    };
    var per = new Person(20, "男");
    console.log(per.sex);
    per.eat();
    ```

- 为内置对象添加原型方法 -> 改变源码

    ```js
    //让字符串倒序输出
    String.prototype.myReverse = function () {
        for (var i = this.length - 1; i >= 0; i--) {
            console.log(this[i]);
        }
    };
    var str = "abcdefg";
    str.myReverse();

    //为Array增加一个使用冒泡排序的方法(自带的不稳定)
    Array.prototype.mySort = function () {
        //冒泡排序代码
    };

    //为String添加一个打招呼的方法
    String.prototype.sayHi = function () {
        console.log(this + ":哈哈!我又变帅了")
    };
    ```

- 把局部变量变成全局变量
    - 自调用函数:创建的时候直接调用,一次性
    - 把局部变量赋值给window的属性即可;
    - window是浏览器的顶级对象,变量/函数/对象都在window中保存

        ```js
        (function () {
            var num = 10;
            window.num = num;
        })();
        console.log(num) //可以访问到num的指
        ```
        
    - 案例:把随机数对象暴露给window成为全局变量

        ```js
        //通过自调用函数产生一个随机数实例对象,在外部调用该随机数对象产生随机数
        (function () {
            //产生随机数的构造函数
            function Random() {
            }
            //在原型对象中添加方法
            Random.prototype.getRandom = function (min, max) {
            return Math.floor(Math.random() * (max - min) + min);
            };
            //创建随机数实例对象,并附着在window属性上供外部使用
            //用random,防止和内置Random冲突
            window.random = new Random();
        })();
        var randomNum = random.getRandom(3, 6);
        console.log(randomNum);
        ```

### 继承

- OOP知识回顾
    - JS面向对象
        - JS是基于类的语言,不是面向对象的语言.
        - JS中没有类(Class)的概念,通过构造函数来模拟类(Class)的概念.
        - 为啥要模拟类:因为类符合人的思想,易编程,已维护,高内聚,低耦合.
    - 面向对象三台特性
        - 封装:就是包装
            ```
            > 一个值放在一个变量中--封装
            > N多重复代码放在一个函数中--封装
            > 一系列属性/方法放在对象中--封装
            > N多类似的对象放在一个js文件中--封装
            > N个文件/夹放在一个文件夹中--封装
            ```
        - 继承
            ```
            > 首先,继承是一种关系,类(class)与类之间的关系;
            > JS中没有类,但是可以通过构造函数模拟类,然后通过构造函数/原型来实现继承;
            > 同原型,继承也是为了数据共享;
            ```
            **Note**: 原型作用1:数据共享,节约内存空间; 原型作用2:为了实现继承.
        - 多态
            ```
            > 一个对象有不同的行为,或者是同一个行为针对不太的对象,产生不同的结果;
            > 要想有多态,首先要有继承;
            > **JS中可以模拟多态,但是不会去使用**,也不会去模拟,因为这会导致--数据不能共享,浪费内存空间.
            ```

- JS中继承的实现
    - 背景代码如下:

        ```js
        function Person(name, age, sex) {
            this.name = name;
            this.age = age;
            this.sex = sex;
        }
        Person.prototype.eat = function () {
                console.log("人可以吃东西");
        };
        ```

    - 方法一:通过原型实现继承:
        - 优点:属性/方法都集成;
        - 缺点:写死了,属性不能更改,

        ```js
        function Student(score) {
            this.score = score;
        }
        Student.prototype = new Person("小明", 10, "男");
        ```

    - 方法二:借用构造函数实现继承:
        - 优点:属性可以更改; 
        - 缺点:原型方法无法继承.

        ```js
        function Student(name, age, sex, score) {
            Person.call(this, name, age, sex);//this指代Student的实例对象
            this.score = score;
        }
        ```

    - 方法三:组合继承:
        - 通过原型继承原型方法;
        - 通过构造函数继承属性.
        
        ```js
        function Student(name, age, sex, score) {
            Person.call(this, name, age, sex);//this指代Student的实例对象
            this.score = score;
        }//继承属性
        Student.prototype = new Person();//实例化时不传参-继承方法
        ```

    - 方法四:拷贝继承:

        ```js
        // - 方式一:只是拷贝地址的指向
        var obj1 = {name: "yaro", age: 38};
        var obj2 = obj1;
        // - 方式二:浅拷贝
        var obj1 = {name: "yaro", age: 38};
        var obj2 = {};
        for (var key in obj1) {
            obj2[key] = obj1[key];
        }
        // - 方式三:可以直接拷贝原型对象(系统的有些东西无法拷贝)
        var obj = Person.prototype;
        ```

### 原型链

- 原型链
    - 由上面可知:
        - 实例对象可以直接访问原型对象中的属性/方法;
        - 任何函数都有prototype(原型对象),构造函数也是;
        - 对象都具有__proto__属性指向其构造函数的原型链.
        - prototype原型对象含有constructor属性,指向其构造函数.
    - 表面上看:构造函数创造了(实例化)了实例对象,但是二者之间没有直接的关系.
    - 原型链:
        - 是一种实例对象和原型对象之间的关系,这种关系是通过__proto__原型来联系的;
        - `每个对象都有自己的原型对象(其构造函数的指向的), 原型对象也是对象, 原型对象也有自己的原型对象, 如此便形成了一个链接结构,叫做原型链`.

- 原型(链)指向的改变
    - `实例对象的__proto__原型`指向的是该产生该实例对象的构造函数的原型对象;
    - 构造函数的原型对象(prototype)指向如果改变了,对应的实例对象的原型(`__proto__`)的指向也会改变.
    - 原型指向改变后,之前添加的方法会失效, 之后再添加方法即可使用.
    - 构造函数中的this指的是实例对象,原型对象添加的方法中的this也是实例对象(`Person.prototype.eat`看似属于`Person.prototype`,最终还是由实例对象调用).

- 对象的成员的搜索原则:原型链
    - 实例对象访问某个属性/方法,优先搜索实例对象,然后再搜索原型对象, 一直搜索到原型链的末端.
    - 属性没有的话,会显示undefined,方法没有会报错;
        - JS是动态语言,只要"."了,就相当于 var xxx;
    
- 继承的原型链
    - 自定义构造函数创建的实例对象,
    - 实例对象可以改变原型的指向实现继承.
    - 图中实例对象: `erHa.__proto__ --> dog.__proto__ --> animal.__proto__ -->Animal.prototype的__proto__ --> Object.prototype的 __proto__-->null(没有__proto__)`
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzousp027xj20mu0nfgqw.jpg)

- 页面DIV对象原型链
    页面中的DIV元素对象: `divObj.__proto__--> HTMLDivElement.prototype的__proto__--> HTMLElement.prototype的__proto__-->Element.prototype的 __proto__-->Node.prototype的 __proto__-->EventTarget.prototype的 __proto__-->Object.prototype的 __proto__-->null(没有__proto__)`

- 函数原型链
    - 所有的函数都是对象.
    - 所有的函数: `foo.__proto__ -->Function.prototype的__proto__ --> Object.prototype的 __proto__-->null(没有__proto__)`

## OOP项目-贪吃蛇

源文件-见百度网盘: `全部文件>others>编程-源文件>贪吃蛇项目-源文件.7z`

### 概述

- 目标
    - 熟悉面向对象编程:
    根据需求,抽象出相关的对象,总结对象的特征和行为,把特征变成属性，行为变成方法,然后定义(js)构造函数,实例化对象,通过对象调用属性和方法,完成相应的需求.
    - 熟悉原型方法的添加;
    - 了解私有函数
    - 使用bind方法

- 过程总结
    - 地图对象: 
        - 宽，高，背景颜色;
        - 地图需要设置reletive.因为小蛇和食物相对地图随机位置显示,是脱离文档流的.
    - 食物对象---div元素
        - elements--->存储div的数组(将来删除的食物div时候,先从map中删除div,再从数组中移除div)
        - 食物:宽,高,背景颜色,横坐标,纵坐标
        - 一个食物就是一个对象,这个对象有相应的属性,这个对象需要在地图上显示
        - 最终要创建食物的对象,先 有构造函数,并且把相应的值作为参数传入到构造函数中
        - 食物要想显示在地图上,食物的初始化就是一个行为: 

            ```
            > 1.食物的构造函数--->创建食物对象
            > 2.食物的显示的方法-->通过对象调用方法,显示食物,设置相应的样式
                2.1 因为食物要被小蛇吃掉,吃掉后应该再次出现食物,原来的食物就删除了
                2.2 每一次初始化食物的时候先删除原来的食物,然后重新的初始化食物
                2.3 通过一个私有的函数(外面不能调用的函数)删除地图上的食物,同时最开始的时候食物也相应的保存到一个数组中,再从这个数组中把食物删除
            ```

        - 最后的时候,把食物的构造函数给window下的属性,这样做,外部就可以直接使用这个食物的构造函数了
    - 小蛇对象
        - 属性: 每个身体都有宽，高，方向
        - 属性:身体分三个部分,每个部分都是一个对象,每个部分都有横纵坐标,背景颜色
        - 小蛇要想显示在地图上,先删除之前的小蛇,然后再初始化小蛇(小蛇要移动)--方法
        - 小蛇要移动---方法
        - 思路:把小蛇的头的坐标给小蛇第一部分的身体,第一部分的身体的坐标给下一个部分身体
        - 小蛇的头,需要单独的设置:方向

- 项目目录
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzov0hbi14j204g02z743.jpg)

### 贪吃蛇.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="food.js"></script>
    <script src="snake.js"></script>
    <script src="game.js"></script>
    <style>
        .map {
            width: 800px;
            height: 600px;
            background-color: #ccc;
            position: relative;
        }
    </style>
</head>
<body>
    <!--画出地图-->
    <div class="map"></div>
    <script>
        //获取map对象 
        map = document.querySelector(".map");
        //初始化游戏对象
        game = new Game(map); //切记:创建对象需要用new关键字!!!
        //开始游戏
        game.init();
    </script>
</body>
</html>
```

### food.js

```js
//自调用函数-食物
(function () {
    var elements = []; //用来保存每个小方块
    //食物就是一个对象,有宽高/颜色/坐标,先定义构造函数,然后创建对象
    function Food(x, y, width, height, color) {
        this.x = x || 0;
        this.y = y || 0;
        this.width = width || 20;
        this.height = height || 20;
        this.color = color || "green";
    }
    
    //为原型添加初始化方法(作用:在页面中显示这个食物)
    //因为食物要在地图上显示,所以,需要地图这个参数
    Food.prototype.init = function (map) {
        //先删除map中的所有食物;
        remove();
        
        //创建新食物div,添加到map中
        var div = document.createElement("div");
        map.appendChild(div);
        //设置div样式
        div.style.width = this.width + "px";
        div.style.height = this.height + "px";
        div.style.backgroundColor = this.color;
        //使用随机对象生成随机坐标
        div.style.position = "absolute";
        this.x = parseInt(Math.random() * (map.offsetWidth / this.width)) * this.width;
        this.y = parseInt(Math.random() * (map.offsetHeight / this.height)) * this.height;
        div.style.left = this.x + "px";
        div.style.top = this.y + "px";
        //把div加入到elements数组中,方便之后被"吃掉"--重新生成
        elements.push(div);
    };
    
    //私有函数(外部无法调用)--删除地图中的所有食物
    function remove() {
        //elements数组中有这个实物
        for (var i = 0; i < elements.length; i++) {
            var ele = elements[i];
            //在地图中删除该食物
            ele.parentElement.removeChild(ele);
            //在数组中删除该元素
            elements.splice(i, 1); //从第i项,删除1个
        }
    }
    //把Food暴露给window,供外界使用
    window.Food = Food;
}());
```

### snake.js

```js
//自调用函数-小蛇
(function () {
    var elements = []; //用来存放小蛇身体的每个部分
    //小蛇的构造函数
    function Snake(width, height, direction) {
        //小蛇的每个部分的宽
        this.width = width || 20;
        this.height = height || 20;
        //小蛇的身体
        this.body = [{
                x: 3,
                y: 2,
                color: "red"
            }, //头
            {
                x: 2,
                y: 2,
                color: "orange"
            }, //身体
            {
                x: 1,
                y: 2,
                color: "orange"
            } //身体
        ];
        //小蛇的方向
        this.direction = direction || "right";
    }
    
    //为原型添加方法--小蛇初始化的方法
    Snake.prototype.init = function (map) {
        //先删除之前的小蛇
        remove();
        //循环遍历,创建div
        for (var i = 0; i < this.body.length; i++) {
            //获取数组中的相应的对象
            var obj = this.body[i];
            //创建div
            var div = document.createElement("div");
            //把div加入的map中
            map.appendChild(div);
            
            //设置div的样式
            div.style.position = "absolute";
            div.style.width = this.width + "px";
            div.style.height = this.height + "px";
            div.style.left = obj.x * this.width + "px";
            div.style.top = obj.y * this.height + "px";
            div.style.backgroundColor = obj.color;
            
            //方向暂时不定
            
            //把div加入的elements数组中--为了删除
            elements.push(div);
        }
    };
    
    //为原型添加方法--小蛇动起来
    Snake.prototype.move = function (food, map) {
        //改变小蛇的身体的坐标位置
        var i = this.body.length - 1; //2
        for (; i > 0; i--) {
            this.body[i].x = this.body[i - 1].x;
            this.body[i].y = this.body[i - 1].y;
        }
        //根据方向,改变小蛇头部的坐标位置
        switch (this.direction) {
            case "right":
                this.body[0].x++;
                break;
            case "left":
                this.body[0].x--;
                break;
            case "up":
                this.body[0].y--;
                break;
            case "down":
                this.body[0].y++;
                break;
        }
        //判断有没有吃到食物:小蛇头和食物坐标一致
        var headX = this.body[0].x * this.width;
        var headY = this.body[0].y * this.height;
        if (headX === food.x && headY === food.y) {
            //获取小蛇的最后的尾巴(最后一个单元)
            var last = this.body[this.body.length - 1];
            //把最后的尾巴复制一个,重新加入到小蛇的body中
            this.body.push({ //不能直接push last,why?
                x: last.x,
                y: last.y,
                color: last.color
            });
            //把食物删除,重新初始化食物
            food.init(map);
        }
    };
    
    //删除小蛇的私有函数
    function remove() {
        //获取数组
        var i = elements.length - 1;
        for (; i >= 0; i--) {
            //先从html中删除
            var ele = elements[i];
            ele.parentElement.removeChild(ele);
            //在从数组中删除
            elements.splice(i, 1);
        }
    }
    
    //把Snake暴露给window,供外部访问
    window.Snake = Snake;
}());
```

### game.js

```js
//自调用函数-游戏对象
(function () {
    var that = null; //该变量的目的就是为了保存游戏Game的实例对象
    
    //游戏的构造函数
    function Game(map) {
        this.food = new Food(); //创建食物对象
        this.snake = new Snake(); //创建小蛇对象
        this.map = map; //接收传入的地图对象
        that = this; //存储此时的实例对象,方便后面的方法使用.
    }
    
    //为原型添加方法-初始化游戏
    Game.prototype.init = function () {
        //食物初始化
        this.food.init(this.map);
        //小蛇初始化
        this.snake.init(this.map);
        //调用让小蛇动起来的函数(一个函数一个功能)
        this.autoRun(this.food, this.map); //this指Game创建的对象
        //调用根据按键修改direction的方法--让小蛇随按键改变方向
        this.bindKey();
    };
    
    //添加原型方法-小蛇自动跑起来
    Game.prototype.autoRun = function (food, map) {
        var timeId = setInterval(function () {
            //切记!!:window.setInterval缩写setInterval
            //所以,定时器中的this指window!!!!!!
            this.snake.move(food, map); //改变新小蛇的位置,以便重新创建
            this.snake.init(map); //清理原来的小蛇,重新创建
            //横坐标最大值
            var maxX = map.offsetWidth / this.snake.width; //40
            //纵坐标最大值
            var maxY = map.offsetHeight / this.snake.height;
            //小蛇头的坐标
            var headX = this.snake.body[0].x;
            var headY = this.snake.body[0].y;
            if (headX < 0 || headX >= maxX || headY < 0 || headY >= maxY) {
                //撞墙了,停止定时器
                clearInterval(timeId);
                alert("游戏结束,下次再来...")
            }
        }.bind(that), 150);
        //函数调用bind方法,里面的this指函数本身;如果传入参数that,里面的this指that.
    };
    
    //添加源性方法-根据用户按键,改变小蛇的移动方向direction属性
    Game.prototype.bindKey = function () {
        //获取用户按键,改变小蛇方向
        document.addEventListener("keydown", function (event) {
            //获取按键的值
            switch (event.keyCode) {
                case 37:
                    this.snake.direction = "left";
                    break;
                case 38:
                    this.snake.direction = "up";
                    break;
                case 39:
                    this.snake.direction = "right";
                    break;
                case 40:
                    this.snake.direction = "down";
                    break;
            }
            console.log(this.snake.direction);
        }.bind(that), false);
    };
    
    //把Game暴露给window,供外部访问
    window.Game = Game;
}());
```

## 函数深入

### 函数的定义

- 函数的定义方式
    - 函数声明
    - 函数表达式
    - `new Function`
- 函数声明vs函数表达式
    - 函数的声明如果放在IF-else中,在ie8中会出现问题(预解析导致函数的声明被覆盖);函数表达式可以解决这个问题(见代码).
    - 以后宁愿用函数表达式,都不用函数的声明.

        ```js
        //函数的声明放在if-else中
        if (true) {
            function foo() {
                console.log("It is true");
            }
        } else {
            function foo() {
                console.log("It is false");//ie8会显示false
            }
        }

        //函数表达式放在if-else中
        var foo;
        if (true) {
            foo = function () {
                console.log("It is true");//正常显示true
            };
        } else {
            foo = function () {
                console.log("It is false");
            };
        }
        ```

    - 函数声明: `function foo () { }`
    - 函数表达式: `var foo = function () { }`
    - 函数声明与函数表达式的区别
        - 函数声明必须有名字
        - 函数声明会函数提升，在预解析阶段就已创建，声明前后都可以调用
        - 函数表达式类似于变量赋值
        - 函数表达式可以没有名字，例如匿名函数
        - 函数表达式没有变量提升，在执行阶段创建，必须在表达式执行之后才可以调用
        下面是一个根据条件定义函数的例子：
        
        ```js
        if (true) {
             function f () {
               console.log(1)
            }
        } else {
             function f () {
               console.log(2)
            }
        }
        ```

        以上代码执行结果在不同浏览器中结果不一致。
        不过我们可以使用函数表达式解决上面的问题：

        ```js
        var f
        if (true) {
             f = function () {
               console.log(1)
            }
        } else {
             f = function () {
               console.log(2)
            }
        }
        ```

### 函数的调用

- 普通函数
    1. `foo()`;
    2. `window.foo()`; 实质:window对象的方法
- 构造函数
    1. `var bar = new Foo()`; 实例化
- 对象方法
    1. `obj.foo()`;

### 函数中this的指向

- JS严格模式: 只需要在script标签的内最上面添加 "`use strict`"; 即可.
- 函数的内this的指向
    - 函数中this的指向与函数定义时无关, 而是取决于函数调用的上下文环境;
    - 不同场景下this的指向

        | 调用方式         | 非严格模式     | 备注                                      |
        | ---------------- | -------------- | ------------------------------------------ |
        | 普通函数调用     | window         | 严格模式下是 undefined                     |
        | 构造函数调用     | 实例对象       | 原型方法中 this 也是实例对象               |
        | 原型中添加的方法 | 实例对象       | Obj.prototype.method()最终还是实例对象调用 |
        | 对象方法调用     | 该方法所属对象 | 紧挨着的对象                               |
        | 事件绑定方法     | 绑定事件对象   |                                            |
        | 定时器函数       | window         | window.setInterval();                      |

    - 根本准则: `函数/方法 "." 前面紧挨着的对象`.

### 函数也是对象

- 函数和对象的判断依据
    - 有__proto__原型的是对象
    - 有prototype原型的函数
    - 二者都有,既是对象,也是函数

        ```js
        function foo() {
        }
        console.dir(foo);
        console.dir(Math);
        ```

        - 而函数foo两者都有,所以函数也是对象
        - Math中只有__proto__,所以是对象,不是函
    - 原生对象构造函数也都有 prototype 属性对象。
        - Object.prototype
        - Function.prototype
        - Array.prototype
        - String.prototype
        - Number.prototype
        - Date.prototype
        - ...

- 函数也是对象
    - 函数也是对象,对象不一定是函数;
    - 所有函数(对象)的构造函数为:Function() ,即所有函数都是 Function 的创建的实例对象.
    - 语法: `new Function ([arg1[, arg2[, ...argN]],] functionBody)`

        ```js
        var add = new Function("m", "n", "return m+n");
        console.log(add(10, 20));
        
        //Funciton本身是函数,也是对象
        console.dir(Function);
        ```

    - Function本身即是函数,也是对象,Function原型对象的__proto__指向了Object.prototype,Function对象的构造函数是Object().

### 函数对象的方法 call/aplly/bind

- 函数/方法的方法
    - 函数本身也是Function构造函数的对象,也有__proto__原型指向Function.prototype原型对象
    - Function.prototype原型对象具有call/apply/bind等方法;
    - 所有,函数可以看成Function的实例对象调用这些方法.
- 函数this指向
    - Bom的顶级对象是window,通过window可以把局部变量变成全局变量;
    - JS的变量/普通函数/定时器(函数)...都是window对象的属性/方法.
    - 所以,普通函数/定时器(函数)里面的this指window
    - 本质: `方法(函数)中this的指向为: 该函数前面 "." 前面紧跟着的对象`.
- call、apply方法
    - 二者都是用来调用函数，而且是立即调用.
    - 但是可以在调用函数的同时，通过第一个参数指定函数内部 this 的指向
    - 两个方法都可以实现: 函数/方法中this对象指向了newObj对象.只是参数传递格式不同而已.
    - 语法:
        - foo.apply(newObj, [arg1, arg2,...]);
        - foo.call(newObj, arg1, arg2,...);
        - Note: 
            ```
            > 如果参数中的newObj为null的话,和普通的调用 foo() 效果一样.
            > 二者可以改变函数中this上下文环境,但是并没有改变函数/方法的所属,之前的函数/方法属于window/实例对象,还得通过window/实例对象调用,只是函数内部的this的指向改变而已.
            > Object.prototype.toString.call() 查看某对象的数据类型.(toString()方法属于Object对象,用于将当前对象以字符串的形式返回。由于所有的对象都"继承"了Object的对象实例，因此几乎所有的实例对象都可以使用该方法。)
            ```
        
        ```js    
        function foo() {
        }
        console.log(typeof "");//string
        console.log(typeof 123);//number
        console.log(typeof []);//object
        console.log(typeof {});//object
        console.log(typeof foo);//function
        console.log(Object.prototype.toString.call(""));//[object String]
        console.log(Object.prototype.toString.call(123));//[object Number]
        console.log(Object.prototype.toString.call([]));//[object Array]
        console.log(Object.prototype.toString.call({}));//[object Object]
        console.log(Object.prototype.toString.call(foo));//[object Function]
        ```

- bind方法
    - bind释义:绑定,限制,约束.
    - 可以用来指定内部 this 的指向，然后生成/返回一个改变了 this 指向的新的函数;
    - 它和 call、apply 最大的区别是：bind 不会调用;
    - 可以在bind的实在传参,也可以在调用的时候传参;如果二者不同,以调用时的参数为准.
    - 语法: 
        - var bar = foo.bind(newObj, arg1, arg2...);
        - Note: 
            ```
            > 根据(复制)原来的函数foo,产生一个新的受限/约束的新函数,并且this指向了newObj.
            > newObj可以是null,表示不改变原来的this指向.
            > 参数可以在bind时传入,也可以在调用新函数bar是再传入.
            ```

        ```js
        function ShowRandom() {
            this.number = parseInt(Math.random() * 10 + 1);
        }

        ShowRandom.prototype.show = function () {
            window.setInterval(function () {
                console.log(this.number);//如果没有bind,这里的this指window,有了之后,指sr实例对象
            }.bind(this), 1000);//这里面的this指的是sr实例对象
        };
        var sr = new ShowRandom();
        sr.show();
        ```

### 函数的其他成员

函数作为Function的实例对象本身具有arguments,caller,length,name属性.

```js
function f1(x, y) {
    console.log(A.name); //函数名-只读,修改无效
    console.log(A.arguments);//实参-伪数组
    console.log(A.arguments.length);//实参的概述
    console.log(A.length);//形参的个数
    console.log(A.caller);//函数的调用者,默认是null,如果在f2函数中调用的f1,调用者为f2
}
```

### 高阶函数

- 高阶函数定义
    - 所谓高阶函数至少满足一下条件之一:
        > - 函数作为函数的参数;
        > - 函数作为函数的返回值;
    - 所谓函数为"一等公民"指: 函数可以和其他对象都一样,可以存放在数组中,可以当做参数, 可以赋值给变量....
- 函数作为参数
    - 定时器中需要传入函数当做参数

        ```js
        function f1(fn) {
            setInterval(function () {
                console.log("定时器开始");
                fn();
                console.log("定时器结束");
            }, 1000);
        }

        f1(function () {//传入匿名函数
            console.log("好困啊,好累啊,就是想睡觉");
        });
        ```

    - 案例-根据电影不同属性排序---数组的sort方法也需要函数当做参数(回调函数)
    
        ```js
        //排序应用:每个文件都有名字，大小,时间,都可以按照某个属性的值进行排序
        //三部电影,电影有名字,大小,上映时间
        function File(name, size, time) {
            this.name = name;//电影名字
            this.size = size;//电影大小
            this.time = time;//电影的上映时间
        }
        var f1 = new File("jack.avi", "400M", "1997-12-12");
        var f2 = new File("tom.avi", "200M", "2017-12-12");
        var f3 = new File("xiaosu.avi", "800M", "2010-12-12");
        var arr = [f1, f2, f3];

        function fn(attr) {
            //函数作为返回值
            return function getSort(obj1, obj2) {
                if (obj1[attr] > obj2[attr]) {
                    return 1;
                } else if (obj1[attr] == obj2[attr]) {
                    return 0;
                } else {
                    return -1;
                }
            }
        }

        var ff = fn("size");

        //函数作为参数
        arr.sort(ff);
        for (var i = 0; i < arr.length; i++) {
                console.log(arr[i].name + "====>" + arr[i].size + "===>" + arr[i].time);
        }
        ```

- 函数作为返回值
    - 简单实例

        ```js
        function foo() {
            console.log("我是foo函数");
            return function () {
                console.log("我是foo函数的返回值-函数");
            }
        }
        ```

    - 其他请参考闭包章节.

### 作用域链-预解析

- 作用域
    - 作用域：变量可以起作用的范围
    1. 全局变量和局部变量
        - 全局变量
            ○ ​在任何地方都可以访问到的变量就是全局变量，对应全局作用域;
            ○ 用var声明的变量，那么这个变量就是全局变量，全局变量可以在页面的任何位置使用（不同script标签内也可以访问）；
            ○ 如果网页页面/或浏览器不关闭，全局变量就不会释放空间，消耗内存；
            
        - 局部变量
            ○ ​只在固定的代码片段内可访问到的变量，最常见的例如函数内部。对应局部作用域(函数作用域)
            ○ 变量退出作用域之后会销毁，如：函数执行结束后，里面的局部变量就会释放。
        - 隐式全局变量：
            ○ 不使用var声明的变量是隐式全局变量，不推荐使用。
            ○ 函数内部的局部变量如果不使用var的话，为隐式全局变量，函数外面可以引用。
            ○ 使用var定义的全局变量不能使用delete命令删除；隐式全局变量可以使用delete删除（外部的引入的js中定义的变量是给人用的，不应该能被删除）。
    2. 块级作用域
        - 任何一对花括号（｛...｝）中的语句集都属于一个块，其中定义的变量在代码块外理论上是"不可见"的，我们称之为块级作用域。 但是，在es5之前没有块级作用域的的概念,只有函数作用域，现阶段可以认为JavaScript没有块级作用域。
        - 即，条件/分支/循环语句中的｛...｝内定义的变量，外部都可以访问。只有函数中内｛...｝定义的变量，外部不能访问。
        - 即，除了函数之外，js没有块级作用域。
    3. 词法作用域
    变量的作用域是在定义时决定而不是执行时决定，也就是说词法作用域取决于源码，通过静态分析就能确定，因此词法作用域也叫做静态作用域。
        - 在 js 中词法作用域规则:
            ○ 函数允许访问函数外的数据.
            ○ 整个代码结构中只有函数可以限定作用域.
            ○ 作用域规则首先使用提升规则分析
            ○ 如果当前作用规则中有名字了, 就不考虑外面的名字

        ```js
        var num = 123;
        function foo() {
            console.log( num );
        }
        foo();
        ​
        if ( false ) {
            var num = 123;
        }
        console.log( num ); // undefiend
        ```

- 作用域链
    - `只有函数可以制造作用域结构,形成新的作用域`， 那么只要是代码，就至少有一个作用域, 即全局作用域。凡是代码中有函数，那么这个函数就构成另一个作用域。如果函数中还有函数，那么在这个作用域中就又可以诞生一个作用域。
    - 将这样的所有的作用域列出来，可以有一个结构: 函数内指向函数外的链式结构。就称作作用域链。
    - script标签里面称为0级作用域；函数（嵌套）产生的以此为：1、2、3...级作用域。n级作用域优先使用n级作用域内定义的变量，若没有，依次查找n-1、n-2...
    - `多个script便签里面的变量会分段，彼此不干扰???`。
    
    ```js
    // 案例1：
    function f1() {
       function f2() {
       }
    }
    var num = 456;
    function f3() {
       function f4() {    
       }
    }
    ```

    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy04dcz3j20lr07fmxq.jpg)

    ```js
    // 案例2
    function f1() {
       var num = 123;
       function f2() {
           console.log( num );
       }
       f2();
    }
    var num = 456;
    f1();
    ```

    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy0hl5a3j20l9084js3.jpg)

- 预解析
    - JavaScript代码的执行是由浏览器中的JavaScript解析器来执行的。JavaScript解析器执行JavaScript代码的时候，分为两个过程：`预解析过程`和`代码执行过程`
    - 预解析过程+举例：
        a. 把`变量的声明`提升到`当前作用域`的最前面，只会提升声明，`不会提升赋值`。
        b. 把`函数的声明`提升到`当前作用域`的最前面，只会提升声明，`不会提升调用`。
        c. `多个script便签里面的变量会分段`，预解析时`彼此不干扰`。
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy4k0wkbj20aa09bdg3.jpg)
        d. `var变量提升比function更靠前`。
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy4s5k72j209q03qmxa.jpg)
        e. 更复杂的案例：
            `隐式全局变量+预编译`
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy51e7txj206w08p3yl.jpg)
            `函数表达式-预编译`
            ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy56k2q4j20aj02t3yj.jpg)

### 闭包

- 闭包概述
    - 定义:闭包（Closure）,又称词法闭包（Lexical Closure）或函数闭包（function closures），是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。所以，有另一种说法认为闭包是由函数和与其相关的引用环境组合而成的实体。
    - 解析1:函数可以嵌套，如果内部的函数引用了外部的函数的变量，一旦外部函数被执行，一个闭包就形成了，闭包中包含了内部函数的代码，以及所需外部函数中的变量的引用(声明而已)。其中所引用的变量称作上值(upvalue)。
    - 解析2:一个函数执行完毕之后,相关变量/数据(环境)就会被释放.但是若里面还有子函数(被父函数返回给外部),且子函数引用了父函数的数据,那么,子函数将会和其相关引用环境组合成一个实体,一同存在,不会释放(缓存数据,延长作用域链),哪怕父函数执行完毕.
    - 作用:`缓存数据, 延长作用域链`
        ○ 优点:`缓存数据`
        ○ 缺点:`缓存数据,没有及时释放`
    
    ```js
    //闭包小例子--缓存数据
    function f1() {
        var num = 10;
        return function () {
            num++;//闭包中的变量num变量一直存在
            return num;
        }
    }
    var ff = f1();
    console.log(ff());//11
    console.log(ff());//12
    console.log(ff());//13
    ```

- 闭包模式
    - 函数模式的闭包(函数中有函数);

        ```js
        //函数模式的闭包
        function A() {
            var num = 10;
            return function () {
                console.log(num);
                return num;
            }
        }
        var ff = A();
        var result = ff();
        console.log(result);
        ```

    - 对象模式的闭包(函数中有对象).

        ```js
        //对象模式的闭包
        function A() {
            var num = 10;
            return {
                age: num
            }
        }
        var obj = A();
        console.log(obj.age);
        ```

- 闭包案例-点赞应用
    如图:实现分别点赞/计数.
    ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzoy9b2d02j20jc01q752.jpg)
    
    ```js
    //闭包缓存数据
    function getValue() {
        var value = 2;
        return function () {
            //每次点击时,改变当前按钮的value值
            this.value = "赞(" + (value++) + ")";
        }
    }

    //获取所有的按钮
    var btnObjs = document.getElementsByTagName("input");
    for (var i = 0; i < btnObjs.length; i++) {
        btnObjs[i].onclick = getValue();
    }
    //如果不使用闭包缓存数据的话,各个按钮的value值是相关联的(累加).
    ```

### 沙箱(自调用函数)

- 自调用函数
    - 定义-自调用函数为:声明函数的同时便调用了
    - 作用: 里面的变量都是局部变量/临时变量;
    - 创建方式
        ○ `(function () {})()`;
        ○ `(function () {}())`;  推荐这种
- 沙箱
    - 沙箱(Sandbox)为一种虚拟技术,通过虚拟创建一个独立的空间,该空间内的操作不会影响外部.
    - 优点:
        ○ 节约内存空间: 全局变量只有在手动删除或者页面关闭才会释放,而沙箱中使用的是局部变量,执行完自动释放;
        ○ 沙箱内的局部变量不会和外部变量产生冲突
    - `Note`: 
        ○ 沙箱内部可以访问外部的变量,外部不可以访问沙箱内部的变量.
        ○ `以后的代码应该在各自的沙箱中编写`.
- 例子

    ```js
    var num = 100;
    (function () {
        var num = 10;
        console.log(num);
    }());
    console.log(num);
    ```

### 函数递归

- 函数递归
    - 定义: 函数中调用函数自己;
    - 注意: 
        ○ 函数递归要有结束条件;
        ○ 前端一般在变量DOM树时使用;
        ○ 递归的效率低,谨慎使用.

- 递归小例子
    1. 注意i的值;

        ```js
        var i = 0;
        function f() {
            i++;
            if (i < 5) {
                f();
            }
            console.log(i);//递归完成后,才执行
        }
        f(); //五个5
        ```

    2. 计算N个数的和 -- 计算阶乘(factorial) 类似

        ```js
        function getSum(n) {
            if (n == 1) {
                return 1;
            }
            return n + getSum(n - 1);
        }
        console.log(getSum(100));
        ```

    3. 求斐波那契数列某项的值
    
        ```js
        //求斐波那契数列
        function getFib(n) { //第n位的Fib数是多少
            if (n == 1 || n == 2) {
                return n;
            }
            return getFib(n - 1) + getFib(n - 2);
        }
        ```

### 深/浅拷贝-递归应用

- 深/浅拷贝介绍
    - 深浅拷贝只针对于想Object, Array这样的引用数据类型有效; 对于String Number等数据类型不存在这个概念.
    - 浅拷贝是对引用数据类型的地址进行拷贝,并没有在堆中开辟新的空间.
    - 深拷贝则是对引用类型中的所有的数据(哪怕引用类型数据里面含有多级引用类型数据)递归的重新开辟新的空间.
- 浅拷贝示例
    - 只把引用类型数据的第一级数据进行赋值拷贝.

    ```js
    var obj1 = {
        age: 10,
        sex: "男",
        car: ["奔驰", "宝马", "特斯拉", "奥拓"]
    };
    //另一个对象
    var obj2 = {};

    //写一个函数,作用:把一个对象的属性复制到另一个对象中,浅拷贝
    //把a对象中的所有的属性复制到对象b中
    function extend(a, b) {
        for (var key in a) {
            b[key] = a[key];
        }
    }
    extend(obj1, obj2);
    console.dir(obj2);//开始的时候这个对象是空对象
    console.dir(obj1);//有属性
    ```

- 深拷贝示例
    - 把引用类型数据中所有级别的数据都递归地进行赋值拷贝.

    ```js
    var obj1 = {
        age: 10,
        sex: "男",
        car: ["奔驰", "宝马", "特斯拉", "奥拓"],
        dog: {
            name: "大黄",
            age: 5,
            color: "黑白色"
        }
    };

    var obj2 = {};//空对象

    //通过函数实现,把对象a中的所有的数据深拷贝到对象b中
    function extend(a, b) {
        for (var key in a) {
            //先获取a对象中每个属性的值
            var item = a[key];
            //判断这个属性的值是不是数组
            if (item instanceof Array) {
                //如果是数组,那么在b对象中添加一个新的属性,并且这个属性值也是数组
                b[key] = [];
                //调用这个方法，把a对象中这个数组的属性值一个一个的复制到b对象的这个数组属性中
                extend(item, b[key]);
            } else if (item instanceof Object) {//判断这个值是不是对象类型的
                //如果是对象类型的,那么在b对象中添加一个属性,是一个空对象
                b[key] = {};
                //再次调用这个函数,把a对象中的属性对象的值一个一个的复制到b对象的这个属性对象中
                extend(item, b[key]);
            } else {
                //如果值是普通的数据,直接复制到b对象的这个属性中
                b[key] = item;
            }
        }
    }

    extend(obj1, obj2);
    console.dir(obj1);
    console.dir(obj2);
    ```

### 遍历DOM树-递归应用

- 节点的三个属性回顾
    - 节点类型nodeType:
        ○ 1代表标签节点,
        ○ 2代表属性节点,
        ○ 3代表文本节点
    - 节点名称nodeName:
        ○ 标签节点--大写的标签名字,
        ○ 属性节点---小写的属性名字,
        ○ 文本节点---#text
    - 节点的值nodeValue:
        ○ 标签节点---null,
        ○ 属性节点---属性的值,
        ○ 文本节点---文本内容

- 遍历代码

    ```js
    //获取页面中的根节点--根标签
    var root = document.documentElement;//html
    //函数遍历DOM树
    //根据根节点,调用fn的函数,显示的是根节点的名字
    function forDOM(root1) {
        //调用showNodeName,显示的是节点的名字
        // showNodeName(root1);
        //获取根节点中所有的子节点
        var children = root1.children;
        //调用遍历所有子节点的函数
        forChildren(children);
    }

    //给我所有的子节点,我把这个子节点中的所有的子节点显示出来
    function forChildren(children) {
        //遍历所有的子节点
        for (var i = 0; i < children.length; i++) {
            //每个子节点
            var child = children[i];
            //显示每个子节点的名字
            showNodeName(child);
            //判断child下面有没有子节点,如果还有子节点,那么就继续的遍历
            child.children && forDOM(child);//等价于if-else
            //||、&&、!!短路运算符的使用
            // ||从左到右,依次计算所有表达式,直到为布尔值true,并返回第一个为布尔值为true的表达式的值.
            // &&从左到右,依次计算所有表达式,直到为布尔值false,并返回第一个为布尔值为false的表达式的值.
            // !!用于把其他类型转换为布尔类型,如 !!5 === true
        }
    }

    //函数调用,传入根节点
    forDOM(root);

    function showNodeName(node) {
        console.log("节点的名字:" + node.nodeName);
    }
    ```

## 正则表达式

### 创建RE对象

- 一句话概括
    - 正则表达式不过是: 大括号, 中括号 小括号; 
    - 书写原则: 找规律 - 不要追求完美
- 复杂的正则解析

    ```js
    var reg = /(?:x)/; //非捕获组 - 
    var reg = /x(?=y)/; //x后面必须紧跟着y,才匹配x - 正向肯定查找
    var reg = /x(!?=y)/; //x后面必须不紧跟着y,才匹配x - 正向否定查找
    var reg = /x(?=y)/; //x前面必须紧跟着y,才匹配x - 反向肯定查找-JS不支持
    var reg = /x(!?=y)/; //x前面必须不紧跟着y,才匹配x - 反向否定查找-JS不支持
    var reg = /([a-z])\1{1,2}/; //小写字母,而且,重复出现2到3词,如 aab foo
    ```

- JS创建RE对象
    - 方法一:构造函数方式创建RE对象

        ```js
        var reg = new RegExp(/\d{5}/);
        // var reg = new RegExp("\\d{5}");
        // var reg = new RegExp("\\d\{5\}");
        //JS的正在放在/ /之间,类似于Python的 r"" , 里面的正则表达式不需要额外JS语言转义(JS转义 + RE转义).即/ /之间直接写正则表达式即可.否则的话,如果传入字符串,字符串的字符需要考虑JS和RE的两层转义, 如 "\\d" 代表 /\d/
        var flag = reg.test("我的电话是10086");
        console.log(flag);
        ```

    - 方法二:字面量方式创建RE对象(推荐)

        ```js
        var reg = /\d{1,5}/; //创建对象
        var flag = reg.test("我的电话是10086"); //使用RE对象的方法
        console.log(flag);
        ```

- Flag标志
    - i 忽略大小写
    - g 全局匹配,不使用g只匹配一个
    - m 多行,会影响 ^& 元字符
    - gi 全局匹配+忽略大小写

### JS中RE对象的属性

S中RE对象默认具有一些属性

```js
var reg = /\w/gim;
console.log(reg.global); //是否全局搜索
console.log(reg.ignoreCase); //是否大小写敏感
console.log(reg.multiline); //是否多行搜索
//global, ignoreCase, mutiline 三个属性是只读的,默认都是false
console.log(reg.source); // \w 正则表达式的文本字符串
console.log(reg.lastIndex); //当前表达式匹配内容的最后一个字符的下一个位置,即,下一次搜索的开始位置
```

### JS中RE相关方法

#### JS中RE相关的方法

- RE可以被用于:
    - `RegExp`对象的`exec`和`test`方法;
    - `String`的`match`、`replace`、`search`和`split`方法
- 验证字符串是否匹配: `test`或`search`方法；
- 获取匹配的内容: `exec`或`match`方法。

#### JS中RE的反向引用

- `$1` - 用于替换,如`String`的`replayce`方法中,如: `replace(reg, '$3-$1-$2')`;
- `\1` - 用于正则表达式当中,如: `/(\w{3}) is \1/`

#### ReExp对象中RE相关方法

1. test方法:`RegExp.prototype.test(str)`
    - 作用: 测试字符串参数中是否存在匹配正在表达式模式的字符串;
    - 返回值: 存在--返回true; 否则返回false.

    ```js
    var reg1 = /\w/; //无g标志--常用
    console.log(reg1.test("ab"), reg1.lastIndex); //true 0 下一个索引还是从0开始
    console.log(reg1.test("ab"), reg1.lastIndex); //true 0 同上
    console.log(reg1.test("ab"), reg1.lastIndex); //true 0 同上

    var reg2 = /\w/g; //有g标志
    console.log(reg2.test("ab"), reg2.lastIndex); //true 1 索引为0的位置开始查找成功,下一个索引从1开始
    console.log(reg2.test("ab"), reg2.lastIndex); //true 2 下一个索引从2开始
    console.log(reg2.test("ab"), reg2.lastIndex); //false 0 索引为2的位置开始查找失败,下一个索引从0开始
    console.log(reg2.test("ab"), reg2.lastIndex); //true 1 
    ```

2. exec方法:`RegExp.prototype.exec(str)`
    - 作用:使用RE模式对字符串执行搜索,并更新全局RegExp对象属性以反映匹配结果.
    - 返回值: 没有匹配到文本-返回null; 否则返回结果数组.
    - 返回的数组有如下特性:
        - 数组的内容: 
            § 第一项为匹配到的文本(`非全局模式为第一个匹配到的文本; 全局模式下需要遍历`);
            § 第二项为正则表达式中第一个组的内容(如果有的话);
            § 第三项为正则表达式中第二个组的内容(如果有的话)
            § 以此类推...
        - 数组的两个属性:
            § index: 存储匹配文本的第一个字符的位置;
            § input:存放被检索的string
    1. 不开启g模式(返回数组第一项为第一个匹配到的内容),`效果同exec方法不开启g模式`
    
        ```js
        //1. 非全局调用
        var reg3 = /\d(\w)(\w)\d/; //非全局,两个分组
        var ts = "$1az2bb3cy4dd5ee";
        var ret = reg3.exec(ts);
        console.log(reg3.lastIndex, ret.index, ret); // 0 1 ["1za2","a","z"]
        console.log(reg3.lastIndex, ret.index, ret); // 0 1 ["1za2","a","z"]
        //lastIndex=0表示下次还是从index=0开始搜索(或者说无效);
        //index=1表示匹配到的字符从index=1开始.
        //返回的数组第一项为第一个个匹配到的文本:"1za2"
        //返回的数组从第二项开始为第1组/第2组...的内容.
        //两次的输出结果一样,说明每次都是从字符串开头找.
        ```

    2. 开启g模式(返回数组第一项根据遍历过程而不同)
    
        ```js
        //2. 全局调用
        var reg4 = /\d(\w)(\w)\d/g; //非全局,只有一个分组
        var ts = "$1az2bb3cy4dd5ee";
        while (ret = reg4.exec(ts)) {
        console.log(reg4.lastIndex, ret.index, ret);
        // 5 1 ["1az2", "a", "z"]
        // 11 7 ["3cy4", "c", "y"]
        };
        //可见,全局模式下,lastIndex是记忆的,
        ```

#### String中RE相关方法

1. search方法: String.prototype.search(regexp)
    - 作用: 在字符串中测试匹配的String方法，
    - 返回值: 返回匹配到的位置索引，或者在失败时返回-1。
    - 它将忽略标志g。同时忽略 regexp 的 lastIndex 属性，并且总是从字符串的开始进行检索。

    ```js
    console.log("1a2b3c4d".search(/1/)); //0 匹配到,在index=1的位置
    console.log("1a2b3c4d".search(1)); //0 自动尝试把非正则参数转换为正则
    console.log("1a2b3c4d".search(/5/)); //-1 没有匹配到
    ```

2. match方法:String.prototype.match(regexp|str)
    - 作用:方法可在字符串内检索指定的值，或找到一个或多个正则表达式的匹配。
    - 参数可以是RE对象,或者字符串
    - 返回值:
        - 参数为字符串的话:匹配不成功: 返回null;
        - 匹配成功:
            □ 返回数组;
            □ 数组内容只有一个元素 -- 第一个匹配的内容; 
            □ 每次都重新匹配;

            ```js
            ret = "secarcasech".match("ca");
            console.log(ret, ret.index, ret.input); // ["ca"] 2 "secarcasech"
            ```

        - 参数为RE对象的话:匹配不成功:返回null;
        - 匹配成功:
            1. 不开启g模式,`效果同exec方法不开启g模式`;返回结果数组.返回的数组有如下特性:
        
            ```
            - 数组的内容: 
                > 第一项为匹配到的文本(非全局模式为第一个匹配到的文本; 全局模式下需要遍历);
                > 第二项为正则表达式中第一个组的内容(如果有的话);
                > 第三项为正则表达式中第二个组的内容(如果有的话)
                > 以此类推...
                > 每次都重新匹配(即, reObj.lastIndex = 0)
            - 数组的两个属性:
                > index: 存储匹配文本的第一个字符的位置;
                > input:存放被检索的string
            ```

            ```js
            var reg = /\d(\w)(\w)\d/; //不开启g模式,两个分组
            var ts = "$1az2bb3cy4dd5ee";
            var ret = ts.match(reg);
            console.log(reg.lastIndex, ret.index, ret); // 0 1 ["1za2","a","z"]
            console.log(reg.lastIndex, ret.index, ret); // 0 1 ["1za2","a","z"]
            ```

            2. 开启g模式的话;

            ```
            > 返回数组;
            > 数组的内容为所有的匹配项组成的元素;
            > 数组没有index和input属性;
            > 每次都重新匹配(即, reObj.lastIndex = 0).
            ```

            ```js
            var reg = /\d(\w)(\w)\d/g; //开启g模式,两个分组
            var ts = "$1az2bb3cy4dd5ee";
            var ret = ts.match(reg);
            console.log(reg.lastIndex, ret.index, ret); //0 undefined ["1az2", "3cy4"]
            console.log(reg.lastIndex, ret.index, ret); //0 undefined ["1az2", "3cy4"]
            ```

3. split方法:String.prototype.split(separator,howmany)
    - 第一个参数为分隔符,可以是字符串或RE对象;
    - 第二个参数可选, 该参数可指定返回的数组的最大长度。
    - 返回值: 一个字符串数组

    ```js
    console.log("a1b2c3d4".split(/\d/));//["a", "b", "c", "d", ""]
    ```

4. replace方法: `String.prototype.replace(regexp/substr,replacement)`
    - 参数一:字符串或RE对象;(被替换)

    - 参数二:字符串或回调函数;

    - 返回值:新的字符串,原字符串不变.如果RE对象没有g标志(或参数1为字符串),只替换第一个,如果有g标志,全部替换.

    - `第二个参数为字符串时,且第一个参数为RE对象,可使用反向索引,如下`:
        ![](http://ww1.sinaimg.cn/large/48356ef5ly1fzozgfhv7hj208h04jq2y.jpg)

    - 第二个参数为回调函数时,该函数的参数为:

        | 变量名     | 代表的值                                                    |
        | ---------- | ------------------------------------------------------------ |
        | match      | 匹配的到的字符串(回调函数会逐个处理这些匹配到的字符串)       |
        | p1,p2, ... | 可选,第一个参数对应的分组(对应于上述的$1，$2...反向引用). 例如, 如果是用 /(\a+)(\b+)/这个来匹配， p1就是匹配的 \a+,  p2 就是匹配的 \b+。 |
        | index      | 匹配到的子字符串在原字符串中的索引(或者叫偏移量)。           |
        | string     | 被匹配的原字符串, Note:   replace不会改变原字符串.           |

        ```js
        //第一个参数为字符串,其实隐式的转换为RE对象,默认不开启g模式.
        console.log("aa1b2c3d4".replace("a", "$1$1")); //Aa1b2c3d4 只替换第一个
        console.log("aa1b2c3d4".replace("a", function (params) {
            return params + "A";
        })); // 第一个参数为字符串,也可以使用回调函数
        
        console.log("aa1b2c3d4".replace(/\d/, "A")); //aaAb2c3d4 只替换第一个
        console.log("aa1b2c3d4".replace(/\d/g, "A")); //aaAbAcAdA 全部替换
        
        //参数为回调函数
        console.log("aa1b2c3d4e5".replace(/(\d)(\w)(\d)/g, function (match, group1, group2, group3, index, originStr) {
            console.log(match, index, originStr);
            return parseInt(group1) + parseInt(group3) + 1;
        }));
        //1b2 2 aa1b2c3d4e5
        //3d4 6 aa1b2c3d4e5
        //aa4c8e5
        ```

#### 反向引用

- String的replace方法中的反向引用 -- $n
- 正则表达式本身的反向引用 -- \n
- 其他地方的调用分组信息 -- RegExp.$n

```js
//提取这里的日
var str = "2017-11-12";
var array = str.match(/(\d{4})[-](\d{2})[-](\d{2})/g);
//console.log(array);
//正则表达式对象.$3
console.log(RegExp.$3);
```

### RE案例

- 案例-RE验证密码强弱

```js

//获取文本框注册键盘抬起事件
my$("pwd").onkeyup = function () {
    //每次键盘抬起都要获取文本框中的内容,验证文本框中有什么东西,得到一个级别,然后下面的div显示对应的颜色
    //如果密码的长度是小于6的,没有必要判断
    //巧妙的利用的类名称和getLvl函数返回值之前的关系
    // if(this.value.length>=6){
        // var lvl= getLvl(this.value);
        // my$("strengthLevel").className="strengthLv"+lvl;
    // }else{
        // my$("strengthLevel").className="strengthLv0";
    // }
    my$("strengthLevel").className = "strengthLv" + (this.value.length >= 6 ? getLvl(this.value) : 0);
};

//给我密码,我返回对应的级别
function getLvl(pwd) {
    var lvl = 0;//默认是0级
    //密码中是否有数字,或者是字母,或者是特殊符号
    if (/[0-9]/.test(pwd)) {
        lvl++;
    }
    //判断密码中有没有字母
    if (/[a-zA-Z]/.test(pwd)) {
        lvl++;
    }
    //判断密码中有没有特殊符号
    if (/[^0-9a-zA-Z_]/.test(pwd)) {
        lvl++;
    }
    return lvl;//最小的值是1,最大值是3
}
```

- 案例-RE验证输入的是否是邮箱

```js
//如果输入的是邮箱,那么背景颜色为绿色,否则为红色
//获取文本框,注册失去焦点的事件
document.getElementById("email").onblur = function () {
    //判断这个文本框中输入的是不是邮箱
    var reg = /^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/;
    if (reg.test(this.value)) {
        this.style.backgroundColor = "green";
    } else {
        this.style.backgroundColor = "red";
    }
};
```

- 案例-验证输入的是不是中文

```js
//是中文名字,则绿色,否则红色
document.getElementById("userName").onblur = function () {
    var reg = /^[\u4e00-\u9fa5]{2,6}$/;
    // var reg = /^[一-龥]{2,6}$/; //这种写法亦可
    if (reg.test(this.value)) {
        this.style.backgroundColor = "green";
    } else {
        this.style.backgroundColor = "pink";
    }
};
```

- 案例-验证表单

**html代码**

```html
<div class="container" id="dv">
    <label for="qq">Q Q</label><input type="text" id="qq"><span></span><br/>
    <label>手机</label><input type="text" id="phone"><span></span><br/>
    <label>邮箱</label><input type="text" id="e-mail"><span></span><br/>
    <label>座机</label><input type="text" id="telephone"><span></span><br/>
    <label>姓名</label><input type="text" id="fullName"><span></span><br/>
</div>
```

**js代码**

```js
//qq的
checkInput(my$("qq"),/^\d{5,11}$/);
//手机
checkInput(my$("phone"),/^\d{11}$/);
//邮箱
checkInput(my$("e-mail"),/^[0-9a-zA-Z_.-]+[@][0-9a-zA-Z_.-]+([.][a-zA-Z]+){1,2}$/);
//座机号码
checkInput(my$("telephone"),/^\d{3,4}[-]\d{7,8}$/);
//中文名字
checkInput(my$("fullName"),/^[\u4e00-\u9fa5]{2,6}$/);

//给我文本框,给我这个文本框相应的正则表达式,我把结果显示出来
//通过正则表达式验证当前的文本框是否匹配并显示结果
function checkInput(input,reg) {
    //文本框注册失去焦点的事件
    input.onblur=function () {
        if(reg.test(this.value)){
            this.nextElementSibling.innerText="正确了";
            this.nextElementSibling.style.color="green";
        }else{
            this.nextElementSibling.innerText="让你得瑟,错了吧";
            this.nextElementSibling.style.color="red";
        }
    };
}
```

### RE作弊单

[RE CheatSheet](http://tool.oschina.net/uploads/apidocs/jquery/regexp.html)

## 伪数组/数组

### 对象和数组的区别

- JS中所有内置构造函数都继承自Object.prototype, 即Array构造函数(也是对对象)的__proto__指向Object.prototype对象; 
- 即new Array() 或[] 创建的数组对象同时具有Object.prototype的属性和Array.prototype的属性;
- 而new Object 或 {} 创建的对象 只具有Object.prototype的属性.
- 数组是基于索引的实现,length与最懂更新. 而对象是键值对.

### 如何判断是否是伪数组

1. fakeArray instanceof Array;
2. Object.prototype.toString.call(fakeArray )
3. Array.isArray(fakeArray)
    - 真数组的长度是可变的,伪数组的长度不可变
    - 真数组可以使用数组中的方法, 伪数组不可以使用数组中的方法
    - JS中伪数组的length不能自动增减.

### 伪数组存在的意义

伪数组(将具有length属性的对象)虽然不能直接使用数组方法,但是可以间接的使用大多数数组的方法.

```js
//间接的使用数组的方法
var arr = Array.prototype.slice.call(arguments)
//或者
var arr = Array.prototype.slice.call(arguments, 0); // 将arguments对象转换成一个真正的数组
Array.prototype.forEach.call(arguments, function (v) {
    // 循环arguments对象
});

//除了使用 Array.prototype.slice.call(arguments)，你也可以简单的使用[].slice.call(arguments) 来代替。另外，你可以使用 bind 来简化该过程。

var unboundSlice = Array.prototype.slice;
var slice = Function.prototype.call.bind(unboundSlice);
function list() {
    return slice(arguments);
}
var list1 = list(1, 2, 3); // [1, 2, 3]
```

### 对象实现伪数组

```js
//对象实现一个伪数组
var fakeArray = {
    0: 10,
    1: 20,
    2: 30,
    length: 3
};
```

### JS中常见的伪数组

- 函数内部的 `arguments`
- DOM 对象列表（比如通过 `document.getElementsByTags/ childNodes`得到的列表）
- jQuery 对象（比如 `$("div")` ）


## JS垃圾回收机制
## JS运行机制:Event Loop
## Object

- 静态成员
    - Object.assign()
    - Object.create()
    - Object.keys()
    - Object.defineProperty()
- 实例成员
    - constructor
    - hasOwnProperty()
    - isPrototypeOf
    - propertyIsEnumerable()
    - toString()
    - valueOf()

## 附录

- 代码规范
    - 代码风格
    - JavaScript Standard Style 
    - Airbnb JavaScript Style Guide() {
    - 校验工具
    - JSLint
    - JSHint
    - ESLint
- [Chrome 开发者工具](https://www.html.cn/doc/chrome-devtools/)
- 文档相关工具
    - 电子文档制作工具: docsify/docute, i5ting_toc(本地MD生成HTML)
    - 流程图工具：ProcessOn/百度脑图 


