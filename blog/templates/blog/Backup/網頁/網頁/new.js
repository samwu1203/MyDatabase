function doFirst(){
	document.getElementById('theForm').onsubmit = setEvent;
	
}
function setEvent(){
	var events=['click','select','contextmenu','input','focus','change'];
	
	for(var i=0 ;i<events.length;i++){
		//先跟HTML畫面產生關聯
		var checkElement =document.getElementById(events[i]);
		//該物件有被勾選,在建事聆聽功能
		if(checkElement.checked){
			document.addEventListener(events[i],report,false); 
			//物件                    
		}
	}
	
	
	
	document.getElementById('output').value='';
	return false;
}

function report(e){
		/* alert(e.target.nodeName); */
	var output= e.target.nodeName + ' : '+e.type+ '\n';
	document.getElementById('output').value +=output;
		
}
	

window.addEventListener('load',doFirst,false);