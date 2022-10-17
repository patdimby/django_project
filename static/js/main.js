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
})