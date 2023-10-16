const main1 = (show) => {
    if (show) {
        document.getElementById("main1").style.display = 'grid';
    } else {
        document.getElementById("main1").style.display = 'none';
    }
}
const main2 = (show) => {
    if (show) {
        document.getElementById("main2").style.display = 'grid';
    } else {
        document.getElementById("main2").style.display = 'none';
    }
}

document.getElementById("btn1").addEventListener("click",function(){
    main1(false);
    main2(true);
})
document.getElementById("btn2").addEventListener("click",function(){
    main2(false);
    main1(true);
})
document.getElementById("btn3").addEventListener("click",function(){
    window.location.replace('Forces/')
})

main1(true)
main2(false);


