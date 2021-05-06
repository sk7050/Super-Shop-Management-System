function SaveItem() {
			
	var name = document.getElementById('name').value;
	var phone =  document.getElementById('phone').value;
	var email= document.getElementById('email').value;
	var id = document.getElementById('id').value;
	var qty = document.getElementById('qty').value;
	if (name.length  && phone.length && email.length && id && qty){
		sessionStorage.setItem('name', name)
		sessionStorage.setItem('phone',phone)
		sessionStorage.setItem('email',email)
   
		document.getElementById("myForm").submit();
	}
	else{
		
		window.alert("please input all data")
	}

		 
  }


function myFunction() {


document.getElementById("name").value =sessionStorage.getItem('name');
document.getElementById("phone").value =sessionStorage.getItem('phone');
document.getElementById("email").value =sessionStorage.getItem('email');

}

function CreatBill() {

var name = document.getElementById('name').value;
var phone =  document.getElementById('phone').value;
var email= document.getElementById('email').value;
	
if (name.length  && phone.length && email.length ){
	
	var total_price=document.getElementById("total_price").innerText;
	document.getElementById("price").value=total_price ;

	 
	 document.getElementById("form1").submit();
	 sessionStorage.clear()
	 location.reload();
	 location.reload();
	}
	else{
		
		window.alert("please input all data")
	}    

   
  }

  function print(){
    var id=document.getElementById('bill_no').value;
    if (id.length){
      
      window.open("/main/order/invoce/"+id);
    }
    else{
      window.alert("please input bill no")
    }
  }