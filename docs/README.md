# Bonita Documentation Generator

The Bonita Documentation Generator is composed of two parts :

* The retrievement of documentation
* The generation of the static website folder

## Use gradle tasks (To fix and to validate):
Some gradle tasks are available to help you to build your environment.

You can find:
- **buildImage -PimageVersion=myTag** to build an image
- **createContainer -PimageVersion=myTag** to build an container for image with tag **myTag**
- **startContainer- PimageVersion=myTag** to run an container
-  **execContainerBuild -PimageVersion=myTag** to generate static site by jekyll
-  **execContainerDev -PimageVersion=myTag** to run static site and deploy it


## Add a new version of documentation

You need to update generate_documentation.sh and _config.yml files.

## Add a new add-on of documentation

You need to update generate_doc.py, generate_documentation.sh and _config.yml files.

## Run generator manually
```

If you use [Docker](https://www.docker.com/), go inside `proto_doc` folder and run :

```bash
 docker build -t bdg .
 docker run --rm --name bdg -it -p 4000:4000 -v $(pwd):/doc bdg
```

Note: *On Windows, use ${pwd} instead of $(pwd)*
Then you can access to the website on http://127.0.0.1:4000

For windows user, powershell is your friend...

If you don't use docker, you configure your environment as bellow.

## Git environment

You need to retrieve git submodule content.

```bash
 git submodule init
 git submodule update
```
The documentation site is generated from 3 documentations repositories :

* [Bonita documentation](https://github.com/bonitasoft/bonita-doc)
* [BICI documentation](https://github.com/bonitasoft/bonita-ici-doc)
* [BCD documentation](https://github.com/bonitasoft/bonita-continuous-delivery-doc)

Today, submodules are linked to my forks of those repos in order to be use with a coherence between version and branch.

## Python environment

### Python 2.7

You can pass this step if you already have Python 2.7 install on your system.
```bash
# refreshing the repositories
sudo apt update
# its wise to keep the system up to date!
# you can skip the following line if you not
# want to update all your software
sudo apt upgrade
# installing python 2.7 and pip for it
sudo apt install python2.7 python-pip

```

[Use python 2 with an existing python 3 on ubuntu](https://askubuntu.com/questions/981118/correct-way-to-install-python-2-7-on-ubuntu-17-10/981279)

### Modules

#### [Slugify](https://pypi.org/project/python-slugify/)

```bash
pip install python-slugify

```

#### [Elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/)

```bash
pip install elasticsearch

```

## Jekyll environment

*[Install ruby if you haven't install it yet](https://www.ruby-lang.org/en/documentation/installation/)*

```bash
bundle
```
It will install all plugins mentions in the [Gemfile](https://github.com/pbelabbes/proto_doc/blob/master/Gemfile)

## React environment

NodeJS is required - [install NodeJS](https://nodejs.org/en/)

To install all the packages needed, run in `proto_doc/`:

```bash
#install package
npm install

#install webpack
npm install -g webpack

#build js
npx webpack-cli
```
# ElasticSearch

The Bonita Doc Generator didn't include the ElasticSearch server but is designed to work with it.

To use ElasticSearch, in `generate_doc.py` you need to add your elasticsearch to `elasticSearchUrl` line 12 and uncomment the lines bellow :

```bash
  # print "try to indexing documentation ..."

  # generator.indexingDocuments(elasticSearchUrl, repo, version)

  # print "... INDEXATION SUCCESSFUL ..."

```
You also need to add your elasticsearch url in `webpack/components/Search.js` to `ELASTICSEARCH_SOCKET` constant :

```bash
const ELASTICSEARCH_SOCKET = "192.168.0.101:9200"
```
You can use a docker container for tests.
Here we add an elasticsearch configuration file to [enable CORS](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-http.html)
```
docker run -d --rm --name elasticsearch -v $PWD/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -p 9200:9200 -p 9300:9300 elasticsearch
```
In that case you can use the following ip `172.17.0.1` for elasticsearch.

# Basic usage

if you use Docker, all the commands will be used in the container bash.

```bash

docker exec -it bdg /bin/sh
```

## Retrieve documentation

Use `python generate_doc.py` to :

* generate a markdown documentation compatible with Jekyll
* Index the content of the documentation in an elasticsearch server

This command requires 2 arguments:
- `product` - Documentation product string. Example: `bonita`.
- `version` - Documentation version string. Example: `1.0`.

Providing arguments to the doc generator command is done with one of the following syntaxes:
```bash
python generate_doc.py <product> <version>
```



Examples:
```bash
python generate_doc.py bcd 1.0
python generate_doc.py bonita 7.7
python generate_doc.py ici 1.0
```




**Note :** If you bind submodule to bonitasoft documentation repos, some visual bug can be found on the frontend. If it's the case, prefix your version by `jekyll-`

Example :
```bash
python generate_doc.py bcd jekyll-2.0
```

## Generate static site

If you use Docker, the jekyll server will be launched each time you run the image.

Once you have update all documentations you want, you need to build the static.
To do so, run jekyll.

```bash
#build project
jekyll build

#build project with a specific destination
jekyll build --destination <destination_folder>

#build project and serve
jekyll serve

#build project and serve with a livereload
jekyll serve --autoreload
```

# Make modifications to the project

## Webpack

If you make some modification to `webpack/entry.js`, `webpack/components/Search.js` or  `webpack.config.js`, you will need to rebuilt the js. To do so, run :

```bash
 npx webpack-cli
```

## Jekyll configuration

If you modify Jekyll's configuration in `_config.yml` you will need to restart the Jekyll's server.

If you use Docker, close the container with the Jekyll's server and run it back. You can also run :

```bash
jekyll build
```


More information in the [Jekyll documentation](https://jekyllrb.com/docs)


