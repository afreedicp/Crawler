console.log('hello world');
function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artist',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list += '<li class="artist">' + element.name + '</li>';
      });
      tag = `<ul>${list}</ul>`;
      $('div.lyrics').html(tag);
      console.log(data);
    },
  });
  $(document).on('click', 'li.artist', function(){
       $.get({
    url: 'http://127.0.0.1:5000/a',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list += '<li class="artist">' + element.name + '</li>';
      });
      tag = `<ul>${list}</ul>`;
      $('div.lyrics').html(tag);
  });
}
$(main);