<h1>MultiPrefixspan</h1>
Implement prefixspan algorithm for a sequence with multiple-item events, also with single0-item event.

Prefixspan
---------------------------
MultiPrefixspan  is to implement prefixspan algorithm for a sequence with multiple-item events.

Installation
---------------------------

Using pip: 
```
pip install multiprefixspan
```

Example for single event
---------------------------
Given data as follows, each element is a sequence. 
```
db = [
    [0, 1, 2, 3, 4],
    [1, 1, 1, 3, 4],
    [2, 1, 2, 2, 0],
    [1, 1, 1, 2, 2],
]
```
Execute prefixspan algorithm to find frequent patterns with the minimum support greater than or equal to 2 on db by:
```
from multiprefixspan import prefixspan_one_item_one_event

pre_object = prefixspan_one_item_one_event(db, 2)
pre_object.exect()
```
Show result:
```
pre_object.found_patterns
```
```
{'[0]': 2,
 '[1]': 4,
 '[1, 2]': 3,
 '[1, 2, 2]': 2,
 '[1, 3]': 2,
 '[1, 3, 4]': 2,
 '[1, 4]': 2,
 '[1, 1]': 2,
 '[1, 1, 1]': 2,
 '[2]': 3,
 '[2, 2]': 2,
 '[3]': 2,
 '[3, 4]': 2,
 '[4]': 2}
```

Example for multiple events
---------------------------
Given data as follows, each element is a sequence, each element in a sequence may have more than one items.
```
db = [[{'a'}, {'a', 'b', 'c'}, {'a', 'c'}, {'d'}, {'c', 'f'}],
      [{'a', 'd'}, {'c'}, {'b', 'c'}, {'a', 'e'}],
      [{'e', 'f'}, {'a', 'b'}, {'d', 'f'}, {'c'}, {'b'}],
      [{'e', 'g'}, {'a', 'f'}, {'c'}, {'b'}, {'c'}],
      [{'a'}, {'g', 'h'}, {'f', 'e'}, {'b', 'c', 'e'}, {'a', 'b', 'c'}]
      ]
```
Execute prefixspan algorithm to find frequent patterns with the minimum support greater than or equal to 2 on db by:
```
from multiprefixspan import prefixspan_multiple_items_one_event

pre_object = prefixspan_multiple_items_one_event(db, 2)
pre_object.exect()
```

Show the first ten patterns (unordered):
```
pre_object.found_patterns[:10]
```
```
[([{'f'}], 4),
 ([{'f'}, {'a'}], 2),
 ([{'f'}, {'a', 'b'}], 2),
 ([{'f'}, {'a', 'b'}], 2),
 ([{'e', 'f'}], 2),
 ([{'e', 'f'}, {'a'}], 2),
 ([{'e', 'f'}, {'a', 'b'}], 2),
 ([{'e', 'f'}, {'a', 'b'}], 2),
 ([{'e', 'f'}, {'b'}], 2),
 ([{'e', 'f'}, {'b'}, {'b'}], 2)]
```

Reference
---------------------------
1. Pei, J., Han, J., Mortazavi-Asl, B., Pinto, H., Chen, Q., Dayal, U., & Hsu, M. (2001). PrefixSpan,: mining sequential patterns efficiently by prefix-projected pattern growth. Proceedings 17th International Conference on Data Engineering, 215-224.
