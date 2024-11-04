let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header ul li a');
let projectsLink = document.querySelector('header ul li a[href="#project"]');

window.onscroll = () => {
    let inProjectsSection = false;

    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if (top >= offset && top < offset + height) {
            navLinks.forEach(link => {
                link.classList.remove('active');
            });
            document.querySelector('header ul li a[href*=' + id + ']').classList.add('active');
            
            if (id === 'Number-Guess' || id === 'Student-info' || id === 'Recursion-turtle' || id === 'Recursion-graphics' ||
                id === 'project') {
                inProjectsSection = true;
            }
        }
    });

    if (inProjectsSection) {
        projectsLink.classList.add('active');
    } else {
        projectsLink.classList.remove('active');
    }
};

var coll = document.getElementsByClassName("collapse");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active1");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
