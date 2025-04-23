from coffee_builder import CoffeeBuilder
if __name__ == "__main__":
    builder = CoffeeBuilder()
    coffee = (
        builder
        .use_house_blend()
        .add_mocha()
        .add_whip()
        .build()
    )

    print(coffee.get_description())  # Output: House Blend Coffee, Mocha, Whip
    print(f"${coffee.get_cost():.2f}")