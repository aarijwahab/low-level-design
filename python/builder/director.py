from __future__ import annotations
from builder import Builder

class Director:
    def __init__(self):
        self._builder = None # Private builder
    
    @property
    def builder(self) -> Builder:
        return self._builder
    
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
    
    def build_mvp(self) -> None:
        self.builder.produce_part_a()
    
    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()
