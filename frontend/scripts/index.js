document.querySelector(".nxt-step").onclick = () => {

    if (document.querySelector(".nxt-step").innerHTML == "Try Again") {
        location.reload();
    }

    document.querySelector(".custom-input").disabled = true;
    document.querySelector(".block-input > div:nth-child(2) > p").style.opacity = "0";

    document.querySelector(".step-1 > div:nth-child(1)").style.background = "#F6F6F6";
    document.querySelector(".step-2 > div:nth-child(1)").style.background = "#0b75ff";

    document.querySelector(".step-1 > div:nth-child(1)").style.color = "#A8ADC7";
    document.querySelector(".step-2 > div:nth-child(1)").style.color = "white";

    document.querySelector(".step-1 > div:nth-child(2) > span").style.color = "#A8ADC7";
    document.querySelector(".step-2 > div:nth-child(2) > span").style.color = "#193660";

    document.querySelector(".block-title > span").innerHTML = "Step 2/2";
    document.querySelector(".block-title > h2").innerHTML = "Results of text analysis";

    document.querySelector(".nxt-step").innerHTML = "Try Again";

    document.querySelector(".similar-result").style.display = "flex";
    document.querySelector(".result").style.display = "flex";

    document.querySelector(".similar-result").style.opacity = "1";
    document.querySelector(".result").style.opacity = "1";

    // document.querySelector(".block-input").innerHTML = document.querySelector(".block-input").innerHTML + ""

    text_1 = document.querySelector(".custom-input").value;

    $.ajax({
        url: "http://localhost:55555/predict",
        data: {text: $.trim(text_1)},
        success: function(result){
            alert(result);
        }
    });
}
