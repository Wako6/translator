from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import concurrent.futures

EN_FR_MODEL_NAME = "Helsinki-NLP/opus-mt-en-fr"
FR_EN_MODEL_NAME = "Helsinki-NLP/opus-mt-fr-en"

_pool = concurrent.futures.ThreadPoolExecutor()

def load_en_fr_model():
    tokenizer = AutoTokenizer.from_pretrained(EN_FR_MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(EN_FR_MODEL_NAME)

    return (tokenizer, model)

def load_fr_en_model():
    tokenizer = AutoTokenizer.from_pretrained(FR_EN_MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(FR_EN_MODEL_NAME)

    return (tokenizer, model)


class Translate:

    def __init__(self) -> 'Translate':
        self.en_fr_model = _pool.submit(load_en_fr_model)
        self.fr_en_model = _pool.submit(load_fr_en_model)

    def translate_en_to_fr(self, sentence):
        tokenizer, model = self.en_fr_model.result()

        tmp_sentence = sentence if sentence[-1:] == "." else sentence + "."

        input_ids = tokenizer(
            tmp_sentence,
            return_tensors="pt"
        ).input_ids
        outputs = model.generate(input_ids)

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result if sentence[-1:] == "." else result[:-1]

    def translate_fr_to_en(self, sentence):
        tokenizer, model = self.fr_en_model.result()

        tmp_sentence = sentence if sentence[-1:] == "." else sentence + "."

        input_ids = tokenizer(
            tmp_sentence,
            return_tensors="pt"
        ).input_ids
        outputs = model.generate(input_ids)

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result if sentence[-1:] == "." else result[:-1]


if __name__ == '__main__':
    t = Translate()

    print(t.translate_fr_to_en("Ma maison est jolie."))
    print(t.translate_fr_to_en("quels montants ont été attribués et quelles sommes ont été effectivement utilisées dans chaque État membre? 4."))
    print(t.translate_en_to_fr("Model on translating legal text from French to English."))
    print(t.translate_en_to_fr("I hate you."))