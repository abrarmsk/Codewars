def song_decoder(song):
    song_lyrics = song.split('WUB')
    words =[]
    for word in song_lyrics:
        if word == '':
            continue
        words.append(word)

        song =' '.join(words)

    return song
