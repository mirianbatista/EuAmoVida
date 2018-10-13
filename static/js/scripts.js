function changeNavColor(){
  $(window).scroll(function() {
    nav = document.getElementById('nav-menu');
    links = document.getElementsByClassName('nav-link');

      if ($(window).scrollTop() == 0) {
          nav.style.background = 'transparent';
          nav.style.boxShadow = '0 0 0 0 #333';
          for(let link of links){
            link.style.color = '#000';
          }
      } else {
          nav.style.background = '#fff';
          nav.style.boxShadow = '0 5px 6px -6px #333';
          for(let link of links){
            link.style.color = '#333';
          }
      }
  });
}
changeNavColor();