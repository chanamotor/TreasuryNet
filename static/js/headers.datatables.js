"use strict";
var KTDatatablesBasicHeaders = function() {

	var initTable1 = function() {
		var table = $('#kt_table_1');
		// begin first table
		table.DataTable({
			responsive: true,
			columnDefs: [	
			],
		});
	};
	return {
		//main function to initiate the module
		init: function() {
			initTable1();
		},
	};
}();

jQuery(document).ready(function() {
	KTDatatablesBasicHeaders.init();
});