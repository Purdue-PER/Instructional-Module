boxes = ["box11","box12","box13","box21","box22","box23","box31","box32","box33"]
boxes2 = ["box112","box122","box132","box212","box222","box232","box312","box322","box332"]

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

// ARRAY 1


ele("btn1").addEventListener("click",() => {
    document.getElementById("starting-message").style.display = "none";
    document.getElementById("array1").style.display = "flex"
})

appear(boxes[0])

ele(boxes[0]).addEventListener("click",() => {
    disappear(boxes[0])
    appear(boxes[1])
})

ele(boxes[1]).addEventListener("click",() => {
    disappear(boxes[1])
    appear(boxes[2])
})

ele(boxes[2]).addEventListener("click",() => {
    disappear(boxes[2])
    appear(boxes[3])
})

ele(boxes[3]).addEventListener("click",() => {
    disappear(boxes[3])
    appear(boxes[4])
})

ele(boxes[4]).addEventListener("click",() => {
    disappear(boxes[4])
    appear(boxes[5])
})

ele(boxes[5]).addEventListener("click",() => {
    disappear(boxes[5])
    appear(boxes[6])
})

ele(boxes[6]).addEventListener("click",() => {
    disappear(boxes[6])
    appear(boxes[7])
})

ele(boxes[7]).addEventListener("click",() => {
    disappear(boxes[7])
    appear(boxes[8])
})

ele(boxes[8]).addEventListener("click",() => {
    disappear(boxes[8])
    sequential_done = true ; 
    document.getElementById("array1").style.display = "none"
    document.getElementById("array2").style.display = "flex";
    appear(boxes2[j])
})

// ARRAY 2

const change = () => {
    const start = Date.now()
    const timer = setInterval(()=>{
        if(Date.now() - start >= 5000){
            window.location.replace("/Force/")
        }
    },150)        
    }


let message = document.getElementById("click-end")

ele(boxes2[0]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
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
        setTimeout(change(),4000)
    }   
})

ele(boxes2[1]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[1])
        j = Math.floor(9*Math.random())
        while (j === 1){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
            array2.style.display = "none"
            setTimeout(change(),4000)
}
})

ele(boxes2[2]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[2])
        j = Math.floor(9*Math.random())
        while (j === 2){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"
    array2.style.display = "none"
    setTimeout(change(),4000)
}
})

ele(boxes2[3]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[3])
        j = Math.floor(9*Math.random())
        while (j === 3){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none"
    setTimeout(change(),4000)
}
})

ele(boxes2[4]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[4])
        j = Math.floor(9*Math.random())
        while (j === 4){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none"
    setTimeout(change(),4000)
}
})

ele(boxes2[5]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[5])
        j = Math.floor(9*Math.random())
        while (j === 5){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex";
    array2.style.display = "none";
    setTimeout(change(),4000)
}

})

ele(boxes2[6]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[6])
        j = Math.floor(9*Math.random())
        while (j === 6){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none"; setTimeout(change(),4000)}
})

ele(boxes2[7]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[7])
        j = Math.floor(9*Math.random())
        while (j === 7){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none"; setTimeout(change(),4000)}
})

ele(boxes2[8]).addEventListener("click",() => {
    if (sequential_done && cnt < max_clicks) {
        disappear(boxes2[8])
        j = Math.floor(9*Math.random())
        while (j === 8){
            j = Math.floor(9*Math.random())
        }
        appear(boxes2[j])
        cnt += 1
    } else {message.style.display = "flex"; array2.style.display = "none"; setTimeout(chane(),4000)}
})



