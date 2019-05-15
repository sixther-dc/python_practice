<!-- <cf-dnd-list  options="$root.favoriteEndpoints" template-url ="src/framework/cf-ui-components/cf-newservicelist/collectionList.html"></cf-dnd-list> -->
<ul class="cf-sidebar-collection-service">
        <li class="cf-sidebar-service-row" style="transform: translate3d(0px, 0px, 0px)" ng-repeat="favoriteEndpoint in $root.favoriteEndpoints" hws-href
            href="{{favoriteEndpoint.endpoint}}" ng-attr-title="{{favoriteEndpoint.name}}">
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
                    $('#cf-service-sidebar').addClass('cf-sidebar-mini');
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
    
    
    .cf-sidebar-service-wrapper {
    height: 40px;
    line-height: 40px;
    background-color: #FFFFFF;
    overflow: hidden;
    position: relative;
}

.cf-sidebar-service-wrapper:hover{
    cursor: pointer;
}

.cf-sidebar-collection-service {
    display: block;
    overflow: hidden;
    position: relative;
    height: 100%;
}

.cf-sidebar-collection-service:hover {
    background-color: #FFFFFF;
}
.cf-sidebar-service-icon {
    padding: 12px 15px;
    font-size: 16px;
    vertical-align: middle;
}
.cf-sidebar-service-row {
    height: 40px;
}

a.cf-sidebar-service-item {
    display: inline-block;
    height: 40px;
    width: 100%;
    overflow: hidden;
    text-decoration: none;
    color: #252B3A;
    white-space: nowrap;
}

a.cf-sidebar-service-item:hover{
    color:#526ECC;
    background-color: #F7F9FC;
    cursor: pointer;
}

.cf-sidebar-service-name {
    display: inline-block;
    height: 40px;
    line-height: 40px;
    width: 188px;
    vertical-align: middle;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap; 
}

.cf-sidebar-service-right-icon{
    position: absolute;
    right: 15px;
    top: 18px;
    display: inline-block;
    border-bottom: 4px solid transparent;
    border-left: 6px solid #252B3A;
    border-top: 4px solid transparent;
    content: '';
}

.cf-sidebar-mini .cf-sidebar-service-right-icon {
    display: none;
}

.cf-sidebar-toolbar {
    height: 40px;
    line-height: 40px;
    vertical-align: middle;
    position: absolute;
    right: 5px;
    background-color: #F7F9FC;
    display: none;
}

.cf-sidebar-mini .cf-sidebar-toolbar {
    display: none;
}

.cf-sidebar-drag {
    cursor: move;
}
