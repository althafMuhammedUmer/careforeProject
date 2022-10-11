$(document).ready(function () {
     $('.payWithRazorpay').click(function (e) { 
        e.preventDefault();

        var fname = $("[name= 'first_name']").val();
        var lname = $("[name= 'last_name']").val();
        var country = $("[name= 'country']").val();
        var Address = $("[name= 'address_line_1']").val();
        var city = $("[name= 'city']").val();
        var state = $("[name= 'state']").val();
        var postcode = $("[name= 'post_code']").val();
        var phone = $("[name= 'phone']").val();
        var email = $("[name= 'email']").val();


        if (fname == "" || lname == "" || country == "" || phone == "" || Address == "" || city == "" || state == "" || postcode == "" || email == "" )
        {   
            console.log("form is invalid")
            swal("Alert!", "Please fill all fields !", "warning");
            
            return false;
        }
        else
        {

            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                
                success: function (response) {
                    console.log(response);
                    
                }
            });
            // var options = {
            //     "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
            //     "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            //     "currency": "INR",
            //     "name": "Acme Corp",
            //     "description": "Test Transaction",
            //     "image": "https://example.com/your_logo",
            //     "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            //     "handler": function (response){
            //         alert(response.razorpay_payment_id);
            //         alert(response.razorpay_order_id);
            //         alert(response.razorpay_signature)
            //     },
            //     "prefill": {
            //         "name": "Gaurav Kumar",
            //         "email": "gaurav.kumar@example.com",
            //         "contact": "9999999999"
            //     },
            //     "notes": {
            //         "address": "Razorpay Corporate Office"
            //     },
            //     "theme": {
            //         "color": "#3399cc"
            //     }
            // };
            // var rzp1 = new Razorpay(options);
            
            // rzp1.open();
            // swal("Good job!", "You clicked the button!", "success");
            

        }



        
        
     });
});