let intro = document.querySelector('.intro');
let logo = document.querySelector('.logo-header');
let logoSpan = document.querySelectorAll('.logo');
let logoLeftSpan = document.querySelectorAll('.logo-left');
let logoRightSpan = document.querySelectorAll('.logo-right');
let logoAuthorSpan = document.querySelectorAll('.logo-author');

let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header ul li a');

window.addEventListener('DOMContentLoaded', ()=>{
    setTimeout(()=>{
        //Fades in the word for the splash screen
        logoLeftSpan.forEach((span, idx)=>{
            setTimeout(()=>{
                span.classList.add('active');
            }, idx * 400)
        });

        logoRightSpan.forEach((span, idx)=>{
            setTimeout(()=>{
                span.classList.add('active');
            }, idx * 400)
        });

        logoAuthorSpan.forEach((span, idx)=>{
            setTimeout(()=>{
                span.classList.add('active');
            }, (idx + 1) * 400)
        });

        logoSpan.forEach((span, idx)=>{
            setTimeout(()=>{
                span.classList.add('active');
            }, (idx + 1) * 400)
        });

        //fades out the words
        setTimeout(()=>{
            logoLeftSpan.forEach((span, idx)=>{
                setTimeout(()=>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, idx * 50)
            })

            logoRightSpan.forEach((span, idx)=>{
                setTimeout(()=>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, idx * 50)
            })

            logoAuthorSpan.forEach((span, idx)=>{
                setTimeout(()=>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 50)
            })

            logoSpan.forEach((span, idx)=>{
                setTimeout(()=>{
                    span.classList.remove('active');
                    span.classList.add('fade');
                }, (idx + 1) * 50)
            })
        },2500);    
        
        setTimeout(()=>{ //time for the splash screen to disappear
            intro.style.top = '-100vh';
        },3200);
        
    })
})

window.onscroll = () => {
    sections.forEach(sec =>{
        let top = window.scrollY;
        let offset = sec.offsetTop - 300;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header ul li a[href*=' + id + ']').classList.add('active');
            });
        };
    });
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
