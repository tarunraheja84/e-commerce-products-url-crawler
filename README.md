# 🕷️ E-commerce Product URL Crawler

## 📌 Overview

This project implements an **asynchronous web crawler** that discovers and collects **product URLs** from various **e-commerce websites**. It is designed to be scalable, efficient, and capable of handling different website structures.


## 🎯 Objective

To create a web crawler that:
- Automatically discovers product page URLs from different e-commerce domains.
- Handles variations in URL patterns like `/product/`, `/item/`, `/p/`, or even regex-based patterns.
- Is efficient, robust, and scalable to work on hundreds of websites.


## 🌐 Supported Domains

The following e-commerce domains are supported as a minimum:

- [https://www.virgio.com/](https://www.virgio.com/)
- [https://www.tatacliq.com/](https://www.tatacliq.com/)
- [https://nykaafashion.com/](https://nykaafashion.com/)
- [https://www.westside.com/](https://www.westside.com/)

The crawler can be extended to more domains by modifying the configuration file.


## ⚙️ How It Works

1. **Load Configuration:** Loads the list of start URLs, URL patterns, and concurrency limits from `config.yaml`.
2. **Crawl Pages:** Starts crawling pages asynchronously using `aiohttp` and `asyncio`.
3. **Extract Links:** Parses HTML content with BeautifulSoup to find all `<a>` and `<link>` tags.
4. **Filter by Domain & Pattern:** Retains only links that match the target domain and known product path patterns.
5. **Save Output:** Saves all matched product URLs to a structured `output.json` file grouped by domain.

---

## 🧰 Features

- ✅ Asynchronous Crawling using `aiohttp` for high performance
- ✅ Custom URL pattern matching (both static and regex support)
- ✅ Domain-restricted crawling to avoid going offsite
- ✅ Duplicate URL prevention using a visited set
- ✅ Output in JSON format for easy integration or analysis

---

## 🗂️ Project Structure

```bash
.
├── app.py                    # Main application script
├── config.yaml               # Configuration file for URLs, patterns, limits
├── utils/
│   ├── fetch_html.py         # Async HTML fetcher
│   ├── helper_functions.py   # URL pattern matcher, domain checker
│   ├── load_config.py        # Loads config.yaml
│   └── output.py             # Saves output JSON
├── output.json               # Output file with matched product URLs
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```


## 🚀 How to Run
1. **Clone the repository**
```
git clone https://github.com/your-username/ecommerce-url-crawler.git
cd ecommerce-url-crawler
```

2. **Install dependencies**
```
pip install -r requirements.txt
```


3. **Run the crawler**
```
python app.py
```

Once executed, the script will create output.json containing all discovered product URLs, grouped by domain.



## 📦 Output Format
The output will be saved in output.json with the structure:

```
{
  "www.virgio.com": [
    "https://www.virgio.com/product/abc",
    "https://www.virgio.com/product/xyz"
  ],
  "www.tatacliq.com": [
    "https://www.tatacliq.com/item/123",
    ...
  ]
}
```

## ✅ Benefits and Use Cases
🔍 Automate product page discovery from multiple websites

📦 Useful for price comparison engines, scrapers, or market analysis tools

📈 Scalable to handle hundreds of sites with deep hierarchies

🛠️ Easily customizable for additional patterns or domains

