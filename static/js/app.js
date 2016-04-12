
//添加
function add(){
	var thing = $("#thing").val();
	$.ajax({
		
		url:"/add?thing="+thing,
		type:"POST",
		success:function(data){
			if(data==1){
				$.toast("添加成功");
				setTimeout(function(){
					window.location.href="/";
				},1000);
				
			}else{
				$.toast("添加失败", "cancel");
			}
		}
	});

}
	

//修改
function change(id,status){
	var id = id;
	var status = status;
	var thing_div_id = "#thing_"+id;
	$.confirm("您确定要更新状态吗", "确认更新?", function(){
		$.ajax({
			url:"/update?id="+id+"&status="+status,
			type:"POST",
			success:function(data){

				if(data==1){
					$.toast("恭喜计划完成");
					setTimeout(function(){
						$(thing_div_id).remove();
					},500);
					
				}else{
					$.toast("服务器开小差了");
				}
			}
		});

		}, function() {
  
	});

}