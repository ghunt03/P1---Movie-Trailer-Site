import media
import create_page


# media_list stores movies and tv series
media_list = []

media_list.append(media.Movie(
    "Fast 5",
    "Dominic Toretto and his crew of street racers plan a massive heist to \
    buy their freedom while in the sights of a powerful Brazilian drug lord \
    and a dangerous federal agent.",
    131,
    "https://upload.wikimedia.org/wikipedia/en/thumb/0/0c/Fast_Five_poster.jpg/220px-Fast_Five_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=bf4oDjHUmkY"))

media_list.append(media.Movie(
    "Fast & Furious 6",
    "Hobbs has Dominic and Brian reassemble their crew to take down a team \
    of mercenaries: Dominic unexpectedly gets convoluted also facing his \
    presumed deceased girlfriend, Letty.",
    130,
    "http://ia.media-imdb.com/images/M/MV5BMTM3NTg2NDQzOF5BMl5BanBnXkFtZTcwNjc2NzQzOQ@@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=C_puVuHoR6o"))

media_list.append(media.Movie(
    "Furious 7",
    "After defeating international terrorist Owen Shaw, Dominic Toretto \
    (Vin Diesel), Brian O'Conner (Paul Walker) and the rest of the crew have \
    separated to return to more normal lives. However, Deckard Shaw \
    (Jason Statham), Owen's older brother, is thirsty for revenge",
    137,
    "http://ia.media-imdb.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE@._V1_SX214_AL_.jpg",  # noqa
    "https://www.youtube.com/watch?v=wGtAvTpNcxc"))

# tv_episodes stores episodes for a tv season
tv_episodes = []
tv_episodes.append(media.TVEpisode("Pilot", 1, 1))
tv_episodes.append(media.TVEpisode("Honor Thy Father", 1, 2))
tv_episodes.append(media.TVEpisode("Lone Gunmen", 1, 3))
tv_episodes.append(media.TVEpisode("An Innocent Man", 1, 4))
tv_episodes.append(media.TVEpisode("Damaged", 1, 5))
tv_episodes.append(media.TVEpisode("Legacies", 1, 6))
tv_episodes.append(media.TVEpisode("Muse of Fire", 1, 7))
tv_episodes.append(media.TVEpisode("Vendetta", 1, 8))
tv_episodes.append(media.TVEpisode("Year's End", 1, 9))
tv_episodes.append(media.TVEpisode("Burned", 1, 10))
tv_episodes.append(media.TVEpisode("Trust But Verify", 1, 11))
tv_episodes.append(media.TVEpisode("Vertigo", 1, 12))
tv_episodes.append(media.TVEpisode("Betrayal", 1, 13))
tv_episodes.append(media.TVEpisode("The Odyssey", 1, 14))
tv_episodes.append(media.TVEpisode("Dodger", 1, 15))
tv_episodes.append(media.TVEpisode("Dead to Rights", 1, 16))
tv_episodes.append(media.TVEpisode("The Huntress Returns", 1, 17))
tv_episodes.append(media.TVEpisode("Salvation", 1, 18))
tv_episodes.append(media.TVEpisode("Unfinished Business", 1, 19))
tv_episodes.append(media.TVEpisode("Home Invasion", 1, 20))
tv_episodes.append(media.TVEpisode("The Undertaking", 1, 21))
tv_episodes.append(media.TVEpisode("Darkness on the Edge of Town", 1, 22))
tv_episodes.append(media.TVEpisode("Sacrifice", 1, 23))
tv_episodes.append(media.TVEpisode("City of Heroes", 2, 1))
tv_episodes.append(media.TVEpisode("Identity", 2, 2))
tv_episodes.append(media.TVEpisode("Broken Dolls", 2, 3))
tv_episodes.append(media.TVEpisode("Crucible", 2, 4))
tv_episodes.append(media.TVEpisode("League of Assassins", 2, 5))
tv_episodes.append(media.TVEpisode("Keep Your Enemies Closer", 2, 6))
tv_episodes.append(media.TVEpisode("State vs Queen", 2, 7))
tv_episodes.append(media.TVEpisode("The Scientist", 2, 8))
tv_episodes.append(media.TVEpisode("Three Ghosts", 2, 9))
tv_episodes.append(media.TVEpisode("Blast Radius", 2, 10))
tv_episodes.append(media.TVEpisode("Blind Spot", 2, 11))
tv_episodes.append(media.TVEpisode("Tremors", 2, 12))
tv_episodes.append(media.TVEpisode("Heir to the Demon", 2, 13))
tv_episodes.append(media.TVEpisode("Time of Death", 2, 14))
tv_episodes.append(media.TVEpisode("The Promise", 2, 15))
tv_episodes.append(media.TVEpisode("Suicide Squad", 2, 16))
tv_episodes.append(media.TVEpisode("Birds of Prey", 2, 17))
tv_episodes.append(media.TVEpisode("Deathstroke", 2, 18))
tv_episodes.append(media.TVEpisode("The Man Under the Hood", 2, 19))
tv_episodes.append(media.TVEpisode("Seeing Red", 2, 20))
tv_episodes.append(media.TVEpisode("City of Blood", 2, 21))
tv_episodes.append(media.TVEpisode("Streets of Fire", 2, 22))
tv_episodes.append(media.TVEpisode("Unthinkable", 2, 23))

media_list.append(media.TvSeason(
    "Arrow",
    "Arrow is a modern retelling of the DC Comic character Green Arrow. \
    Multi-millionaire playboy Oliver Queen is missing, and presumed dead \
    after a shipwreck at sea. He is found five years later, having survived \
    on a desert island off his wits and by mastering the bow and arrow. \
    When he returns to Starling City however, he discovers that it is rife \
    with corruption and crime. Oliver decides to put his skills to use by \
    taking on the persona of Arrow and becoming the vigilante that Starling \
    City needs.",
    "http://ia.media-imdb.com/images/M/MV5BMTg3OTc0NzkyOV5BMl5BanBnXkFtZTgwMDMwMTM3MjE@._V1_SX214_AL_.jpg",  # noqa
    tv_episodes))
tv_episodes = []
tv_episodes.append(media.TVEpisode("Pilot", 1, 1))
tv_episodes.append(media.TVEpisode("0-8-4", 1, 2))
tv_episodes.append(media.TVEpisode("The Asset", 1, 3))
tv_episodes.append(media.TVEpisode("Eye Spy", 1, 4))
tv_episodes.append(media.TVEpisode("Girl in the Flower Dress", 1, 5))
tv_episodes.append(media.TVEpisode("FZZT", 1, 6))
tv_episodes.append(media.TVEpisode("The Hub", 1, 7))
tv_episodes.append(media.TVEpisode("The Well", 1, 8))
tv_episodes.append(media.TVEpisode("Repairs", 1, 9))
tv_episodes.append(media.TVEpisode("The Bridge", 1, 10))
tv_episodes.append(media.TVEpisode("The Magical Place", 1, 11))
tv_episodes.append(media.TVEpisode("Seeds", 1, 12))
tv_episodes.append(media.TVEpisode("T.R.A.C.K.S", 1, 13))
tv_episodes.append(media.TVEpisode("T.A.H.I.T.I", 1, 14))
tv_episodes.append(media.TVEpisode("Yes Men", 1, 15))
tv_episodes.append(media.TVEpisode("End of the Beginning", 1, 16))
tv_episodes.append(media.TVEpisode("Turn, Turn, Turn", 1, 17))
tv_episodes.append(media.TVEpisode("Providence", 1, 18))
tv_episodes.append(media.TVEpisode("The Only Light in the Darkness", 1, 19))
tv_episodes.append(media.TVEpisode("Nothing Personal", 1, 20))
tv_episodes.append(media.TVEpisode("Rag Tag", 1, 21))
tv_episodes.append(media.TVEpisode("Beginning of the End", 1, 22))
media_list.append(media.TvSeason(
    "Agents of S.H.I.E.L.D.",
    "The missions of the Strategic Homeland Intervention, Enforcement and \
    Logistics Division.",
    "http://ia.media-imdb.com/images/M/MV5BMTkwODYyMjgzOV5BMl5BanBnXkFtZTgwODAzMTE5MjE@._V1_SX214_AL_.jpg",  # noqa
    tv_episodes))

# create and open page based on media_list array
create_page.open_movies_page(media_list)
