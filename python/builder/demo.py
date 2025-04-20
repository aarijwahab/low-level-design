from director import Director
from builder import Builder
from concretebuilder import ConcreteBuilder1

class Demo():
    def run(self):
        director: Director = Director()
        builder: Builder = ConcreteBuilder1()
        director.builder = builder

        print("Standard basic product")
        director.build_mvp()
        builder.product.listParts()

        print("\n")

        print("Full featured product")
        director.build_full_featured_product()
        builder.product.listParts()

        print("\n")

        print("Custom product: ")
        builder.produce_part_a()
        builder.produce_part_b()
        builder.product.listParts()

if __name__ == "__main__":
    demo = Demo()
    demo.run()