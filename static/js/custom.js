//Messages Timeout
var display_msg = document.getElementById("display_timeout");
setTimeout(function(){ 
    display_msg.style.display = "none"; 
}, 5000);

//Toggle Active
$(document).ready(function(){
    $('a[data-toggle="tab"]').on('show.bs.tab', function(e) {
        localStorage.setItem('activeTab', $(e.target).attr('href'));
    });
    var activeTab = localStorage.getItem('activeTab');
    if(activeTab){
        $('#myTab a[href="' + activeTab + '"]').tab('show');
    }
});