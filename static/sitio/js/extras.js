function abrirmodal(url)
{
     $('#modal').load(url, function()
          {
           $(this).modal({
                backdrop: 'static',
                keyboard: false
            })
               $(this).modal('show');
            });
}