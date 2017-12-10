function codeImplementator(i){

    var CSStext = document.getElementById("CSSsource"+i).value;
    var HTMLtext = document.getElementById("HTMLsource"+i).value;
    var JAVASCRIPTtext = document.getElementById("JAVASCRIPTsource"+i).value;
    var ifr = document.createElement("iframe");
    ifr.name = "target"+i;
    ifr.width  = "100%";
    ifr.height = "500";
    document.getElementById("iframeWrapper"+i).innerHTML="";
    document.getElementById("iframeWrapper"+i).appendChild(ifr);

    document.getElementById("CSScode").value = CSStext;
    document.getElementById("HTMLcode").value = HTMLtext;
    document.getElementById("JAVASCRIPTcode").value = JAVASCRIPTtext;
    document.getElementById("codeForm").action = "http://localhost/projectstarbucks/firstcode.php";
    document.getElementById('codeForm').method = "post";
    document.getElementById('codeForm').acceptCharset = "utf-8";
    document.getElementById('codeForm').target = "target"+i;
    ifr.src="http://localhost/projectstarbucks/firstcode.php";
    document.getElementById("codeForm").submit();

}

function finder(){
  var column = document.getElementById("search_column").value;
  var text = document.getElementById("search_value").value;
  var ifr = document.createElement("iframe");
  ifr.name = "target"
  ifr.width = "100%";
  ifr.height = "500";
  document.getElementById("iframeWrapperForSearch").innerHTML="";
  document.getElementById("iframeWrapperForSearch").appendChild(ifr);

  document.getElementById("column").value = column;
  document.getElementById("text").value = text;
  document.getElementById("codeForm").action = "http://localhost/projectstarbucks/search.php";
  document.getElementById('codeForm').method = "post";
  document.getElementById('codeForm').acceptCharset = "utf-8";
  document.getElementById('codeForm').target = "target";
  ifr.src="http://localhost/projectstarbucks/search.php";
  document.getElementById("codeForm").submit();



}

function codeModifier(i){
  var htmlsource = document.getElementById("HTMLsourceinsert").value;
  var csssource = document.getElementById("CSSsourceinsert").value;
  var javascriptsource = document.getElementById("JAVASCRIPTsourceinsert").value;
  var title = document.getElementById("inputTitleinsert").value;
  document.getElementById("id").value = i;//current id
  document.getElementById("CSScode").value = csssource;
  document.getElementById("HTMLcode").value = htmlsource;
  document.getElementById("JAVASCRIPTcode").value = javascriptsource;
  document.getElementById("title").value = title;
  document.getElementById("codeForm").action = "http://localhost/projectstarbucks/modify.php";
  document.getElementById('codeForm').method = "post";
  document.getElementById('codeForm').acceptCharset = "utf-8";
  document.getElementById("codeForm").submit();
}

var codebtn=document.getElementById("adder");
codebtn.addEventListener('click',function(){

  //data를 저장하기 위한 code.
  var htmlsource = document.getElementById("HTMLsourceinsert").value;
  var csssource = document.getElementById("CSSsourceinsert").value;
  var javascriptsource = document.getElementById("JAVASCRIPTsourceinsert").value;
  var title = document.getElementById("TITLEsourceinsert").value;
  document.getElementById("CSScode").value = csssource;
  document.getElementById("HTMLcode").value = htmlsource;
  document.getElementById("JAVASCRIPTcode").value = javascriptsource;
  document.getElementById("title").value = title;
  document.getElementById("codeForm").action = "http://localhost/projectstarbucks/insert.php";
  document.getElementById('codeForm').method = "post";
  document.getElementById('codeForm').acceptCharset = "utf-8";
  document.getElementById("codeForm").submit();

});

function changeTab(i){

  // 각 Frame에 설정된 초기 값으로 리셋하는 함수들
  var CSStext = document.getElementById("CSSsource"+i).value;
  var HTMLtext = document.getElementById("HTMLsource"+i).value;
  var JAVASCRIPTtext = document.getElementById("JAVASCRIPTsource"+i).value;
  var ifr = document.createElement("iframe");
  ifr.name = "target"+i;
  ifr.width  = "100%";
  ifr.height = "500";
  document.getElementById("iframeWrapper"+i).innerHTML="";
  document.getElementById("iframeWrapper"+i).appendChild(ifr);

  document.getElementById("CSScode").value = CSStext;
  document.getElementById("HTMLcode").value = HTMLtext;
  document.getElementById("JAVASCRIPTcode").value = JAVASCRIPTtext;
  document.getElementById("codeForm").action = "http://localhost/projectstarbucks/firstcode.php";
  document.getElementById('codeForm').method = "post";
  document.getElementById('codeForm').acceptCharset = "utf-8";
  document.getElementById('codeForm').target = "target"+i;
  ifr.src="http://localhost/projectstarbucks/firstcode.php";
  document.getElementById("codeForm").submit();
}

function menus(menu){

  htmlstr = '<label class="row" id="description" style="margin-left:0px;">';

  if(menu_name == "insert"){
              htmlstr = htmlstr + '새로운 코드를 입력하고 싶을 때 사용합니다.';
  }else if(menu_name == "search"){
              htmlstr = htmlstr + '새로운 코드를 입력하고 싶을 때 사용합니다.';
  }
  htmlstr = htmlstr + '</label>';

  return htmlstr;
}
