
// When key is pressed form is updated. 
// $(document).ready(function(){
//   $('textarea').keyup(function(event){
//
//       //iframe handling
//       // $('#tmpresult').get(0).contentDocument.documentURL = $('#tmpresult').get(0).contentDocument.baseURL;
//       var code = $('textarea').serializeArray(); //data serialization.
//
//       //initialize
//       var destiframe = $('#tmpresult').contents();
//       destiframe.find('head').empty();
//       destiframe.find('body').empty();
//
//       //add script and style
//       destiframe.find('head').append("<style></style>");
//       destiframe.find('body').append('<script type="text/javascript"></script>');
//
//       //attach customized code
//           jQuery.each( code, function( i, code ) {
//             switch(i){
//               case 0:
//                     destiframe.find('style').append(code.value);
//
//               break;
//               case 1:
//                     destiframe.find('body').append(code.value);
//
//               break;
//               case 2:
//                     destiframe.find('script').append(code.value);
//
//               break;
//               default:
//                     console.log("empty set");
//               break;
//             }//end of switch
//           });//end of each
//       });//end of key press
// });//end of ready
