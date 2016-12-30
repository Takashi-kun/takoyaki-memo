var DOMAIN = "https://takoyaki-memo.appspot.com";
$(document).ready(function() {
    var memo_id = getParamId();
    if (memo_id) {
        toggleInputs(true);
        getMemoContent(memo_id);
    } else {
        $("#create_button").click(function() {
            toggleInputs(true);
            postMemoContent();
        });
    }
});

function toggleInputs(isDisable) {
    if (isDisable) {
        $("#memo_id").attr("readonly", true);
        $("#memo_area").attr("readonly", true);
        $("#create_button").attr("disabled", true);
    } else {
        $("#memo_id").attr("readonly", false);
        $("#memo_area").attr("readonly", false);
        $("#create_button").attr("disabled", false);
    }
}

function getMemoContent(memo_id) {
    $.ajax({
        type: "GET",
        url: "/api/" + memo_id,
        dataType: "json",
        success: function(responseData, status, xhr) {
            if (xhr.status == 200) {
                $("#memo_id").val(responseData["body"]["id"]);
                $("#memo_area").val(responseData["body"]["text"]);
                showShareLink(responseData["body"]["id"]);
            } else {
                location.href = "/";
            }
        },
        error: function() {
            location.href = "/";
        }
    });
}

function postMemoContent() {
    var memo_id = $("#memo_id").val();
    if (! memo_id) {
        memo_id = "new";
    }
    var text = $("#memo_area").val();
    $.ajax({
        type: "POST",
        url: "/api/" + memo_id,
        dataType: "json",
        contentType: "application/json",
        data: JSON.stringify({"context": text}),
        success: function(responseData, status, xhr) {
            if (xhr.status == 200) {
                $("#memo_id").val(responseData["body"]["id"]);
                $("#memo_area").text(responseData["body"]["text"]);
                showShareLink(responseData["body"]["id"]);
            } else {
                alert("失敗！！！");
            }
        },
        error: function() {
            alert("失敗！！！");
        }
    });
}

function showShareLink(memo_id) {
    $("#share_link").attr("href", "/?id=" + memo_id);
    $("#share_link").text(DOMAIN + "/?id=" + memo_id);
    $("#share_link").show();
}

function getParamId() {
    var url = location.href;
    var parameters = url.split("?");
    if (! parameters[1]) {
        return "";
    }

    params = parameters[1].split("&");
    for (var i = 0; i < params.length; i++) {
        var arr = params[i].split("=");
        if (arr[0] == "id") {
            return arr[1];
        }
    }

    return "";
}