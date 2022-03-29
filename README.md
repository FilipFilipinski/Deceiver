# Deceiver👮🔦

Python application written in Flask that generates fake personal information. Data used in the project was taken from [dane.gov.pl](https://dane.gov.pl/pl/dataset/219,imiona-nadawane-dzieciom-w-polsce/resource/36393/table?page=1&per_page=20&q=&sort=)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install requirements.txt
```

## Usage

```bash
python3 app.py
```
## API Reference

#### Get fake name

```http
  GET /api/
```

| Parameter | Type     | Result                |
| :-------- | :------- | :------------------------- |
| `none` | `none` | `fake data` |

#### Lots of fake data

```http
  GET /api/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `quantity`      | `number` | `returns fake data in the amount specified above`|
## License
[MIT](https://choosealicense.com/licenses/mit/)
