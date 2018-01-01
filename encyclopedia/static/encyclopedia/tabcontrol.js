$(document).ready(function(){

  //수만큼 내용을 붙여넣도록 조작해야함.
  //내용을 넣을 수 있도록 조작해야함.
  //어떻게 django model의 내용을 전달할 수 있을까...?
  //row num에 따라 값을 넣는다.
  //iframe setting. listing.

  for(i = 0; i < $('#iframecount').val(); i++) {
    selector = "#listNum";
    selector = selector.concat(i);

    $(selector).attr('src', '/static/encyclopedia/sourcestorage/codeinventory/'+i);
    //files structure setting 필요
  }

  $('#nav-list-tab').click(function(){
      $('#layoutTitle').slideDown("slow");
  });

  $('#nav-insert-tab').click(function(){
      $('#layoutTitle').slideUp("slow");
  });

  $("form").submit(function() {
      var id= $("input[type=submit][clicked=true]").attr("id");
      if(id == 'savebutton'){
        $('#selectorID').val('makeFILE');
      }
   });

   $("form input[type=submit]").click(function() {
       $("input[type=submit]", $(this).parents("form")).removeAttr("clicked");
       $(this).attr("clicked", "true");
   });

});
