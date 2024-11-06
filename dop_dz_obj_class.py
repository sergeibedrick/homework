import hashlib
from time import sleep
from typing import List, Union

class User:
    """
    представляет пользователя платформы UrTube
    Attributes:
        nickname (str): Имя пользователя.
        password (int): Хэшированный пароль.
        age (int): Возраст пользователя.
    """

    def __init__(self, nickname: str, password: str, age: int) -> None:
        self.nickname = nickname
        self.password = self._hash_password(password)  # Хешируем пароль при создании
        self.age = age

    def __str__(self) -> str:
        return f"Пользователь (nickname = {self.nickname}, age = {self.age})"

    def __repr__(self) -> str:
        return self.__str__()

    def _hash_password(self, password: str) -> int:
        """Хеширует пароль с помощью SHA-256."""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

    def check_password(self, password: str) -> bool:
        """Проверяет, совпадает ли введенный пароль с хэшированным."""
        return self._hash_password(password) == self.password


class Video:
    """
    Представляет видео на платформе UrTube.

    Attributes:
        title (str): Заголовок видео.
        duration (int): Продолжительность видео в секундах.
        time_now (int): Текущее время воспроизведения (изначально 0).
        adult_mode (bool): Ограничение по возрасту (False по умолчанию).
    """

    def __init__(self, title: str, duration: int, time_now: int = 0,
                 adult_mode: bool = False) -> None:
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self) -> str:
        return f"Video(title={self.title}, duration={self.duration})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        """Сравнивает видео по названию."""
        if not isinstance(other, Video):
            return NotImplemented
        return self.title == other.title


class UrTube:
    """
    Представляет платформу UrTube.

    Attributes:
        users (List[User]): Список зарегистрированных пользователей.
        videos (List[Video]): Список доступных видео.
        current_user (Union[User, None]): Текущий авторизованный пользователь.
    """

    def __init__(self) -> None:
        self.users: List[User] = []
        self.videos: List[Video] = []
        self.current_user: Union[User, None] = None

    def log_in(self, nickname: str, password: str) -> None:
        """Авторизует пользователя."""
        for user in self.users:
            if user.nickname == nickname and user.check_password(password):
                self.current_user = user
                return
        print(
            f"Пользователь с никнеймом {nickname} и таким паролем не найден.")

    def register(self, nickname: str, password: str, age: int) -> None:
        """Регистрирует нового пользователя."""
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует.")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user  # Автоматический вход после регистрации

    def log_out(self) -> None:
        """Выходит из аккаунта."""
        self.current_user = None

    def add(self, *videos: Video) -> None:
        """Добавляет новые видео, если их еще нет на платформе."""
        for video in videos:
            if not any(existing_video == video for existing_video in
                       self.videos):  # используем __eq__ из класса Video
                self.videos.append(video)

    def get_videos(self, search_term: str) -> List[str]:
        """Возвращает список названий видео, содержащих поисковое слово."""

        return [video.title for video in self.videos if
                search_term.lower() in video.title.lower()]

    def watch_video(self, video_title: str) -> None:
        """Воспроизводит видео, если оно найдено и пользователь авторизован."""
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == video_title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                video.time_now = 0  # Сбрасываем текущее время воспроизведения
                for i in range(video.duration):
                    video.time_now += 1  # Увеличиваем время воспроизведения
                    print(
                        f"Просмотр видео '{video.title}': {video.time_now} секунда")
                    sleep(1)  # sleep импортируется в начале файла
                print("Конец видео")

                video.time_now = 0  # сбрасываем время просмотра после окончания
                return

        print(f"Видео с названием '{video_title}' не найдено.")



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')