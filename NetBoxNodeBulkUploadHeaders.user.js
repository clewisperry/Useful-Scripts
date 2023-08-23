// ==UserScript==
// @name         NetBox Node Bulk Upload Headers
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://nautobot.service.dev.itauto.nvidia.com/dcim/devices/import/child-devices/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=nvidia.com
// @grant        none
//test update url
// ==/UserScript==

(function() {
    'use strict';

    let tarea = document.getElementById("id_csv_data")
    tarea.value="name,device_role,tenant,manufacturer,device_type,serial,status,parent,device_bay,cf_install_date,cf_purchase_order"
    tarea.style.width = "1310px"
})();
