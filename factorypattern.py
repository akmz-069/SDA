class Burger:
    def __init__(self,ingredients):
        self.ingredients=ingredients
    def print(self):
        print(self.ingredients)
    
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["bhakku pauroti","cheese","patty "]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["bhakku pauroti","cheese","patty ","tomato","lettuce"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients= ["bhakku pauroti","special-sauce","patty "]
        return Burger(ingredients)
    
burgerFactory= BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()


        