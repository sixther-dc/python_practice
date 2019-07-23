<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <div>
        <button id="hold-me">Click Me</button>
        <div>your time: <span id="hold-time"></span>ms</div>
        <div id="rank"></div>
        <div>
            <button id="getStar">getStar</button>
        </div>
        <div>
            <div id="text"></div>
        </div>
    </div>

</body>
<script src="../lib//rx.js"></script>
<script>
    class Producer {
        constructor() {
            this.listeners = [];
        }
        addListener(listener) {
            if (typeof listener === 'function') {
                this.listeners.push(listener)
            } else {
                throw new Error('listener 必須是 function')
            }
        }
        removeListener(listener) {
            this.listeners.splice(this.listeners.indexOf(listener), 1)
        }
        notify(message) {
            this.listeners.forEach(listener => {
                listener(message);
            })
        }
    }

    var egghead = new Producer();

    function listener1(message) {
        console.log(message + 'from listener1');
    }

    function listener2(message) {
        console.log(message + 'from listener2');
    }

    egghead.addListener(listener1);
    egghead.addListener(listener2);

    egghead.notify('A new course!!');
    egghead.notify('dc ');
/* 
        创建类
        转化类  map
                mapTo  转化为常量Observable
                pluck  针对字典类型的Observable，使用pluck将特定字段给拔出来 TODO: 常用场景，获取网页应用中的DOM事件的值，缺点是每次只能拔出一个属性
                bufferTime   把时间划分为连续的400毫秒的长度区块，其实是一个高阶的Observable
                bufferCount  根据数量来划分缓冲区
                bufferWhen   鸡肋
                bufferToggle
                buffer
                高阶map: 转换为Observable对象
                数据分组:
                    groupby: 依照定制参数的返回值作为key来分割数据， 跟window/buffer相比，groupby可以交叉的把数据传给下游‘
                             场景：　利用时间委托来对时间的元素进行分类，然后单独绑定事件处理函数
                    partition:  返回一个包含两个元素的数组，第一个是满足条件的Observable对象，第二个是不满足的
                累计数据：
                    scan: 可以处理一个永不完结的上游Observable对象，reducer则不能, scan可以保存当前状态
                    mergeScan：类似scan，只是规约函数返回的的是一个Observable对象， 未来可能会被废弃
        过滤类  filter
                first
                last
                take
                lakeLast
                skip
                throttleTime
                distnct
                single
                elementAt
        辅助类   count
                max
                min
                reduce(规约统计), 可以使用该方法来实现上述几种操作符
                every 判定操作， 不要对一个永不完结的Observable使用every操作符
                find  找到符合判定条件的数据
                findIndex   找到符合判定条件的数据的序号
                isEmpty
                defaultIfEmpty  如果上游是空的，则会返回参数中的数据
        合并类   concat  (收尾相连接) 
                merge （先到先得）
                zip(拉链机制， 两两配对，没有配对的数据将会被丢弃)  
                combineLatest(合并最后一个数据，不管哪个observable产生了数据，都会触发新的数据处理，可定制下游数据)
                withLatestFrom(产生给下游的数据由主触方触发， 然后结合所带的参数处理后传递给下游)
                race(胜者通吃， 以第一个产生数据的Observable为准，剩余的抛弃)
                startWith(可以使用concat实现，就是在数据流之前生成添加数据)
                forkJoin(相当于promise.All, 等待所有的Observable对象完结后获取最新的数据)
                高阶Observable（产生的数据依然是Observable的Observable）：
                    concatAll
                    mergeAll
                    zipAll
                    combileAll
                    switch (总是切换到最新的Observable去获取数据， 抢山头游戏)
                    exhaust (耗尽，在耗尽当前内部的Observable的数据之前不会切换到下一个内部Observable对象， 在中间生成的内部Observable对象将会被舍弃)
        多播类
        错误处理类
            catch     “恢复”， 使用一个正常数据来恢复数据流在遇到异常时
            retry
            retryWhen    控制重试的节奏， 会根据notifer返回的Observable对象来决定什么时候重试， 该Ob每吐出一个数据，就会重试一次
            finally
        条件分支类
        数学和合计类

        多播
            Subject类型：
                BehaviorSubject
                ReplaySubject
                AsyncSubject
            操作符：
                multicast
                publishLast
                publishReplay
                publishBehavior
        分为 实例操作符（原型链方法）  和   静态操作符号（静态方法）
    */

    const holdButtom = document.querySelector("#hold-me");
    const mouseDown$ = Rx.Observable.fromEvent(holdButtom, "mousedown");
    const mouseUp$ = Rx.Observable.fromEvent(holdButtom, "mouseup");

    //获得一个通过计算可以获取的流
    const holdTime$ = mouseUp$.timestamp().withLatestFrom(mouseDown$.timestamp(), (mouseUpEvent, mouseDownEvent) => {
        return mouseUpEvent.timestamp - mouseDownEvent.timestamp;
    });
    holdTime$.subscribe(ms => {
        document.querySelector("#hold-time").innerText = ms
    })
    // holdTime$.flatMap( ms => Rx.Observable.ajax("https://timing-sense-score-board.herokuapp.com/score/0" +ms))
    //     .map(e => e.response)
    //     .subscribe(res => {
    //         document.querySelector('#rank').innerText("res.rank");
    //     })
    //观察者模式
    //生产者，subscribe传入的console.log则是观察者
    const testSource$ = Rx.Observable.of(1, 2, 3);
    testSource$.subscribe(console.log);

    const onSubscribe = observer => {
        let number = 4;
        const handle = setInterval(() => {
            observer.next(number++);
            if (number > 6) {
                //错误状态也会终结整个数据流
                // observer.error("something wrong");
                clearInterval(handle);
                observer.complete();
            }
        }, 1000)
    }
    const testSource1$ = new Rx.Observable(onSubscribe);
    //此处可以直接使用create来替代处理，操作符
    const theObserver = {
        next: item => console.log(item),
        //TODO: 这里好像是生效了，但是对应的complete方法却没有执行
        complete: () => console.log("no more data"),
        error: err => console.error(err)
    };
    //两种写法都可以
    //.map会生成一个新的observable
    testSource1$.map(x => x * x).subscribe(console.log);
    // testSource1$.subscribe(theObserver);

    // Rx.Observable.fromEvent(document.querySelector("#getStar"), "click").subscribe(
    //     () => {
    //         console.log("getStar have been clicked");
    //         Rx.Observable.ajax('https://api.github.com/repos/ReactiveX/rxjs', {
    //             responseType: 'json'
    //         }).subscribe(
    //             value => {
    //                 console.log(value);
    //             }
    //         )
    //     }
    // )


    const notifier = () => {
        return Rx.Observable.interval(1000);
    }
    // Rx.Observable.of(1,3,3,4).repeatWhen(notifier).subscribe(console.log);


    const original$ = Rx.Observable.timer(0, 1000);
    const source1$ = original$.map(x => x + 'a');
    const source2$ = original$.map(x => x + 'b');
    const result$ = source1$.withLatestFrom(source2$, (a, b) => a + b);
    // result$.subscribe(console.log);

    //combineLatest和withLatestFrom
    const event$ = Rx.Observable.fromEvent(document.body, 'click');
    const x$ = event$.map(e => e.x);
    const y$ = event$.map(e => e.y);
    const result1$ = x$.withLatestFrom(y$, (x, y) => `x: ${x}, y: ${y}`);
    result1$.subscribe((location) => {
        console.log(location);
        document.querySelector("#text").innerHTML = location;
    })

    //高阶Observable
    Rx.Observable.interval(1000).take(2).map(x => Rx.Observable.interval(3000).map(y => x + ':' + y).take(2)).subscribe(
        ob => ob.subscribe(console.log))

    const ho$ = Rx.Observable.interval(1000).take(2).map(x=> Rx.Observable.interval(1000).map(y => x+':'+y).take(2)).concatAll()

    //计算1到100的和
    Rx.Observable.range(1,100).reduce((acc, current) => acc + current, 0).subscribe(console.log);

    //以4s为间隔缓存数据流中的数据，然后相应的处理函数中也需要做相应的处理
    Rx.Observable.timer(0, 1000).take(8).bufferTime(4000).subscribe(console.log)
    Rx.Observable.timer(0, 1000).take(8).bufferCount(4).subscribe(console.log)

    //按照奇偶数分流
    Rx.Observable.interval(1000).take(8).groupBy(x => x % 2).subscribe(s => {if(s.key == 1) {s.subscribe(console.log)}})

    //上游每输出一个值，则计算所有已经输出的值的合
    Rx.Observable.interval(100).take(10).scan((acc, value) => {return acc + value}).subscribe(console.log)



    //nodeJS 风格的回调函数， 缺陷是会引起“毁掉嵌套地狱”
    //const invalidJsonString = "NOT FOUND";
    const invalidJsonString = '{"name":"dc"}';
    const delayParse = (jsonString, callback) => {
        setTimeout(() => {
            try {
                const result = JSON.parse(jsonString);
                callback(null, result);
            } catch (error) {
                callback(error)
            }
        }, 100)
    }

    delayParse(invalidJsonString, (error, result) => {
        if(error) {
            console.error("catch error:", error);
            return
        }
        console.log(result);
    })

    //Promise的异常处理   预备状态（pending）  成功状态(fulfilled)  失败状态(rejected)  .then().catch() 支持链式调用，不支持重试

    //数据流中遇到异常怎么处理， 异常之后的数据将没有机会走向下游
    //caught$就是代表了上游的Observable对象
    Rx.Observable.range(1,5).map(value => {if(value == 4) {throw new Error("unlucky number 4")} return value}).catch((err, caught$) => Rx.Observable.of(8)).subscribe(console.log)

    //失败后每个三秒重试一次，总共重试一次
    Rx.Observable.range(1,5).map(value => {if(value == 4) {throw new Error("unlucky number 4")} return value}).retryWhen(err$ => Rx.Observable.interval(3000).take(2)).catch((err, caught$) => Rx.Observable.of(8)).subscribe(console.log)
    //每隔3秒重试一次
    // Rx.Observable.range(1,5).map(value => {if(value == 4) {throw new Error("unlucky number 4")} return value}).retryWhen(err$ => err$.delay(3000)).catch((err, caught$) => Rx.Observable.of(8)).subscribe(console.log)

    //TODO: 重试的本质是退订加上重新订阅


    //递增延时重试
    Rx.Observable.prototype.retryWithExpotentialDelay = function (maxRetry, initialDelay) {
        return this.retryWhen(
            err$ => {
                return err$.scan((errorCount, err) => {
                    if(errorCount >= maxRetry) {
                        throw err;
                    }
                    return errorCount + 1
                }, 0).delayWhen(errorCount => {
                    const delayTime = Math.pow(2, errorCount - 1) * initialDelay;
                    return Observable.timer(delayTime);
                })
            }
        )
    }

    //Hot Observable有 fromPromise  fromEvent  fromEventPattern 默认Hot实现的是多播，  Cold实现的是单播
    //如何把Cold变为Hot，   使用Subject
    const subject = new Rx.Subject();
    subject.map(x => x * 2).subscribe(
        value => console.log('on data: ' + value),
        err => console.log('on error: ' + err.message),
        () => console.log('on complete')
    )

    //subject有状态，会记住所有Observer的列表
    //使用subject将cold observable转换为 hot observable
    const tick$ = Rx.Observable.interval(1000).take(3);
    const subject1 = new Rx.Subject();
    tick$.subscribe(subject1);
    subject1.subscribe(value => console.log('observer 1: ' + value));
    setTimeout(() => {
        subject1.subscribe(value => console.log('observer 2: ' + value))
    }, 1500)

    //或者直接使用multicast来实现
    //tick$.multicast(new Rx.Subject())
    //支持subject的参数是为了提高multicast操作符的定制能力
</script>

</html>
