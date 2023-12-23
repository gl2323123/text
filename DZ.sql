CREATE TABLE IF NOT EXISTS Musicain (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS Genre (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS GenresMusicain (
id SERIAL PRIMARY KEY,
musicain_id INT NOT NULL references Musicain(id),
genre_id INT NOT NULL references Genre(id)
);

CREATE TABLE IF NOT EXISTS Album (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL,
year_of_realese DECIMAL(4,0) NOT NULL 
);

CREATE TABLE IF NOT exists MusicainAlbum (
id SERIAL PRIMARY KEY,
musicain_id INT NOT NULL references Musicain(id),
album_id INT NOT NULL references Album(id)
);

CREATE TABLE IF NOT exists Track(
id SERIAL PRIMARY KEY,
name VARCHAR(40) not null,
album_id INT NOT NULL REFERENCES Album(id),
times DECIMAL(2,2) NOT NULL
)


CREATE TABLE IF NOT EXISTS Collection (
id SERIAL PRIMARY KEY,
name varchar(40) NOT NULL,
year_of_relase decimal(4,0)
)

CREATE TABLE IF NOT EXISTS CollectionTrack (
id SERIAL PRIMARY KEY,
collection_id INT NOT NULL references Collection(id),
track_id INT NOT NULL REFERENCES track(id)
)
