# Configure

See customization in
<https://mutt-language-server.readthedocs.io/en/latest/api/mutt-language-server.html#mutt_language_server.server.get_document>.

## (Neo)[Vim](https://www.vim.org)

### [coc.nvim](https://github.com/neoclide/coc.nvim)

```json
{
  "languageserver": {
    "mutt": {
      "command": "mutt-language-server",
      "filetypes": [
        "muttrc",
        "neomuttrc"
      ],
      "initializationOptions": {
        "method": "builtin"
      }
    }
  }
}
```

### [vim-lsp](https://github.com/prabirmuttrestha/vim-lsp)

```vim
if executable('mutt-language-server')
  augroup lsp
    autocmd!
    autocmd User lsp_setup call lsp#register_server({
          \ 'name': 'mutt',
          \ 'cmd': {server_info->['mutt-language-server']},
          \ 'whitelist': ['muttrc', 'neomuttrc'],
          \ 'initialization_options': {
          \   'method': 'builtin',
          \ },
          \ })
  augroup END
endif
```

## [Neovim](https://neovim.io)

```lua
vim.api.nvim_create_autocmd({ "BufEnter" }, {
  pattern = { "muttrc*" "neomuttrc*" },
  callback = function()
    vim.lsp.start({
      name = "mutt",
      cmd = { "mutt-language-server" }
    })
  end,
})
```

## [Emacs](https://www.gnu.org/software/emacs)

```elisp
(make-lsp-client :new-connection
(lsp-stdio-connection
  `(,(executable-find "mutt-language-server")))
  :activation-fn (lsp-activate-on "muttrc*" "neomuttrc*")
  :server-id "mutt")))
```

## [Sublime](https://www.sublimetext.com)

```json
{
  "clients": {
    "mutt": {
      "command": [
        "mutt-language-server"
      ],
      "enabled": true,
      "selector": "source.mutt"
    }
  }
}
```
