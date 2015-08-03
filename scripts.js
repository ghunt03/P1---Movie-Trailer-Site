// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
	// Remove the src so the player itself gets removed, as this is the only
	// reliable way to ensure the video stops playing in IE
	$("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.view-trailer', function (event) {
	var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
	var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
	$("#trailer-video-container").empty().append($("<iframe></iframe>", {
	  'id': 'trailer-video',
	  'type': 'text-html',
	  'src': sourceUrl,
	  'frameborder': 0
	}));
});

$(document).ready(function () {
	// Open episode_list modal and populate season selector dropdown
	$("button[class*=view-episodes]").click(function(){
		var divEpisodeList = $(this).parent().parent().find(".episode_list");
		$(divEpisodeList).modal("show");
		// find table rows
		var tableRows = $(divEpisodeList).find("table tbody tr");
		var seasons = [];
		$.each(tableRows,function(){
			seasons.push($(this).data("season"));
		});
		seasons = $.unique(seasons).sort();	  
		var seasonFilter = $(divEpisodeList).find("div[class*=season-selector]");
		$(seasonFilter).empty();
		$(seasonFilter).append("<button type='button' class='btn btn-info season-filter' data-season='all'>All</button>");
		$.each(seasons,function(key,value){
			$(seasonFilter).append("<button type='button' class='btn btn-info season-filter' data-season='"+value+"'>"+value+"</button>"); 			
		});
		// filters episode list based on filter selected
		$("button[class*=season-filter]").click(function(){
			var season = $(this).data("season");
			switch(season) {
				case "all":
					$(tableRows).show(); 
				break;
				default:
					$(tableRows).hide();
					$(divEpisodeList).find("table tbody tr[data-season="+season+"]").show();
				break;
			}
		});	  
	});
	
	$("button[class*=filter_media]").click(function(){
		$("button[class*=filter_media]").removeClass("active");
		switch($(this).data("filter_value")) {
			case "movie":
				$("div[class*=movie-tile]").show();
				$("div[class*=tv-tile]").hide();
				break;
			case "tv":
				$("div[class*=movie-tile]").hide();
				$("div[class*=tv-tile]").show();
				break;
			default:
				$("div[class*=tile]").show();
				break;
		}
		$(this).addClass("active");
	});
});