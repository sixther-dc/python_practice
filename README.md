<!-- <cf-dnd-list  options="$root.favoriteEndpoints" template-url ="src/framework/cf-ui-components/cf-newservicelist/collectionList.html"></cf-dnd-list> -->
<ul class="cf-sidebar-collection-service">
    <li class="cf-sidebar-service-row" ng-style="{'transform': 'translate3d(0px,' + 40 * $index +'px, 0px)'}"
        ng-repeat="favoriteEndpoint in $root.favoriteEndpoints" hws-href href="{{favoriteEndpoint.endpoint}}"
        ng-attr-title="{{favoriteEndpoint.name}}">
        <a class="cf-sidebar-service-item">
            <span class="cf-sidebar-service-icon"
                ng-class="'hwsicon-frame-service-'+favoriteEndpoint.serviceCss"></span>
            <span class="cf-sidebar-service-name" id="{{favoriteEndpoint.tipsElementId}}"
                ng-bind="favoriteEndpoint.name"></span>
            <span class="cf-sidebar-toolbar">
                <span class="icon-cloud-action-cross cf-sidebar-remove"></span>
                <span class="icon-cloud-action-gridlines cf-sidebar-drag"></span>
            </span>
        </a>
    </li>
</ul>

<script>
    setTimeout(function () {
        $(".cf-sidebar-service-item").hover(function () {
            $(this).children(".cf-sidebar-toolbar").css("display", "inline-block");
            if ($('#cf-service-sidebar').hasClass('cf-sidebar-mini')) {
                $('#cf-service-sidebar').removeClass('cf-sidebar-mini');
            }
        }, function () {
            $(this).children(".cf-sidebar-toolbar").css("display", "none");
            if (!$('#cf-service-sidebar').hasClass('cf-sidebar-mini')) {
                // $('#cf-service-sidebar').addClass('cf-sidebar-mini');
            }
        })

        $(".cf-sidebar-drag").mousedown(function () {
            var ulEle = $(this).parent().parent().parent();
            ulEle[0].style.zIndex = 101;
            var eleTop = $(ulEle).offset().top;
            //记录首次位移的方向
            var firstMove;
            //用户移动方向开关，用于控制上移一般又下移的场景（反之亦然）
            var moveFlag;
            //获取li的元素集合
            var liList = $($(".cf-sidebar-collection-service")[0]).children("li");
            //获取当前li的序号
            var currentEleIndex = liList.index(ulEle);
            //记录当前元素显示的位置序号
            var currentEleDisplayIndex = currentEleIndex;
            var currentEleDisplayOffsetTop = eleTop + 20;
            document.onmousemove = function (e) {
                var event = e || window.event;
                var pageY = event.pageY;
                $(ulEle).offset({
                    top: pageY - parseInt(getComputedStyle(ulEle[0],
                        null).height) / 2
                });
                //处理下移
                if (((pageY - currentEleDisplayOffsetTop) > 20) && (currentEleDisplayIndex < liList
                        .length - 1)) {
                    if (!firstMove) {
                        firstMove = 'down'
                    }
                    //移动超过半个身位，基准点加一个身位， 基准点为元素的中间高度
                    currentEleDisplayOffsetTop += 40;
                    if (moveFlag !== "up") {
                        currentEleDisplayIndex += 1;
                    }
                    if (firstMove === "up") {
                        var nextEleTransformY = (currentEleDisplayIndex + 1) * 40;
                    } else {
                        var nextEleTransformY = currentEleDisplayIndex * 40;
                    }
                    if (currentEleDisplayIndex !== currentEleIndex) {
                        $(liList[currentEleDisplayIndex]).css({
                            'transform': 'translate3d(0px, ' + (parseInt(
                                    nextEleTransformY) -
                                    40) +
                                'px, 0px)'
                        })
                    }
                    moveFlag = "down";
                }
                //处理上移
                if ((currentEleDisplayOffsetTop - pageY) > 20 && (currentEleDisplayIndex > 0)) {
                    if (!firstMove) {
                        firstMove = 'up'
                    }
                    currentEleDisplayOffsetTop -= 40;
                    if (moveFlag !== "down") {
                        currentEleDisplayIndex -= 1;
                    }
                    console.log(currentEleDisplayIndex);
                    if (firstMove === "down") {
                        var nextEleTransformY = (currentEleDisplayIndex - 1) * 40;
                    } else {
                        var nextEleTransformY = currentEleDisplayIndex * 40;
                    }
                    if (currentEleDisplayIndex !== currentEleIndex) {
                        $(liList[currentEleDisplayIndex]).css({
                            'transform': 'translate3d(0px, ' + (parseInt(
                                        nextEleTransformY) +
                                    40) +
                                'px, 0px)'
                        })
                    }
                    moveFlag = "up"
                }
            };
            document.onmouseup = function () {
                document.onmousemove = null;
                ulEle[0].style.zIndex = 100;
                //这里修改拖动元素的translate3d值以及做具体的位移， 同时需要清除top属性
            }
        })

        function cuteHide(el) {
            el.animate({
                opacity: '0'
            }, 150, function () {
                el.animate({
                    height: '0px'
                }, 150, function () {
                    el.remove();
                });
            });
        }

        $(".cf-sidebar-remove").click(function () {
            cuteHide($(this).parent().parent().parent());
        })

    }, 1000)
</script>
