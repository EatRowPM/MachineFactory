from src.core.scene.scene import Scene
from src.core.tool.draw import draw_text
from src.core.scene.save_scene import *
from src.core.map.ground import Ground
from pygame import KEYDOWN

class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.scene_manager = get_scene('manager')
        self.ground_map = Ground()

    def on_enter(self):
        print('进入游戏')

    def on_update(self):
        print('游戏正在运行')

    def on_input(self, event):
        if event.type == KEYDOWN:
            self.scene_manager.switch_scene('menu')

    def on_draw(self):
        draw_text('游戏绘图')

    def on_exit(self):
        print('退出游戏')