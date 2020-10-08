#!/usr/bin/env python

import sys, subprocess, generator

# Path to docs repository
# Just add an item to this dictionnary to add a new repository

repos = {
    "bonita":"repos/bonita-doc",
    "bcd":"repos/bonita-continuous-delivery-doc",
    "ici":"repos/bonita-ici-doc"
}
destPath = ""

# Elastic search Socket. It will be use to index the documentation
elasticSearchUrl = "localhost:9200"

# Check the number of arguments. The commande line for this script must be `Python generate_doc.py <product> <version>`
if len(sys.argv) < 3 :
    print("Not enough argument, we expected : python generate_doc.py <product> <version>")
    exit()


if sys.argv[1] in repos:
    print(repos[sys.argv[1]])
    repo = sys.argv[1]
    print("try repo %s" %(repo))
    path = repos[repo]
    print("try path %s" %(path))
    print("try to checkout the version ...")


    version = sys.argv[2]
    print("try version %s" %(version))
    print("cd %s && git checkout -f %s  && git pull " % (path, version ))
    #Prepration of the commande to get the right version of the product
    cmd ="cd %s && git fetch --prune && git checkout --force %s  && git pull --rebase" % (path, version )

    # comments this, i don't know why (perhaps, python update break or change this behavior)
    #try:
    #    # System call with the command line prepare above
    #    subprocess.check_output([cmd],shell=True,  stderr=subprocess.STDOUT)
    #except subprocess.CalledProcessError as e:
    #   print(e)
    #   sys.exit(1)

    print("repo checkout with success")

    print("clean destination... ")

    try:
        # The destination folder must be clean in case of a change of the doc structure
        cmd ="cd %s  && rm -rf %s " % (destPath, version )

    except subprocess.CalledProcessError as e:
        print(e)

    print("try to generate documention %s %s ..." % (path, version))

    # Generate the documentation from the r
    generator.generate_doc(repo, path,version, destPath)

    print("... GENERATION SUCCESSFUL ...")

    # Uncomment when elastic is configured
    # print("try to indexing documentation ...")

    #generator.indexingDocuments(elasticSearchUrl, repo, version)

    # print("... INDEXATION SUCCESSFUL ...")

else:
    print("Unkown repo")
