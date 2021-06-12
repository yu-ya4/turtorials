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
