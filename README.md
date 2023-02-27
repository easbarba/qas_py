# Qas

Easily manage multiple FLOSS repositories

Installation

You can install the package via pip:

TODO

## Usage

`Qas` consumes configuration in the following manners:

By default it looks for configuration files at `$XDG_CONFIG/qas`.

```shell
qas --grab
```

Of course, a `JSON` configuration file can provide projects;

```shell
qas --grab --json ~/Downloads/misc.json
```

or it consumes even a REST API `JSON` resource providing all the projects.

```shell
qas --grab --api localhost:5000/configs
```

PS: an API example is at: https://github.com/easbarba/qas_api.

## Configuration file

A `qas` single configuration file:

```json
[
  {
    "name": "awesomewm",
    "branch": "master",
    "url": "https://github.com/awesomeWM/awesome"
  },
  {
    "name": "nuxt",
    "branch": "main",
    "url": "https://github.com/nuxt/framework"
  }
]
```

More examples of configuration files are at `examples`.

## Options

Consult `qas --help` for more options.

## GNU Guix

To load all system dependencies, just run `guix shell`

## TODO

### High

- config: branch defaults to master

### Low

- config: move on these to a syntax check class
- cli: add rest api option: `--api`
- cli: add single configuration file option: `--json`

## LICENSE

[GPL-v3](https://www.gnu.org/licenses/gpl-3.0.en.html)
