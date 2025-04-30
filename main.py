from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        # Set window size for testing
        Window.size = (360, 640)
        
        # Create a layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Create buttons
        btn1 = Button(text='Button 1', size_hint=(1, 0.2))
        btn2 = Button(text='Button 2', size_hint=(1, 0.2))
        btn3 = Button(text='Button 3', size_hint=(1, 0.2))
        
        # Add buttons to layout
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        
        return layout

if __name__ == '__main__':
    MyApp().run() 