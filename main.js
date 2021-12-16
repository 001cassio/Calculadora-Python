function soma(num1, num2){
    return num1 + num2;
}
function subtracao(num1, num2){
    return num1 - num2;
}
function divisao(num1, num2){
    return num1 / num2;
}
function multilicacao(num1, num2){
    return num1 * num2;
}
function ola(){
    console.log(
        botao.innerHTML
    );
}

//window.onload = function(){
//    alert('pagina carregada');
//}
var botao = document.getElementById("botao");
botao.addEventListener("click", function(){
    console.log("ok");
});