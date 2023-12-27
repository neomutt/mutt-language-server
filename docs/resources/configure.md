# Configure

- For windows, change `~/.config` to `~/AppData/Local`
- For macOS, change `~/.config` to `~/Library`

## (Neo)[Vim](https://www.vim.org)

For vim:

- Change `~/.config/nvim` to `~/.vim`
- Change `init.vim` to `vimrc`

### [coc.nvim](https://github.com/neoclide/coc.nvim)

`~/.config/nvim/coc-settings.json`:

```json
{
  "languageserver": {
    "mutt": {
      "command": "mutt-language-server",
      "filetypes": [
        "muttrc",
        "neomuttrc"
      ]
    }
  }
}
```

### [vim-lsp](https://github.com/prabirshrestha/vim-lsp)

`~/.config/nvim/init.vim`:

```vim
if executable('mutt-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'mutt',
          \ 'cmd': {server_info->['mutt-language-server']},
          \ 'whitelist': ['muttrc', 'neomuttrc'],
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

`~/.config/nvim/init.lua`:

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "muttrc*", "neomuttrc" },
  callback = function()
    vim.lsp.start({
      name = "mutt",
      cmd = { "mutt-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

`~/.emacs.d/init.el`:

```lisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "mutt-language-server")))
  :activation-fn (lsp-activate-on "muttrc" "neomuttrc")
  :server-id "mutt")))
```

## [Helix](https://helix-editor.com/)

`~/.config/helix/languages.toml`:

```toml
[[language]]
name = "muttrc"
language-servers = [ "mutt-language-server",]

[[language]]
name = "neomuttrc"
language-servers = [ "mutt-language-server",]

[language_server.mutt-language-server]
command = "mutt-language-server"
```

## [KaKoune](https://kakoune.org/)

### [kak-lsp](https://github.com/kak-lsp/kak-lsp)

`~/.config/kak-lsp/kak-lsp.toml`:

```toml
[language_server.mutt-language-server]
filetypes = [ "muttrc", "neomuttrc",]
command = "mutt-language-server"
```

## [Sublime](https://www.sublimetext.com)

`~/.config/sublime-text-3/Packages/Preferences.sublime-settings`:

```json
{
  "clients": {
    "mutt": {
      "command": [
        "mutt-language-server"
      ],
      "enabled": true,
      "selector": "source.muttrc"
    }
  }
}
```

## [Visual Studio Code](https://code.visualstudio.com/)

[An official support of generic LSP client is pending](https://github.com/microsoft/vscode/issues/137885).

### [vscode-glspc](https://gitlab.com/ruilvo/vscode-glspc)

`~/.config/Code/User/settings.json`:

```json
{
  "glspc.serverPath": "mutt-language-server",
  "glspc.languageId": "muttrc"
}
```
