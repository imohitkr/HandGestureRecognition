
/**
 * Request data from the server, update the graph and set a timeout
 * to request again
 */
function requestData() {
    $.ajax({
        url: '/live-data_video',
        success: function(response) {
            const {labels}=response;
            const html = labels.reduce((res, label)=>`${res}<div class="row">${label}</div>`, "");
            $('#recognition-results').html(html)
            setTimeout(requestData, 1000);
        },
        cache: false
    });
}

$(document).ready(function () {
    requestData();
});
