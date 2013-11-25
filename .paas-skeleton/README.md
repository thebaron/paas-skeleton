paas-skeleton quickstart
========================

GitHub home: https://github.com/easel/paas-skeleton

To create a new project using this skeleton:
- create a new repo
- git pull https://github.com/easel/paas-skeleton.git master

To update your project with the latest updates from this skeleton:
- make update-skeleton

To build a project using this skeleton:
- source env.sh
- make

To run a project using this skeleton:
- honcho -f Procfile start

Architecture
============
This PAAS skeleton is designed to ensure a reproducible development and deployment environment
that is suitable for use across a wide variety of PAAS platforms. It provides two very high-level
interface points that are designed to be extended by more specialized skeleton projects or by projects
themself.
