from src.surface.SurfaceBase import SurfaceBase

class Scene(SurfaceBase):
    def __init__(self):
        super().__init__()
    def on_enter(self): ...
    def on_update(self): ...
    def on_draw(self): ...
    def on_input(self, event): ...
    def on_exit(self): ...
    def update_surface(self):
        super().update_surface()