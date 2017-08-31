class CGProjectLoader{
    constructor(){
    	var self = this;
    	self.checkSwitcherState();
    	self.loading = false;
    	self.loadingTimer;
    	self.overlay = $('#overlay');
    	self.canvas = $('#renderCanvas' ); 
    	self.current_model_index = 0;
    	self.logo_link = $('#logo-link');
    	self.current_animation_index = -1;
    	
    	this.project_json = $.parseJSON($('#model-project').val())[0]['fields'];
    	this.project_json['materials'] = $.parseJSON($('#model-materials').val());
    	this.model3d_json = $.parseJSON($('#model-3dmodels').val());
    	this.model2d_json = $.parseJSON($('#model-2dmodels').val());
    	this.$model_switcher = $('#model-switcher .slim-scrollbar');
    	
    	self.bindUI();
    }
    
    webgl_support() {
    	var params = this.queryParameters();
    	if( params.force2d === 'true' ){
    		return false;
    	}
		try{
			var gl = this.canvas.get(0).getContext( 'webgl' ) || canvas.getContext( 'experimental-webgl' );
			return true;
		}catch( e ) { 
			return false; 
		} 
	}
    
    buildUI2d(){
    	var context = {
    		'model_type': 'model2d',
    		'object_list': this.model2d_json,
    	};
    	var tmpl = nunjucks.render('switcher.html', context);
    	this.$model_switcher.html(tmpl);
    	
    	this.set_loading(false);
    }
    
    buildUI3d(){
    	var context = {};
    	if(this.model3d_json.length === 1){
    		if(this.model3d_json[0].animation.animations && this.model3d_json[0].animation.animations.length > 0){
    			context['model_type'] = 'animation';
    			context['object_list'] = this.model3d_json[0].animation.animations;
    		}else{
    			context['model_type'] = 'model3d';
    			context['object_list'] = this.model3d_json;
    		}
    	}else{
    		context['model_type'] = 'model3d';
			context['object_list'] = this.model3d_json;
    	}
    	var tmpl = nunjucks.render('switcher.html', context);
    	this.$model_switcher.html(tmpl);
    }
    
    bindUI(){
    	this.bindUICommon();
    	this.bindUI2d();
    	this.bindUI3d();
    }
    
    bindUICommon(){
    	var self = this;
    	if( self.overlay.hasClass('play') ){
    		self.overlay.click(function(){
    			self.overlay.removeClass('play').find('.text-play').remove();
    			self.loadProjectAuto();
    		})
    	}else{
    		self.loadProjectAuto();
    	}
    	
    	$('.slim-scrollbar').each(function(i, scrollbar){
    		var bg = $(scrollbar).attr('data-bgcolor');
    		$(scrollbar).slimScroll({
    	        height: '100%',
    	        color: bg,
    	        alwaysVisible: true,
    	        disableFadeOut: true,
    	    });
    	});
    	
    	function onResize(){
			$('#model-switcher ul').css('max-height', $(window).height()-56+'px');
		};
		
		$(window).resize(function() {
			onResize();
		});
		onResize();
    }
    
    bindUI2d(){
    	var self = this;
    }
    
    bindUI3d(){
    	var self = this;
    	$('#switcher-model3d > li > a[data-index]').click(function(e){
			e.preventDefault();
			$('#popup-post-loading').remove();
			self.changeModel($(this).attr('data-index'));
		})
		
		$('#switcher-model2d > li > a[data-index]').click(function(e){
			e.preventDefault();
			$('#popup-post-loading').remove();
			self.changeModel2d($(this).attr('data-index'));
		})
		
		$('#switcher-animation > li > a[data-index]').click(function(e){
			e.preventDefault();
			$('#popup-post-loading').remove();
			self.changeAnimation(parseInt( $(this).attr('data-index') ));
		})
		
		$(document).on('click touchstart', '.animation-fliper', function(e){
			e.preventDefault();
			if(CG.App.Instance.animationManager.isAnimating){
				return;
			}
			$('#popup-post-loading').remove();
			var item_active = $('#model-switcher ul > li:has(a.active[data-index])');
			if(item_active.length === 0 || self.current_animation_index < 0){
				if($(this).hasClass('animation-prev')){
					return;
				}
				item_active = $('#model-switcher ul > li:has(a[data-index])').first();
			}else if($(this).hasClass('animation-next')){
				item_active = item_active.next();
			}
			if(item_active){
				item_active.find('a').click();
			}
			
			if($(this).hasClass('animation-prev')){
				$('#model-switcher ul > li > a.active[data-index]').removeClass('active');
				item_active.prev().find('a').addClass('active');
			}
		})
		
		self.canvas.on('mousedown touchstart', function(){
			$('#popup-post-loading').remove();
		})
    }
    
    set_loading(v){
    	var self = this;
    	self.loading = v;
    	if(self.loading){
    		self.overlay.find('.text-loading').show();
	    	self.loadingTimer = setTimeout(function(){
				var d = self.overlay.find('.text-loading .dots');
				if(d.text().length > 2){
					d.text('');
				}else{
					d.text(d.text() + '.');	
				}
				$('#overlay img').height($('#overlay').height());
				self.set_loading(v);
			}, 400);
    	}else{
    		clearTimeout(self.loadingTimer);
    		self.overlay.remove();
    	}
    }
    
    checkSwitcherState(){
    	var ms = $('#model-switcher');
    	if(ms.hasClass('hidden-always')){
    		ms.hide();
    		return;
    	}
		var is_show = $('#model-switcher #witcher-model3d').children().length > 1;
		is_show = is_show || $('#model-switcher #switcher-animation').children().length > 0;
		if(is_show){
			ms.show();
		}else{
			ms.hide();
		}
	}
    
//    ===============
    loadProjectAuto(){
    	var type = this.webgl_support() ? '3d' : '2d';
    	this.loadProjectByType(type);
    }
    
    loadProjectByType(type){
    	this.set_loading(true);
    	if(type === '2d'){
    		this.loadProject2D();
    	}else if(type === '3d'){
    		this.loadProject3D();
    	}
    }
    
    loadProject3D(){
    	new CG.App(this.project_json);
    	this.buildUI3d();
    	this.changeModel(0);
    }
    
    loadProject2D(){
    	this.buildUI2d();
    	this.changeModel2d(0);
    }
    
    changeModel(index){
    	if( this.model3d_json.length <= index ){
    		return;
    	}
    	var data = $.extend({}, {type: "modelChanged", tab: "models"}, this.model3d_json[index]);
    	$("body").trigger(data);
    	this.current_model_index = index;
    	
    	$('#switcher-model3d > li > a[data-index]').removeClass('active').eq(index).addClass('active');
    }
    
    changeModel2d(index){
    	if( this.model2d_json.length <= index ){
    		return;
    	}
    	var image = this.model2d_json[index].image;
    	$('#main_container').css('background-size', 'cover');
    	$('#main_container').css('background-repeat', 'no-repeat');
    	$('#main_container').css('background-position', 'center');
    	$('#main_container').css('background-image', 'url(' + image + ')');
    	$('#switcher-model2d > li > a[data-index]').removeClass('active').eq(index).addClass('active');
    	
    	this.current_model_index = index;
    }
    
    changeAnimation(index){
    	if(CG.App.Instance.animationManager.isAnimating){
			return;
		}
    	
    	CG.App.Instance.animationManager.animate(index);
    	$('#switcher-animation > li > a[data-index]').removeClass('active').eq(index).addClass('active');
    	

    	var current_animation = this.model3d_json[this.current_model_index]['animation']['animations'][index];
    	if(current_animation['logo_url']){
    		this.logo_link.attr('href', current_animation['logo_url'])
    	}
    	
    	this.current_animation_index = index;
    }
    
    queryParameters () {
        var result = {};

        var params = window.location.search.split(/\?|\&/);

        params.forEach( function(it) {
            if (it) {
                var param = it.split("=");
                result[param[0]] = param[1];
            }
        });

        return result;
    }
//  ===============
}

var CG_PROJECT_LOADER = new CGProjectLoader();
window['sceneReady'] = function sceneReady(){
	CG_PROJECT_LOADER.set_loading(false);
	$('#popup-post-loading').show();
}