from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

map = {
    "English": "en",
    "Hindi": "hi"
}

class Language:
    
    def __init__(self,name) -> None:
        
        self.name = name
    def __repr__(self) -> str:
        return f"{self.name}"
    def addLanguage(self, name, code):
        self.map[name] = code
    
    

class English(Language):    
    
    def __init__(self) -> None:
        super().__init__("English")
    def __repr__(self) -> str:
        return f"{self.name}"
    @staticmethod
    def TranslateTo(text, language):
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-" + map[language])
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-" + map[language])
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model.generate(**inputs)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return decoded
    
class Hindi(Language):
    def __init__(self) -> None:
        super().__init__("Hindi")
    def __repr__(self) -> str:
        return f"{self.name}"
    @staticmethod
    def TranslateTo(self, text, language):
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-hi-" + map[language])
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-hi" + map[language])
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model.generate(**inputs)
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return decoded
