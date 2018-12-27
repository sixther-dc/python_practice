define(['backend/backend', 'fruitProvider/config/fruit_config','framework/testmodule'], function (backend, fruit, test) {
    var dependency = [
        fruit.name,
        test.name
    ];
    var framework = angular.module("framework", dependency);
    //添加系统服务,
    //问题：然后其他模块就可以使用这个系统服务了吗？为什么
    framework.service("backend", backend);
    
    console.log("framework模块要启动了..");

    //定义一个provider
    var testProvider = function(){
        var baseUrl = "test";
        //一定要有$get方法
        this.$get = function() {
            return {
                baseUrl: baseUrl
            }
        }
    }

    framework.provider("test_provider", testProvider);
    //定义一个controller
    var testController = function($scope, $rootScope, test_for_module, test_provider) {
        $scope.testValue = "duanchao";
        $rootScope.testValue = "duanchao";
        console.log("I am parent controller");
        console.log(test_for_module + " from dependency module");
        console.log(test_provider.baseUrl + ' from privider');
    }

    testController.$injector = ["$scope", "$rootScope", "test_for_module", "test_provider"];

    framework.controller("testController", testController);

    //注意引用provider要添加Provider后缀
    framework.config(["test_providerProvider", function(test_provider){
        test_provider.baseUrl = "www.huawei.com"
    }])

    //可执行的语句执行完后编执行run方法
    framework.run([function(){
        console.log("run方法什么时候执行");
    }]);

    return framework
});



define([], function () {
    var testModule = angular.module("test_module", []);
    //添加系统服务,
    //问题：然后其他模块就可以使用这个系统服务了吗？为什么
    console.log("testModule模块要启动了..");
    testModule.value("test_for_module", "test_for_module");
    return testModule
});
