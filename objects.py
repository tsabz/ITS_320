

class Dog:
    bark = 'roof roof'
    walking = 'boom boom'

    def quack(self):
        print(self.bark)

    def walk(self):
        print(self.walking)


def main():
    simba = Dog()
    simba.quack()
    simba.walk()


if __name__ == '__main__':
    main()
