import threading
import time
import random

class Bank:
    """Класс, представляющий банк с балансом и блокировкой."""
    def __init__(self, initial_balance: int = 0) -> None:
        """Инициализирует банк."""
        self.balance: int = initial_balance
        self.lock: threading.Lock = threading.Lock()

    def deposit(self):
        """Совершает 100 транзакций пополнения."""
        for _ in range(100):
            amount: int = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        """Совершает 100 транзакций снятия."""
        for _ in range(100):
            amount: int = random.randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=bk.deposit) # передаем методы объекта, а не класса
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')