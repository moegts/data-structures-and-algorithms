from stack_queue_animal_shelter import __version__
from stack_queue_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog


def test_version():
    assert __version__ == '0.1.0'


def test_enqueue_cat():
    animalshelter = AnimalShelter()
    yuumi = Cat('yuumi')
    animalshelter.enqueue(yuumi)
    assert animalshelter.frontcat.name == 'yuumi'


def test_enqueue_dog():
    animalshelter = AnimalShelter()
    roxi = Dog('roxi')
    animalshelter.enqueue(roxi)
    assert animalshelter.frontdog.name == 'roxi'

def test_dequeue_cat():
    animalshelter = AnimalShelter()
    yuumi, lulu = Cat('yuumi'), Cat('lulu')
    animalshelter.enqueue(yuumi) ; animalshelter.enqueue(lulu)
    animalshelter.dequeue('cat')
    assert animalshelter.frontcat.name =='lulu'



def test_dequeue_dog():
    animalshelter = AnimalShelter()
    flanker, sasha = Dog('flanker'), Dog('sasha')
    animalshelter.enqueue(sasha) ; animalshelter.enqueue(flanker)
    animalshelter.dequeue('dog')
    assert animalshelter.frontdog.name == 'flanker'

def test_enqueue_dog_and_cat():
    animalshelter = AnimalShelter()
    yuumi, roxi = Cat('yuumi'), Dog('roxi')
    animalshelter.enqueue(roxi) ; animalshelter.enqueue(yuumi)
    assert animalshelter.frontdog.name == 'roxi'
    assert animalshelter.frontcat.name == 'yuumi'


def test_null_case():
    animalshelter = AnimalShelter()
    flanker,sasha = Dog('flanker'), Dog('sasha')
    animalshelter.enqueue(sasha) ; animalshelter.enqueue(flanker)
    animalshelter.dequeue('dog') ; animalshelter.dequeue('dog')
    assert animalshelter.dequeue('dog') == 'null'