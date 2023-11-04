# A python library to humanize time.

---

To install you need [git](https://git-scm.com/downloads) installed. After installing it, run

```shell
pip install git+https://github.com/aiokev/human_time.git
```

---

## Simple example:
```py
from human_time import humantime as ht

print(ht.humanize(10000))
# 2 hours, 46 minutes and 40 seconds
print(ht.humanize(10000, True))
# 2h 46m 40s
```
