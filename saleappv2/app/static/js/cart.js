function AddToCart(id, name, price){

alert("asd")
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
        let carts = document.getElementsByClassName("cart-counter");
        if ( let c of carts)
        c.innerText = data.total_quantity;
    })
}
