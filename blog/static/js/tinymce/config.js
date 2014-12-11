window.onload=function(){
    document.getElementById("id_use_visual_editor").onclick=function(){
        if(this.checked){
		tinymce_init();
	} else {
		window.location.reload();
	}
    }
}

function tinymce_init() {
	tinyMCE.init({
			mode : "textareas",
			plugins : "advlist,anchor,autolink,autosave,bbcode,charmap,code,contextmenu,directionality,emoticons,fullpage,fullscreen,hr,image,insertdatetime,layer,legacyoutput,link,lists,media,nonbreaking,noneditable,pagebreak,paste,preview,print,save,searchreplace,spellchecker,tabfocus,table,template,textcolor,visualblocks,visualchars,wordcount",  
			width: '600',
			height: '600',
		});
}
