from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
import json


class KivyApp(App):
    firebase_url = "https://adotefoz-dd3ef-default-rtdb.firebaseio.com/.json"

    def build(self):
        box_layout = BoxLayout()
        box_layout.orientation = 'vertical'
        button_get = Button(text="Get Data")
        button_get.bind(on_press=self.create_get)

        button_post = Button(text="Post Data")
        button_post.bind(on_press=self.create_post)

        button_put = Button(text="Put Data")
        button_put.bind(on_press=self.create_put)

        button_delete = Button(text="Delete Data")
        button_delete.bind(on_press=self.create_delete)

        box_layout.add_widget(button_get)
        box_layout.add_widget(button_post)
        box_layout.add_widget(button_put)
        box_layout.add_widget(button_delete)

        return box_layout

    def create_patch(self, *args):
        print("BUTTON CLICKED")
        json_data = '{"url": "amazon.com", "age": "17 years old"}'
        res = requests.patch(url=self.firebase_url, json=json.loads(json_data))
        print(res)

    def create_get(self, *args):
        print("BUTTON GET CLICKED")
        res = requests.get(url=self.firebase_url)
        print(res.json())

    def create_post(self, *args):
        print("BUTTON CLICKED")
        json_data = '{"age": "36 years old"}'
        res = requests.post(url=self.firebase_url, json=json.loads(json_data))
        print(res.json())

    def  create_put(self, *args):
        firebase_put_url = "https://adotefoz-dd3ef-default-rtdb.firebaseio.com/Tabela2.json"
        print("BUTTON CLICKED")
        json_data = '{"age": "21 years old"}'
        res = requests.put(url=firebase_put_url, json=json.loads(json_data))
        print(res)

    def create_delete(self, *args):
        print("BUTTON CLICKED")
        delete_url = "https://adotefoz-dd3ef-default-rtdb.firebaseio.com/"
        res = requests.delete(url=delete_url+"Table2/Tabela2/age" "url"+".json")
        print(res.json())


if __name__ == '__main__':
    KivyApp().run()
