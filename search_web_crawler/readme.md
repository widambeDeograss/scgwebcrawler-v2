<h1>
  <a href="http://196.192.78.28:8082/noberto/spiderweb.git">
    <!-- Please provide path to your logo here -->
    <img src="logo/Untitled_design-removebg-preview.png" alt="spiderWeblogo" width="120" height="120">
  </a>
<strong>Web Crawler</strong>
</h1>

<div align="center">
  <br />
  <a href="#about"><strong>Explore the screenshots »</strong></a>
  <br />
</div>

<div align="center">

[![Project license](https://img.shields.io/github/license/dec0dOS/spiderweb.svg?style=flat-square)](LICENSE)
[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/dec0dOS/spiderweb/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project assistance](#project-assistance)
- [License](#license)

</details>



## About

<table><tr><td>
An information gathering platform that collects open source information from different sources on Internet and provide analyzed and meaningful query results.

<details>
<summary>Screenshots</summary>
<br>

|                               Home Page                               |                               Login Page                               |
| :-------------------------------------------------------------------: | :--------------------------------------------------------------------: |
| <img src="docs/images/screenshot.png" title="Home Page" width="100%"> | <img src="docs/images/screenshot.png" title="Login Page" width="100%"> |

</details>

</td></tr></table>

### Built With

> <li>Python</li>
> <li>MongoDB</li>
> <li>Scrapy</li>
> <li>Scrapyd</li>
> <li>ScrapyWeb</li>
> <li>Elasticsearch</li>


## Getting Started

### Prerequisites & dependencies
``` 
pip : -r requirements.txt
```

### Installation

```
git clone https://github.com/widambeDeograss/Web-Crawler-v2.git

```

<div style="margin:auto">OR</div> 

```
git clone https://github.com/widambeDeograss/Web-Crawler-v2.git

```

## Usage

To start the crawling process, run the command:
```
scrapy crawl web -o <filename>.csv/json/jl/xml
```

<br>To scrap using scrapyd and scrapyWeb: OPEN TWO TERMINAL INSTANCES run<br>
```
1: scrapyd

2:scrapyweb
```

Or run single crawlers following command:
```
scrapy crawl body -o \<filename>.csv/json/jl/xml<br>
```

## License

This project is licensed under the 

See [LICENSE](LICENSE) for more information.

