class Media(object):
    """ Main parent class for storing common information about media items
    Attributes:
        title: stores title for media item as a string
        story_line: stores the story line for the media item as string
        thumbnail: stores the url to the thumbnail / poster image online
        media_type: stores the type of media item ie TC Show or Movie
    """

    def __init__(self, title, story_line, thumbnail, media_type):
        """ Initialises Media with title, story_line, thumbnail, media_type """
        self.title = title
        self.story_line = story_line
        self.thumbnail = thumbnail
        self.media_type = media_type


class Movie(Media):
    """ Class for storing information about a movie
    Inherits from Media class
    Attributes:
        trailer_url: url to YouTube trailer for movie
        duration: Integer for movie length in minutes
	"""

    def __init__(self, title, story_line, duration, thumbnail, trailer_url):
        """ Initialises Movie class"""
        Media.__init__(self, title, story_line, thumbnail, 'Movie')
        self.trailer_url = trailer_url
        self.duration = duration

    def __getitem__(self, i):
        return self[i]


class TvSeason(Media):
    """ Class for storing information about a TV Season
    Inherits from Media class
    Attributes:
        episode_list: list of TV Episode objects
    """

    def __init__(self, title, story_line, thumbnail, episode_list):
        """ Initialises TV Season class"""
        Media.__init__(self, title, story_line, thumbnail, 'TV Show')
        self.episode_list = episode_list


class TVEpisode():
    """ Class for details relating to an episode of a TV Season
    Attributes:
        title: string for title of episode
        season: integer for season number
        episode: integer for episode number
    """
    def __init__(self, title, season, episode):
        """ Inits TV Episode class"""
        self.title = title
        self.season = season
        self.episode = episode
