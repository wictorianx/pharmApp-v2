function createAccount(){
    window.location.href = '/createAccount'
}
var nameinputx = document.getElementById("nameinput")
var passinputx = document.getElementById("passinput")
var form = document.getElementById("form")
nameinputx.addEventListener("keypress", function (e){
    if (e.key === "Enter"){
        passinputx.focus()
    }
})
passinputx.addEventListener("keypress", function (e){
    if (e.key === "Enter"){
        form.submit()
    }
})