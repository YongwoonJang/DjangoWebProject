$(document).ready(function(){

  //수만큼 내용을 붙여넣도록 조작해야함.
  //내용을 넣을 수 있도록 조작해야함.
  //어떻게 django model의 내용을 전달할 수 있을까...?
  //row num에 따라 값을 넣는다.
  //iframe setting. listing.
  
  for(i = 0; i < $('#iframecount').val(); i++) {
    selector = "#listNum";
    selector = selector.concat(i);
    destiframe = $(selector).contents();

    destiframe.find('head').empty();
    destiframe.find('body').empty();
    destiframe.find('head').append("<style></style>");
    destiframe.find('body').append("<script></script>");

    csscontents = "#iframecss";
    csscontents = csscontents.concat(i);
    destiframe.find('style').append($(csscontents).val());


    htmlcontents = "#iframehtml";
    htmlcontents = htmlcontents.concat(i);
    destiframe.find('body').append($(htmlcontents).val());

    jscontents = "#iframejs";
    jscontents = jscontents.concat(i);
    destiframe.find('script').append($(jscontents).val());
  }

  $('#nav-list-tab').click(function(){
      $('#layoutTitle').slideDown("slow");
  });

  $('#nav-insert-tab').click(function(){
      $('#layoutTitle').slideUp("slow");
  });

});
