from Domain import Client, Movie
from Service.RentalService import RentalService
from Repository.FileClientRepo import FileClientRepo
from Repository.FileMovieRepo import FileMovieRepo
from Repository.MovieRepo import MovieRepo
from Repository.ClientRepo import ClientRepo
from Repository.RentalRepo import RentalRepo
from Service.MoviesService import MoviesService
from Service.ClientsService import ClientsService
from Presentation.Console import UI


if __name__ == '__main__':
    moviesPath = "./Repository/movies.txt"
    clientsPath = "./Repository/clients.txt"
    movieRepo = FileMovieRepo(moviesPath)
    clientRepo = FileClientRepo(clientsPath)
    rentalRepo = RentalRepo()
    moviesService = MoviesService(movieRepo)
    clientsService = ClientsService(clientRepo)
    rentalsService = RentalService(clientRepo, movieRepo, rentalRepo)
    console = UI(moviesService, clientsService, rentalsService)
    console.run()
