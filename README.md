# View the actual news about cryptocurrencies

---
## Installation
---

```console
pip install requests
pip install bs4
pip install lxml
```

---
## Usage
 User can get actual news about certain cryptocurrency by typing the name of cryptocurrency.

---
## Example

```python
from coinScrapper import Scrapper

test = Scrapper()
user_input = "Please, input the name of cryptocurrency to see all actual related information: "
test.scrap_articles(user_input)
```

--- 
## License
Rakhat Yerezhepov, 2021
