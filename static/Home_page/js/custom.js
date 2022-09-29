$(document).ready(function(){
    $('.increment-btn').click(function(e){
        e.preventDefault();

        var inc_value = $(this).closest('.product-data').find('.qty-input').val();
        var value = parseInt(inc_value, 20)
        value = isNaN(value) ? 0 : value;
        if(value < 10)
        {
            value++;
            $(this).closest('.product-data').find('.qty-input').val(value);

        }
    });

    $('.decrement-btn').click(function(e){
        e.preventDefault();

        var inc_value = $(this).closest('.product-data').find('.qty-input').val();
        var value = parseInt(inc_value, 10)
        value = isNaN(value) ? 0 : value;
        if(value > 1 )
        {
            value--;
            $(this).closest('.product-data').find('.qty-input').val(value);

        }
    });
    //add to cart
    $('.addToCartBtn').click(function (e) { 
        e.preventDefault();

        var product_id  = $(this).closest('.product-data').find('.prod_id').val();
        var product_qty = $(this).closest('.product-data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/cart/add-to-cart/",
            data: {
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken:token,
            },
            
            success: function (response) {
                console.log(response)
                alertify.success(response.status)
                
            }
        });
        
    });
});