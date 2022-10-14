$.ajax({
        type:'GET',
        url : '/blog/posts',
        success: function(response){            
            //
        },
        error: function(error){
            console.log(error)
        }
})