from googletrans import Translator

transaltor = Translator()

text = 'The quick brown fox jumps over the lazy dog'

destination = ['ko','ar','es','hi','fr','nl','ru']
answer = []

for end in destination:
    final = transaltor.translate(text,dest=end)
    print("The text is in",final.src, "which means",final.text, "in",final.dest)
    answer.append(final.dest)

for start in answer:
    result = transaltor.detect(start)
    print("This is in",result.lang)    
