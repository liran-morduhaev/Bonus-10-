from Cat import Cat
from Fish import Fish
from Spider import Spider

if __name__ == "__main__":
# Create instances
    spider = Spider()
    cat = Cat("Mitzi")
    fish = Fish()
    fish.set_name("Nemo")

    # Run spider methods
    print()
    spider.walk()
    spider.eat()

    # Run cat methods
    print()
    cat.walk()
    cat.eat()
    cat.play()

    # Run fish methods
    print()
    fish.walk()
    fish.eat()
    fish.play()