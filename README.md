# mutt-language-server

[![readthedocs](https://shields.io/readthedocs/mutt-language-server)](https://mutt-language-server.readthedocs.io)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/neomutt/mutt-language-server/main.svg)](https://results.pre-commit.ci/latest/github/neomutt/mutt-language-server/main)
[![github/workflow](https://github.com/neomutt/mutt-language-server/actions/workflows/main.yml/badge.svg)](https://github.com/neomutt/mutt-language-server/actions)
[![codecov](https://codecov.io/gh/neomutt/mutt-language-server/branch/main/graph/badge.svg)](https://codecov.io/gh/neomutt/mutt-language-server)
[![DeepSource](https://deepsource.io/gh/neomutt/mutt-language-server.svg/?show_trend=true)](https://deepsource.io/gh/neomutt/mutt-language-server)

[![github/downloads](https://shields.io/github/downloads/neomutt/mutt-language-server/total)](https://github.com/neomutt/mutt-language-server/releases)
[![github/downloads/latest](https://shields.io/github/downloads/neomutt/mutt-language-server/latest/total)](https://github.com/neomutt/mutt-language-server/releases/latest)
[![github/issues](https://shields.io/github/issues/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/issues)
[![github/issues-closed](https://shields.io/github/issues-closed/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/issues?q=is%3Aissue+is%3Aclosed)
[![github/issues-pr](https://shields.io/github/issues-pr/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/pulls)
[![github/issues-pr-closed](https://shields.io/github/issues-pr-closed/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/pulls?q=is%3Apr+is%3Aclosed)
[![github/discussions](https://shields.io/github/discussions/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/discussions)
[![github/milestones](https://shields.io/github/milestones/all/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/milestones)
[![github/forks](https://shields.io/github/forks/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/network/members)
[![github/stars](https://shields.io/github/stars/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/stargazers)
[![github/watchers](https://shields.io/github/watchers/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/watchers)
[![github/contributors](https://shields.io/github/contributors/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/graphs/contributors)
[![github/commit-activity](https://shields.io/github/commit-activity/w/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/graphs/commit-activity)
[![github/last-commit](https://shields.io/github/last-commit/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/commits)
[![github/release-date](https://shields.io/github/release-date/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/releases/latest)

[![github/license](https://shields.io/github/license/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server/blob/main/LICENSE)
[![github/languages](https://shields.io/github/languages/count/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)
[![github/languages/top](https://shields.io/github/languages/top/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)
[![github/directory-file-count](https://shields.io/github/directory-file-count/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)
[![github/code-size](https://shields.io/github/languages/code-size/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)
[![github/repo-size](https://shields.io/github/repo-size/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)
[![github/v](https://shields.io/github/v/release/neomutt/mutt-language-server)](https://github.com/neomutt/mutt-language-server)

[![pypi/status](https://shields.io/pypi/status/mutt-language-server)](https://pypi.org/project/mutt-language-server/#description)
[![pypi/v](https://shields.io/pypi/v/mutt-language-server)](https://pypi.org/project/mutt-language-server/#history)
[![pypi/downloads](https://shields.io/pypi/dd/mutt-language-server)](https://pypi.org/project/mutt-language-server/#files)
[![pypi/format](https://shields.io/pypi/format/mutt-language-server)](https://pypi.org/project/mutt-language-server/#files)
[![pypi/implementation](https://shields.io/pypi/implementation/mutt-language-server)](https://pypi.org/project/mutt-language-server/#files)
[![pypi/pyversions](https://shields.io/pypi/pyversions/mutt-language-server)](https://pypi.org/project/mutt-language-server/#files)

A language server for (neo)mutt's muttrc.

- [x] [Diagnostic](https://microsoft.github.io/language-server-protocol/specifications/specification-current#diagnostic)
- [x] [Document Link](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_documentLink)
- [x] [Hover](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_hover)
- [x] [Completion](https://microsoft.github.io/language-server-protocol/specifications/specification-current#textDocument_completion)

A screencast authored by @rbmarliere:

[![asciicast](https://camo.githubusercontent.com/aa2be3ad710e855b3e6b7cd55f5261ac7582f1e69c8947f4619ba4c96f8cc506/68747470733a2f2f61736369696e656d612e6f72672f612f3631303634352e737667)](https://asciinema.org/a/610645)

![diagnostic](https://github.com/neomutt/mutt-language-server/assets/32936898/61c81c34-c5ae-4d66-82b2-2be5affb1162)

![document link](https://github.com/neomutt/mutt-language-server/assets/32936898/7db39120-401e-4be7-82c4-827609ab7f26)

See
[![readthedocs](https://shields.io/readthedocs/mutt-language-server)](https://mutt-language-server.readthedocs.io)
to know more.

## How Does It Work

See [here](https://github.com/neomutt/lsp-tree-sitter#usage).

## Related Projects

- [neomutt.vim](https://github.com/neomutt/neomutt.vim): vim filetype plugin
  for neomuttrc
