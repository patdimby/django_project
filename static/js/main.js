cleared[0] = cleared[1] = cleared[2] = 0; 
function clearField(t) { 
  if (!cleared[t.id]) { 
    cleared[t.id] = 1; 
    t.value = ''; 
    t.style.color = '#fff';
  }
}

const social = document.getElementById('socials')
$.ajax({
    type:'GET',
    url : '/blog/socials',
    success: function(response){          
        const data = response.data            
        data.forEach(element => {
            socials.innerHTML +=`<li><a href="${element.link}">${element.title}</a></li>`
        });
    },
    error: function(error){
        console.log(error)
    }
});