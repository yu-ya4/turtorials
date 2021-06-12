from sudachipy import tokenizer
from sudachipy import dictionary


tokenizer_obj = dictionary.Dictionary().create()


mode = tokenizer.Tokenizer.SplitMode.C
print("mode C")
[print(m.surface()) for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家公務員']


print("mode B")
mode = tokenizer.Tokenizer.SplitMode.B
[print(m.surface()) for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家', '公務員']


print("mode A")
mode = tokenizer.Tokenizer.SplitMode.A
[print(m.surface()) for m in tokenizer_obj.tokenize("国家公務員", mode)]
# => ['国家', '公務', '員']


# Morpheme information

m = tokenizer_obj.tokenize("食べ", mode)[0]

print(m.surface()) # => '食べ'
print(m.dictionary_form()) # => '食べる'
print(m.reading_form()) # => 'タベ'
print(m.part_of_speech()) # => ['動詞', '一般', '*', '*', '下一段-バ行', '連用形-一般']


# Normalization

print(tokenizer_obj.tokenize("附属", mode)[0].normalized_form())
# => '付属'
print(tokenizer_obj.tokenize("SUMMER", mode)[0].normalized_form())
# => 'サマー'
print(tokenizer_obj.tokenize("シュミレーション", mode)[0].normalized_form())
# => 'シミュレーション'
