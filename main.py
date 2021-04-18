import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import *
from googletrans import Translator

class TranslatorApp(Widget):
	def __init__(self, **kwargs):
		super(TranslatorApp, self).__init__(**kwargs)
		self.translator = Translator()
		
		#background
		with self.canvas:
			Color(rgba=(0, 0.5, 0.5, 1))
			Rectangle(size=(720, 1440))
			
		#language
		self.languages = ["Arabic", "Bengali",  "Chinese", "Dutch", "English", "French", "German", "Italian", "Japanese", "Korean", "Latin", "Russian", "Spanish", "Turkish", "Urdu"]
		self.languageCodes = ["ar", "bn", "zh", "nl", "en", "fr", "de", "it", "ja", "ko", "la", "ru", "es", "tr", "ur"]
		
		self.num = len(self.languages)
		
		#heading
		head = Label(text="Translator", font_size=100, color=(1, 1, 0, 1), pos=(320, 1120))
		self.add_widget(head)
		
		#language selection
		self.fromButton = Button(text="Select a language", pos=(100, 920), size=(400, 1440/self.num), color=(1, 1, 0, 1), font_size=40, background_color=(0, 1, 1, 1))
		self.fromButton.bind(on_press=self.select)
		self.add_widget(self.fromButton)
		
		self.toButton = Button(text="Select language to translate to", pos=(100, 600), size=(500, 1440/self.num), color=(1, 1, 0, 1), font_size=35, background_color=(0, 1, 1, 1))
		self.toButton.bind(on_press=self.select)
		self.add_widget(self.toButton)
		
		#word
		self.add_widget(Label(text="Enter a word:", font_size=30, color=(1, 1, 0, 1), pos=(100, 820)))
		self.entrybox = TextInput(multiline=True, pos=(100, 750), size=(500, 80))
		self.add_widget(self.entrybox)
		
		#translation
		self.translation = Label(text="", font_size=50, color=(1, 1, 0, 1), pos=(200, 450))
		self.add_widget(self.translation)
		
		#translate button
		self.translateBtn = Button(text="Translate", pos=(200, 350), size=(300, 70), color=(1, 1, 0, 1), font_size=50, background_color=(0, 1, 1, 1))
		self.translateBtn.bind(on_press=self.select)
		self.add_widget(self.translateBtn)
		
		#buttons
		x, y = 750, 1440 - (1440/self.num)
		self.btn = []
		for i in range(self.num):
			self.btn.append(Button(text=self.languages[i], pos=(x, y), size=(300, 1440/self.num), color=(1, 1, 0, 1), font_size=40, background_color=(0, 1, 1, 1)))
			self.btn[i].bind(on_press=self.select)
			self.add_widget(self.btn[i])
			y -= 1440/self.num
			
		self.flag = 0
		self.fromLang = ""
		self.toLang = ""
			
	def select(self, instance):
		if instance == self.fromButton:
			self.flag = 1
			for i in range(self.num):
				if self.btn[i].pos[0] == 750:
					self.btn[i].pos = (300, self.btn[i].pos[1])
				elif self.btn[i].pos[0] == 300:
					self.btn[i].pos = (750, self.btn[i].pos[1])
		
		elif instance == self.toButton:
			self.flag = 2
			for i in range(self.num):
				if self.btn[i].pos[0] == 750:
					self.btn[i].pos = (300, self.btn[i].pos[1])
				elif self.btn[i].pos[0] == 300:
					self.btn[i].pos = (750, self.btn[i].pos[1])
				
		elif instance in self.btn:
			if self.flag == 1:
				self.fromButton.text = instance.text
			elif self.flag == 2:
				self.toButton.text = instance.text
			
			for i in range(self.num):
				self.btn[i].pos = (750, self.btn[i].pos[1])
		
		elif instance == self.translateBtn:
			for i in range(self.num):
				if self.fromButton.text == self.btn[i].text:
					self.fromLang = self.languageCodes[i]
				
				if self.toButton.text == self.btn[i].text:
					self.toLang = self.languageCodes[i]
					
			self.translation.text = self.translator.translate(self.entrybox.text, dest=self.toLang, src=self.fromLang).text

class MyApp(App):
	def build(self):
		return TranslatorApp()
		
if __name__ == "__main__":
	MyApp().run()
