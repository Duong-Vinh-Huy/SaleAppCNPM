function AddToCart(id, name, price){
    fetch('/api/cart', {
        method : 'post',
        body: JSON.stringify({
            "id" : id,
            "name" : name,
            "price" : price
        }),
        headers: {
            'Content-Type' : 'application/json'
        }
    }).then(function(res){
        return res.json();
    }).then(function(data) {
        console.info(data);
    })
}