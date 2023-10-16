// document.addEventListener("DOMContentLoaded", hideshow());
document.getElementById('menu_btn').addEventListener("click", hideshowinfo);
    function hideshowinfo() {
        let x = document.getElementById('info');
        if (x.style.display == "none"){
        x.style.display = "block";
        } else {
        x.style.display = "none"}
    };
document.getElementById('portfolio_btn').addEventListener("click", hideshowportf);
    function hideshowportf() {
        let list = document.getElementById('portfolio_list1');
        if (list.style.display == "none"){
        list.style.display = "block";
        } else {
        list.style.display = "none"}
    };