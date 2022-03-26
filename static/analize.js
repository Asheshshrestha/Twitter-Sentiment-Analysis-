$('#btnAnalayze').off('click').on('click',function(){

    if(!$('#txtAnalayzeText').val().trim()){
        alert('Please enter sentence first.');
        return;
        
    }
    $(this).attr('disabled',true).html('<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>Loading...');

    var form = new FormData();
    var text = $('#txtAnalayzeText').val();
    form.append("text", text);
    
    var settings = {
      "url": analizeURL,
      "method": "POST",
      "timeout": 0,
      "processData": false,
      "mimeType": "multipart/form-data",
      "contentType": false,
      "data": form
    };
    
    $.ajax(settings).done(function (response) {
      data = JSON.parse(response);
      if (data!= null)
      {
          var html = '';
          if(data.data == 'positive'){
              html = `<div class="alert alert-success" role="alert">
                        The text given has <span class="alert-link">POSITIVE</span> sentiment. Click clear.
                      </div>`;
          }else if(data.data=='negative'){
                html = `<div class="alert alert-danger" role="alert">
                            The text given has <span class="alert-link">NEGATIVE</span> sentiment. Click clear.
                        </div>`;
          }else if(data.data =='neutral'){
            html = `<div class="alert alert-info" role="alert">
                        The text given has <span class="alert-link">NEUTRAL</span> sentiment. Click clear.
                    </div>`;
          }
          else{
            html = `<div class="alert alert-warning" role="alert">
                        The text given has <span class="alert-link">${data.data}</span> sentiment. Click clear.
                    </div>`;
          }
          $("#result").html(html);
          $('#btnAnalayze').attr('disabled',false).html('Submit');
      }
    });
    
});
$('#btnClear').off('click').on('click',function(){
    $("#result").html('');
    $("#txtAnalayzeText").val('');
});