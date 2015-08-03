import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>GH Media Site</title>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="styles.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="scripts.js"></script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!-- Main Page Content -->
<body>
    <div class="container">
        <div class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">GH Media Site</a>
                </div>
            </div>
        </div>
    </div>
    <div class="container">
        <div class="col-sm-2">
            <h4>Show: </h4>
            <div class="btn-group-vertical" role="group">
              <button type="button" class="btn btn-primary filter_media active" data-filter_value="all">All</button>
              <button type="button" class="btn btn-primary filter_media" data-filter_value="movie">Movies</button>
              <button type="button" class="btn btn-primary filter_media" data-filter_value="tv">TV Series</button>
            </div>
        </div>
        <div class="col-sm-10">
            {tiles}
        </div>
    </div>
	<!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                    Trailer
                </div>
                <div class="scale-media" id="trailer-video-container">
                </div>
            </div>
        </div>
    </div>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="row movie-tile">
    <div class="col-sm-3"><img src="{thumbnail}" width="220" height="342"/></div>
    <div class="col-sm-9">
        <h2>{title}</h2>
        <p>{story_line}</p>
        <p>
        <button type="button" class="btn btn-primary view-trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">View Trailer</button>
        </p>
    </div>
</div>
'''

# A single tv show html template
tv_tile_content = '''
<div class="row tv-tile">
    <div class="col-sm-3">
        <img src="{thumbnail}" width="220" height="342"/>
    </div>
    <div class="col-sm-9">
        <h2>{title} (TV Series)</h2>
        <p>
            {story_line}
        </p>
        <p>
            <button type="button" class="btn btn-primary view-episodes">View Episode List</button>
        </p>
        <div class="episode_list modal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        {title} (TV Series) - Episode List
                    </div>
                    <div class="modal-body">
                        <b>Season: </b>
                        <div class="btn-group season-selector">
                        </div>
                        <div style="height:500px; overflow:auto;">
                            <table class="table table-striped">
                                <thead>
                                    <tr>
                                        <th>Season</th>
                                        <th>Episode</th>
                                        <th>Title</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {episodes}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
'''
# row template for tv episode
tv_episode_row = '''
<tr data-season={season}>
    <td>
        {season}
    </td>
    <td>
        {episode}
    </td>
    <td>
        {title}
    </td>
</tr>
'''


def create_media_tiles_content(media_list):
    # The HTML content for this section of the page
    content = ''
    for media_item in media_list:
        if media_item.media_type == "Movie":
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+',
                media_item.trailer_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+',
                media_item.trailer_url)
            if youtube_id_match:
                trailer_youtube_id = youtube_id_match.group(0)
            else:
                trailer_youtube_id = None

            # Append the tile for the movie with its content filled in
            content += movie_tile_content.format(
                title=media_item.title,
                thumbnail=media_item.thumbnail,
                trailer_youtube_id=trailer_youtube_id,
                story_line=media_item.story_line
            )
        else:
            # Build Episode List
            episode_content = ''
            for episode_details in media_item.episode_list:
                episode_content += tv_episode_row.format(
                    season=episode_details.season,
                    episode=episode_details.episode,
                    title=episode_details.title
                )
            # Append the tile for the tv show with its content filled in
            content += tv_tile_content.format(
                title=media_item.title,
                thumbnail=media_item.thumbnail,
                story_line=media_item.story_line,
                episodes=episode_content
            )
    return content


def open_movies_page(media_list):
    # Create or overwrite the output file
    output_file = open('entertainment_center.html', 'w')

    # Replace the placeholder for the movie tiles with the actual
    # dynamically generated content
    rendered_content = main_page_content.format(
        tiles=create_media_tiles_content(media_list))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
