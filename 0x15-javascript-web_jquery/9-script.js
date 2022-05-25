$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  $('DIV#hello').text(data.hello);
});
