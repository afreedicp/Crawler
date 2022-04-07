console.log('hello world');
function main() {
  $.get({
    url: 'http://127.0.0.1:5000/artist',
    success: (data) => {
      list = '';
      data.forEach((element) => {
        list +=
          `<li class="artist" value=${element.id}>` + element.name + `</li>`;
      });
      tag = `<ul>${list}</ul>`;
      $('div.artist').html(tag);
      console.log(data);
    },
  });
  $(document).on('click', 'li.artist', function () {
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}`,
      success: (data) => {
        list = '';
        data.forEach((element) => {
          list += `<li class="song" id=${element.id}>` + element.name + `</li>`;
        });
        tag = `<ul>${list}</ul>`;
        $('div.song').html(tag);
      },
    });
  });
  $(document).on('click', 'li.song', function () {
    $.get({
      url: `http://127.0.0.1:5000/songs/${this.value}/lyrics/${this.id}`,
      success: (data) => {
        $('div.lyrics').html(data);
      },
    });
  });
}
$(main);
