$(document).ready(function(){

  //수만큼 내용을 붙여넣도록 조작해야함.
  //내용을 넣을 수 있도록 조작해야함.
  //어떻게 django model의 내용을 전달할 수 있을까...?
  //row num에 따라 값을 넣는다.
  //iframe setting. listing.

  for(i = 0; i < $('#iframecount').val(); i++) {
    selector = "#listNum";
    selector = selector.concat(i);
    var address = '/static/encyclopedia/sourcestorage/codeinventory/'+i+'.html';
    $(selector).attr('src', address);
    //files structure setting 필요
  }

  $('#nav-list-tab').click(function(){
      $('#layoutTitle').slideDown("slow");
  });

  $('#nav-insert-tab').click(function(){
    console.log("hello world");
      $('#layoutTitle').slideUp("slow");
  });

  $("form").submit(function() {
      var id= $("input[type=submit][clicked=true]").attr("id");
      console.log("this is public service announcement");
      //if(id == 'savebutton'){
        $('#selectorID').val('makeFILE');
      //}
   });

   $("#transferbutton").click(function(){
     console.log("this section is executed.");
     var formData = $("#codeform").serialize();
     $('#selectorID').val('makeDEMO');

     $.ajax({
         type : "POST",
         url : "http://localhost:8000/encyclopedia/upload",
         data : formData,
         success:function(data){
           $('#tmpresult').attr('src','/static/encyclopedia/sourcestorage/hello.html');
         }
     });
   });

   $("#searchtext").on('keypress', function(e){
   });

   $("#searchtext").on('keyup keypress', function(e){
     var keyCode = e.KeyCode || e.which;
     if(keyCode === 13){
       e.preventDefault();
       console.log("enter up function is executed");
       var formData = $("#searchform").serialize();

       //replace submit
       $.ajax({
         type : "POST",
         url : "http://localhost:8000/encyclopedia/search",
         data : formData,
         dataType : 'json',
         success:function(data){
           result = jQuery.parseJSON(data);
           var index;
           $.each(result, function(key, value){
             $.each(value, function(k, v){
               console.log("start");
               if(k == "pk"){
                 index = v;
                 console.log("type of index is "+typeof(index));
               }else if(k == "fields"){
                 console.log("fields");
                 $.each(v, function(i, title){
                   if(i == "title"){

                       $('#resultofsearch').append(
                         '<div class="col-sm-4">'
                          +'<iframe class="col-sm-11" style="display:block; margin:auto; height:177.273px;" src="/static/encyclopedia/sourcestorage/codeinventory/'
                          + index
                          +'.html"></iframe><div style="background-color:yellow; text-align:center;">'
                          + title
                          + '</div></div>'
                       );
                   }

                 });
               }

             });
           });
         },

         error:function(xhr, status,error){
           $('#resultofsearch').text('internal server is error');
         }
       });
     }
   });

});
