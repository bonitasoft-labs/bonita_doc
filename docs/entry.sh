#!/bin/sh

git submodule init
git submodule update
bundle
npm i
npx webpack-cli
# jekyll serve -H 0.0.0.0 -P 4000
jekyll serve --force_polling -H 0.0.0.0 -P 4000
