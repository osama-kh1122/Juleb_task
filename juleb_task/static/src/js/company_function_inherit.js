odoo.define('juleb_task.session', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.Session');
var ajax = require('web.ajax');
var concurrency = require('web.concurrency');
var core = require('web.core');
var local_storage = require('web.local_storage');
var mixins = require('web.mixins');
var utils = require('web.utils');
var mobile = require('web_mobile.rpc');
var rpc = require('web.rpc');

console.log("yesssssssssssssssssssssss")

session.include({

    /**
     * @override
     */
   setCompanies: function (main_company_id, company_ids) {
        var hash = $.bbq.getState()
        hash.cids = company_ids.sort(function(a, b) {
            if (a === main_company_id) {
                return -1;
            } else if (b === main_company_id) {
                return 1;
            } else {
                return a - b;
            }
        }).join(',');
        rpc.query({
                    model: 'translate.name',
                    method: 'translate_names',
                    args: [main_company_id],
                });
        utils.set_cookie('cids', hash.cids || String(main_company_id));
        $.bbq.pushState({'cids': hash.cids}, 0);
        location.reload();


        console.log("workingggggggggggggggggggggggg",main_company_id)

    },
});

});
