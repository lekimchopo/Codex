# AI & Automation Lab

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active_lab-0e7490?style=flat-square)
![Dependencies](https://img.shields.io/badge/runtime_dependencies-none-16a34a?style=flat-square)

A public laboratory for small, reviewable experiments around **Python, security utilities, AI-assisted development and automation**.

The goal is not to collect disconnected demos. Each experiment should be understandable, safe to run, documented and small enough to review.

## Current utility

### Cryptographically secure password generator

`password_generator.py` generates passwords using Python's `secrets` module, which is designed for security-sensitive randomness.

```bash
python3 password_generator.py --length 20
```

Short option:

```bash
python3 password_generator.py -l 24
```

The command validates the requested length and uses letters, digits and punctuation from Python's standard library.

## Run the tests

No third-party packages are required.

```bash
python3 -m unittest discover -s tests -v
```

## Repository structure

```text
.
├── password_generator.py
├── tests/
│   └── test_password_generator.py
├── .gitignore
└── README.md
```

## Engineering principles

- Prefer the Python standard library when it is sufficient.
- Use secure randomness for security-sensitive values.
- Validate untrusted command-line input.
- Add tests before expanding behavior.
- Never commit API keys, tokens, generated passwords or personal data.
- Document the threat boundary and limitations of every security-related utility.

## Roadmap

- [x] Secure password generation with `secrets`.
- [x] Input validation and automated unit tests.
- [ ] Password-strength and entropy explanation utility.
- [ ] Safe file-hash verification tool.
- [ ] Structured-output examples for AI integrations.
- [ ] Local-agent experiments with sanitized configuration examples.
- [ ] Continuous integration for automated tests.

## Security note

Generated passwords are written to standard output. Avoid running the command in environments where terminal history, screen recording or process output may be captured. This utility is educational and does not replace a reputable password manager.

## Profile

More product case studies and technical context are available on [my GitHub profile](https://github.com/lekimchopo).
