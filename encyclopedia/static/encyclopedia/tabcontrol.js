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
     var formData = $("#codeform").serialize();
     console.log("this section is executed.");
     $('#selectorID').val('makeDEMO');

     $.ajax({
         type : "POST",
         url : "http://14.63.172.86:8001/encyclopedia/upload",
         data : formData,
         success:function(data){
           $('#tmpresult').attr('src','/static/encyclopedia/sourcestorage/hello.html');
         }
     });
   });

   $("#searchtext").on('keypress', function(e){
   	var keyCode = e.KeyCode || e.which;
	if(keyCode === 13){
	       var formData = $("#searchform").serialize();

	       //replace submit
	       $.ajax({
	         cache : false,
		 type : "POST",
	         url : "http://14.63.172.86:8001/encyclopedia/search",
	         data : formData,
	         dataType : 'json',
	         success:function(data){
	           console.log("this part is success")
	           result = jQuery.parseJSON(data);
	           $('#resultofsearch').append(
	             '<div class="col-sm-4">'
			+ result
			+ '</div>'
		   );  
		 },
	
	         error:function(xhr, status, error){
	           $('#resultofsearch').text('internal server is error');
	         }
	       });
	
		return false;
	 }
	
	//prevent submit. 
	//if submit is executed.. then key up is happened. 

   });

//   $("#searchtext").keyup(function(e){
//  });

});
