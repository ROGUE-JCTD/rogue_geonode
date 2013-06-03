var HistoryApp = (function(){
	
	return {
		init: function(options){
			$('.geogit-commit-history').live('click',function(evt){
				var commitId = $(this).find('.commit-id').attr('geogit-commit-id');
				console.log("commitId: " + commitId);
				HistoryApp.fetchDiff(commitId);
			});
			
			$('.back-to-history').click(this.toggleDivs);
		},
		fetchDiff: function(commitId){
			var fetched = GeoGit.ViewDiff.fetchDiff(commitId);
			
			if(fetched !== -1){
				this.toggleDivs();
			}
		},
		toggleDivs: function(){
			$('div .geogitCommit').toggle();
			$('div .geogitHistory').toggle();
		}
	};
}());