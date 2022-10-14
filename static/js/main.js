$.ajax({
        type:'GET',
        url : '/blog/posts',
        success: function(response){
            console.log(response)
            const data = response.data
        },
        error: function(error){
            console.log(error)
        }
})