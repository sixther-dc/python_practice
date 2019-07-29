/* global Rx */
const stage = document.getElementById("stage");
const context = stage.getContext('2d');
context.fillStyle = "green";

const PADDLE_WIDTH = 100;
const PADDLE_HEIGHT = 20;
const BALL_RADIUS = 10;
const BRICK_ROWS = 5;
const BRICK_COLUMNS = 7;
const BRICK_HEIGHT  = 20;
const BRICK_GAP  = 3;

//显示游戏说明
function drawIntro() {
    context.clearRect(0, 0, stage.width, stage.height);
    context.textAlign = "center";
    context.font = '24px Courier New';
    context.fillText("Press [<] and [>]", stage.width / 2, stage.height / 2);
}


//绘制球拍
function drawPaddle(position) {
    context.beginPath();
    context.rect(
        position - PADDLE_WIDTH / 2,
        stage.height - PADDLE_HEIGHT,
        PADDLE_WIDTH,
        PADDLE_HEIGHT
    );
    context.fill();
    context.closePath();
}

function drawBall(ball) {
    context.beginPath();
    context.arc(ball.position.x, ball.position.y, BALL_RADIUS, 0, Math.PI * 2);
    context.fill();
    context.closePath();
}

const PADDLE_SPEED = 240;
const PADDLE_POSATION = stage.width / 2;
let nextPaddlePosation = PADDLE_POSATION;
drawPaddle(PADDLE_POSATION)
const time$ = Rx.Observable
     //保持60hz的刷新率
    .interval(1000 / 60, Rx.Scheduler.requestAnimationFrame)
    .map(() => ({
        time: Date.now(),
        deltaTime: null 
    }))
    .scan((previous, current) => ({
        time: current.time,
        deltaTime: (current.time - previous.time) / 1000
    }))
    // .subscribe((value) => {
    //     nextPaddlePosation = nextPaddlePosation + value.deltaTime * PADDLE_SPEED;
    //     // context.clearRect(0, 0, stage.width, stage.height);
    //     // drawPaddle(nextPaddlePosation);
    // })


const PADDLE_CONTROLS = {
    'ArrowLeft': -1,
    'ArrowRight': 1
}
const keys$ = Rx.Observable
                .merge(
                    Rx.Observable.fromEvent(document, 'keydown').map(event => ( PADDLE_CONTROLS[event.key] || 0 )),
                    //释放按键
                    Rx.Observable.fromEvent(document, 'keyup').map(event => (0))
                )
                //对数据去重
                .distinctUntilChanged();

//结合时间流以及鼠标时间来控制球拍的位置
time$.withLatestFrom(keys$).subscribe(value => {
    nextPaddlePosation = nextPaddlePosation + value[0].deltaTime * PADDLE_SPEED * value[1];
    context.clearRect(0, 0, stage.width, stage.height);
    drawPaddle(nextPaddlePosation);
    drawBall(initState().ball);
});


const initState = () => ({
    ball: {
        position : {
            x: stage.width / 2,
            y: stage.height - PADDLE_HEIGHT - BALL_RADIUS
        }
    }
})


// drawBall(initState().ball)



let umdConfig = Object.assign({}, getCommonConfig(), {
    entry: entrys,
    output: {
        path: `${helpers.packageBuildPath}/main`,
        filename: '[name].js',
        libraryTarget: 'umd',
        library: '[name]',
        umdNamedDefine: true,
        chunkFilename: '[name].js'
    },
});

let globalConfig = Object.assign({}, getCommonConfig(), {
    entry: entrys,
    output: {
        path: `${helpers.packageBuildPath}/main`,
        filename: 'g[name].js',
        libraryTarget: 'window',
        // library: '[name]',
        // umdNamedDefine: true,
        chunkFilename: 'g[name].js'
    },
});
