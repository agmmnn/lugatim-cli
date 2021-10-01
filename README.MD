![screenshot](https://user-images.githubusercontent.com/16024979/135603517-62ec874a-b117-485c-9e8f-86da5062288a.png)

<div align="center">
<a href="https://github.com/agmmnn/lugatim-cli">
<img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/agmmnn/lugatim-cli"></a>
<a href="https://pypi.org/project/lugatim-cli/">
<img alt="PyPI" src="https://img.shields.io/pypi/v/lugatim-cli"></a>

Command-line tool for Kubbealti Lugati: [lugatim.com](http://lugatim.com/), with rich output.

</div>

```
pip install lugatim-cli
```

# Usage

```
lugatim <word>
```

```
lugatim <word> -a
#shows all results
```

```
lugatim <word> -p
# returns plain text output
```

## Arguments

```
  -h, --help     show this help message and exit
  -p, --plain    returns plain text output
  -a, --all      show all results
  -v, --version  show program's version number and exit
```

# Requirements

- Python >3.5

## Dependencies

- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [rich](https://pypi.org/project/rich/)
- [lxml](https://pypi.org/project/lxml/)

# License

CC0
