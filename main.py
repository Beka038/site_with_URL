from flask import Flask, render_template
from random import randint, choice

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("index.html")


@app.route("/random_facts")
def random_fact1():
    facts = [
        "Самый дорогой хот-дог в мире приготовили в Нью-Йорке за 69 долларов.",
        "Молоко бегемотов розового цвета.",
        "По статистике, более 7000 человек получают травмы, упав со стула.",
        "Собаки могут лаять с акцентом.",
        "Пингвин может прыгнуть на три метра в высоту.",
        "15 граммов адреналина с избытком хватило бы для всех людей земного шара.",
        "Дельфины убивают акул, идя с ними на таран «лоб в лоб».",
        "Личный парикмахер Папы Римского зарабатывает 250 000 долларов в год.",
        "Около 27 тонн космической пыли падает на Землю каждый день.",
        "Ежегодно в мире попадает на свалки 40 тысяч тонн сломанных или устаревших сотовых телефонов и аккумуляторов к ним.",
        "Кошки поддерживают равновесие с помощью усов.",
        "Арахис используется при создании динамита.",
        "В Австралии больше кроликов, чем людей в Китае."
    ]
    
    random_fact = choice(facts)
    return render_template("random_fact.html", random_fact=random_fact)

@app.route("/random_numbers")
def random_num():
    number = randint(0, 10)
    return render_template("random_number.html", number=number)

app.run(debug=True)
