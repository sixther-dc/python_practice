# python_practice

# eventlet 创建TCP链接用于client跟server交互
# Rlock不知道用于什么
# zookeeper注册了很多时间不知道是做了什么


const webpack = require('webpack');
const webpackDevMiddleware = require("webpack-dev-middleware");
const webpackHotMiddleware = require('webpack-hot-middleware');
const webpackConfig = require('../webpack.config.js');
const express = require('express');
const open = require('open');

const app = express();
const compiler = webpack(webpackConfig);

app.use(webpackDevMiddleware(compiler, {

}));

app.use(webpackHotMiddleware(compiler, {
    log: console.log, 
    path: '/__webpack_hmr', 
    heartbeat: 10 * 1000
  }));

app.listen(3000, () => {
    console.log("Example app listening on port 3000!")
    open("http://localhost:3000/index.html")
})



const path = require("path");
const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    //支持多条打包路径
    entry: { 
        home : ['webpack-hot-middleware/client?path=/__webpack_hmr&reload=true', './src/index.js']
    },
    mode: 'development',
    devtool: 'inline-source-map',
    output: {
        //这里的name就是每条entry的key值，默认为main
        filename: '[name].js',
        path: path.resolve(__dirname, 'dist'),
        sourceMapFilename: '[file].map'
        //libraryTarget: 'var',
        //library: 'xxxx',
    },
    resolve: {
        extensions: ['.js', '.json'],
        //Tell webpack what directories should be searched when resolving modules.
        modules: [
            'src',
            'lib',
            'node_modules'
        ],
        alias: {
            "angular" : path.resolve(__dirname, 'src/lib/angular')
        }
    },
    plugins: [
        // new webpack.ProvidePlugin({
        //     'windows.angular': 'angular'
        //   })

        new HtmlWebpackPlugin({
            template: './src/index.html',
            filename: 'index.html',
            inject: 'true'
        }),
        //实现实时刷新浏览器
        new webpack.HotModuleReplacementPlugin(),
    ],
    //将全局模块导出为conmmonjs格式
    module: {
        rules: [{
            test: /angular\.js$/, 
            loader: "exports-loader?angular" 
        }]
    }
}


{
  "name": "webapp",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "directories": {
    "lib": "lib"
  },
  "dependencies": {
    "webpack-cli": "^3.1.2",
    "webpack": "^4.26.0"
  },
  "devDependencies": {
    "exports-loader": "^0.7.0",
    "express": "^4.16.4",
    "html-webpack-plugin": "^3.2.0",
    "open": "0.0.5",
    "webpack-dev-middleware": "^3.4.0",
    "webpack-hot-middleware": "^2.24.3"
  },
  "scripts": {
    "test": "echo \"Error: no test specified\" ",
    "start": "node script/start.js"
  },
  "author": "",
  "license": "ISC"
}

