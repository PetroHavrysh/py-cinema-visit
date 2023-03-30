from app.people.customer import Customer


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: str) -> None:
        print(f'"{movie_name}" started in hall number {self.number}.')
        for customer in customers:
            print(f'{Customer(name=customer.name, food=customer.food)} '
                  f'is watching "{movie_name}".')
        print(f'"{movie_name}" ended.')
        print(f'Cleaner {cleaning_staff} is cleaning hall number '
              f'{self.number}.')