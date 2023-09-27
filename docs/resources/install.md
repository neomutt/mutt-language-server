# Install

## [AUR](https://aur.archlinux.org/packages/mutt-language-server)

```sh
yay -S mutt-language-server
```

## [NUR](https://nur.nix-community.org/repos/Freed-Wu)

```nix
{ config, pkgs, ... }:
{
  nixpkgs.config.packageOverrides = pkgs: {
    nur = import
      (
        builtins.fetchTarball
          "https://github.com/nix-community/NUR/archive/master.tar.gz"
      )
      {
        inherit pkgs;
      };
  };
  environment.systemPackages = with pkgs;
      (
        python3.withPackages (
          p: with p; [
            nur.repos.Freed-Wu.mutt-language-server
          ]
        )
      )
}
```

## [Nix](https://nixos.org)

```sh
nix shell github:neomutt/mutt-language-server
```

Run without installation:

```sh
nix run github:neomutt/mutt-language-server -- --help
```

## [PYPI](https://pypi.org/project/mutt-language-server)

```sh
pip install mutt-language-server
```

See [requirements](requirements) to know `extra_requires`.
