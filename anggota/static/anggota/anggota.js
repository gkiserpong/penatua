$( function() {
    $( "#pengusul_nama" ).autocomplete({
        // source: availableTags
        source: "{% url 'get-anggota' %}"
    });
    $( "#penatua_1" ).autocomplete({
        source: "{% url 'get-anggota' %}"
    });
    $( "#penatua_2" ).autocomplete({
        source: "{% url 'get-anggota' %}"
    });
    $( "#penatua_3" ).autocomplete({
        source: "{% url 'get-anggota' %}"
    });
    $( "#penatua_4" ).autocomplete({
        source: "{% url 'get-anggota' %}"
    });
    $( "#penatua_5" ).autocomplete({
        source: "{% url 'get-anggota' %}"
    });
    $.ajax('{% url 'get-wilayah' %}',
    {
        success: function(data, status, jqXHR) {
            // console.log(data);
            $.each(data, function(i, item) {
                //console.log(item.id);
                $('.form-select').append($('<option>', {
                    value: item.id,
                    text: item.nama

                }));                    
            });
        }
    });

    $("#submit_button").css('display', 'none');
    
    $("#section_detail_usulan").css('display', 'none');
    
    $("#konfirmasi").click(function() {
        if($("#konfirmasi").is(':checked')) {
            $("#submit_button").css('display', 'block');  // checked
            console.log("CHECKED")
        } else {
            $("#submit_button").css('display', 'block');  // unchecked
            console.log("UNCHECKED")
        }

    });

});

function isEmail(email) {
var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
return regex.test(email);
}

function validateEmail() {
let email_val = $('#pengusul_email').val();
if (! isEmail(email_val)) {
    alert('Mohon alamat email yang benar');
    $('#pengusul_email').focus();
}
else 
{
$('#section_detail_usulan').css('display', 'block');
            
$.ajax('{% url 'get-pengusul' %}?term=' + email_val, 
{
    success: function(data, status, jqXHR) {
        $('#data_detail').innerHTML = data;
        if ('pengusul_nama' in data) {
            $('#pengusul_email').val(data['pengusul_email'])
            $('#pengusul_nama').val(data['pengusul_nama'])
            $('#pengusul_mobile').val(data['pengusul_mobile'])
            $('#penatua_1').val(data['penatua_1'])
            $('#penatua_1_wilayah').val(data['penatua_1_wilayah'])
            $('#penatua_1_alasan').val(data['penatua_1_alasan'])
            $('#penatua_2').val(data['penatua_2'])
            $('#penatua_2_wilayah').val(data['penatua_2_wilayah'])
            $('#penatua_2_alasan').val(data['penatua_2_alasan'])
            $('#penatua_3').val(data['penatua_3'])
            $('#penatua_3_wilayah').val(data['penatua_3_wilayah'])
            $('#penatua_3_alasan').val(data['penatua_3_alasan'])
            $('#penatua_4').val(data['penatua_4'])
            $('#penatua_4_wilayah').val(data['penatua_4_wilayah'])
            $('#penatua_4_alasan').val(data['penatua_4_alasan'])
            $('#penatua_5').val(data['penatua_5'])
            $('#penatua_5_wilayah').val(data['penatua_5_wilayah'])
            $('#penatua_5_alasan').val(data['penatua_5_alasan'])
            
        }
        //console.log(data);
    }
});
}
}