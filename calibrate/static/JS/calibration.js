boxes = ["box11","box12","box13","box21","box22","box23","box31","box32","box33"]
boxes2 = ["box112","box122","box132","box212","box222","box232","box312","box322","box332"]


const cal_sub = (e,message) => {
    let calForm = document.getElementById("cal-form")
    
    let newDate = new Date();
    let datetime = `${newDate.getFullYear()}-${newDate.getMonth() + 1}-${newDate.getDate()} --- ${newDate.getHours()} : ${newDate.getMinutes()} : ${newDate.getSeconds()}`
    if (typeof e === "string"){
        calForm.mouseX.value = e
        calForm.mouseY.value = e
    } else {
        calForm.mouseX.value = e.pageX
        calForm.mouseY.value = e.pageX
    }

    calForm.time_stamp.value = datetime
    calForm.event.value = message

    return $('#cal-form').triggerHandler("submit")
}


window.addEventListener("load",function(){
    cal_sub("NA","Page Load")
})


const ele = (ID) => {
    return document.getElementById(ID)
}

const appear = (ID) => {
    ele(ID).style.opacity = 1
}

const disappear = (ID) => {
    ele(ID).style.opacity = 0
}

const max_clicks = 10

let j = Math.floor(9*Math.random())
let i = 0
cnt = 0
let sequential_done = false
array2 = document.getElementById("array2")
let message = document.getElementById("click-end")

// ARRAY 1
const click_count = (cnt,max_clicks) => {
    if (cnt >= max_clicks){
        array2.style.display="none";
        message.style.display = "flex";
        document.getElementById("navbar").style.display = "flex";
        ele("btn2").addEventListener("click",(e) => {
            cal_sub(e,"Finished Calibration");
            window.location.replace("/Force/")
        })
    }
}

ele("btn1").addEventListener("click",(e) => {
    document.getElementById("starting-message").style.display = "none";
    document.getElementById("array1").style.display = "flex";
    document.getElementById("navbar").style.display = "none";
    cal_sub(e,"Start Calibration")
})

appear(boxes[0])

ele(boxes[0]).addEventListener("click",(e) => {
    disappear(boxes[0])
    appear(boxes[1])
    cal_sub(e,`Clicked on Box ${boxes[0]}`)
})

ele(boxes[1]).addEventListener("click",(e) => {
    disappear(boxes[1])
    appear(boxes[2])
    cal_sub(e,`Clicked on Box ${boxes[1]}`)
})

ele(boxes[2]).addEventListener("click",(e) => {
    disappear(boxes[2])
    appear(boxes[3])
    cal_sub(e,`Clicked on Box ${boxes[2]}`)
})

ele(boxes[3]).addEventListener("click",(e) => {
    disappear(boxes[3])
    appear(boxes[4])
    cal_sub(e,`Clicked on Box ${boxes[3]}`)
})

ele(boxes[4]).addEventListener("click",(e) => {
    disappear(boxes[4])
    appear(boxes[5])
    cal_sub(e,`Clicked on Box ${boxes[4]}`)
})

ele(boxes[5]).addEventListener("click",(e) => {
    disappear(boxes[5])
    appear(boxes[6])
    cal_sub(e,`Clicked on Box ${boxes[5]}`)
})

ele(boxes[6]).addEventListener("click",(e) => {
    disappear(boxes[6])
    appear(boxes[7])
    cal_sub(e,`Clicked on Box ${boxes[6]}`)
})

ele(boxes[7]).addEventListener("click",(e) => {
    disappear(boxes[7])
    appear(boxes[8])
    cal_sub(e,`Clicked on Box ${boxes[7]}`)
})

ele(boxes[8]).addEventListener("click",(e) => {
    disappear(boxes[8])
    sequential_done = true ; 
    document.getElementById("array1").style.display = "none"
    document.getElementById("array2").style.display = "flex";
    appear(boxes2[j])
    cal_sub(e,`Clicked on Box ${boxes[8]}`)
})

// ARRAY 2

ele(boxes2[0]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done && cnt < max_clicks) {
        cal_sub(e,`Clicked on Box ${boxes[0]}`)
        disappear(boxes2[0])
        j = Math.floor(9*Math.random())
        while (j === 0){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {
        message.style.display = "flex";
        array2.style.display = "none"
    }   
})

ele(boxes2[1]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done && cnt < max_clicks) {
        cal_sub(e,`Clicked on Box ${boxes[1]}`)
        disappear(boxes2[1])
        j = Math.floor(9*Math.random())
        while (j === 1){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
            array2.style.display = "none"
}
})

ele(boxes2[2]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[2]}`)
        disappear(boxes2[2])
        j = Math.floor(9*Math.random())
        while (j === 2){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"
    array2.style.display = "none"
}
})

ele(boxes2[3]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[3]}`)
        disappear(boxes2[3])
        j = Math.floor(9*Math.random())
        while (j === 3){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none"
}
})

ele(boxes2[4]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[4]}`)
        disappear(boxes2[4])
        j = Math.floor(9*Math.random())
        while (j === 4){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none"
}
})

ele(boxes2[5]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[5]}`)
        disappear(boxes2[5])
        j = Math.floor(9*Math.random())
        while (j === 5){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none";
}

})

ele(boxes2[6]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[6]}`)
        disappear(boxes2[6])
        j = Math.floor(9*Math.random())
        while (j === 6){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none";}
})

ele(boxes2[7]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[7]}`)
        disappear(boxes2[7])
        j = Math.floor(9*Math.random())
        while (j === 7){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none";}
})

ele(boxes2[8]).addEventListener("click",(e) => {
    click_count(cnt,max_clicks);
    if (sequential_done) {
        cal_sub(e,`Clicked on Box ${boxes[8]}`)
        disappear(boxes2[8])
        j = Math.floor(9*Math.random())
        while (j === 8){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none";}
})


$("#cal-form").submit(function(e){
    e.preventDefault();
    form = $(this);
    const url = window.location;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        type: "POST",
        url: url,
        data: form.serialize(),
        })
    })

