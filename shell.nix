{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    buildInputs = [
      pkgs.python3
      pkgs.python3Packages.pip
      pkgs.python3Packages.pygame
      pkgs.python3Packages.virtualenv
    ];

    shellHook = ''
      [ -d .venv ] || python3 -m venv .venv
    '';
  }
