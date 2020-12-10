function init () {
    /**
     * Создаем мультимаршрут.
     * @see https://api.yandex.ru/maps/doc/jsapi/2.1/ref/reference/multiRouter.MultiRoute.xml
     */
    var multiRoute = new ymaps.multiRouter.MultiRoute({
        referencePoints: [
            addrFrom,
            addrTo
        ],
        params: {
            routingMode: 'masstransit',
            avoidTrafficJams: true,

        }
    }, {
        wayPointDraggable: true,
        boundsAutoApply: true
    });

    ymaps.modules.require([
        'MultiRouteColorizer'
    ], function (MultiRouteColorizer) {
        new MultiRouteColorizer(multiRoute);
    });

    var myMap = new ymaps.Map('map', {
        center: [55.739625, 88.54120],
        zoom: 12,
    });

    myMap.geoObjects.add(multiRoute);
}

ymaps.ready(init);
