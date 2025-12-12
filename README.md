Music Library System (Song Class)
Description

This project implements a Song class for a simplified music library system using Python. Each Song instance represents an individual track, while the class itself maintains shared, aggregate data about the entire song library.

The system demonstrates practical use of instance attributes, class attributes, and class methods to track global insights such as total song count, unique artists and genres, and per-artist and per-genre song totals. This mirrors real-world analytics and reporting behavior in music streaming platforms.

Features

Create individual Song objects with a name, artist, and genre

Automatically track total number of songs created

Maintain a unique list of all artists

Maintain a unique list of all genres

Track number of songs per genre

Track number of songs per artist

Uses class methods to manage shared state cleanly

Fully tested using pytest

Technologies Used

Python 3

Pytest

Installation

Clone the repository from GitHub

Navigate into the project directory

Install pytest if it is not already installed

Example commands:
git clone https://github.com/learn-co-curriculum/python-music-library-system-lab

cd python-music-library-system-lab
sudo apt install python3-pytest

Usage

Create Song instances to automatically populate the music library data.

Example:
from song import Song
Song("99 Problems", "Jay Z", "Rap")
Song("Halo", "Beyonce", "Pop")
Song("Smells Like Teen Spirit", "Nirvana", "Rock")

Access class-level analytics:
Song.count
Song.genres
Song.artists
Song.genre_count
Song.artist_count

How It Works

Instance attributes (name, artist, genre) describe a single song. Class attributes store shared data across all Song instances. Class methods are responsible for mutating shared state. The init method acts as the trigger point that updates all tracking structures whenever a new Song is created.

This design ensures a single source of truth for library-wide data and clean separation between instance-level and class-level responsibilities.

Running Tests

Run the test suite using pytest from the project root directory.

Command:
pytest

The tests validate correct song initialization, accurate total counts, proper tracking of artists and genres, and correct per-artist and per-genre totals.

Project Structure

song.py contains the Song class implementation
song_test.py contains pytest test cases
conftest.py contains pytest configuration
README.md contains project documentation

Notes

This project follows a test-driven mindset where the test suite defines the expected public interface. The implementation intentionally matches the test contract exactly, including attribute naming. The focus of this lab is reinforcing understanding of object-oriented design, class attributes, and class methods.