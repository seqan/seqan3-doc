#  written by Jongkyu Kim (j.kim@fu-berlin.de)

import os
import sys

CAT_NAME = "Modules"
INDEX_TEMP = "_index.rst"

def generateIndex(inDir, outDir):
    listModules = []
    for fileName in os.listdir(inDir) :
        if os.path.isdir(inDir + fileName) == True:
            listModules.append(fileName)  
    listModules = sorted(listModules)

    # generate index.rst
    inFile = open(INDEX_TEMP, "r")
    outFile = open(outDir + "/index.rst", "w")
    for line in inFile :
        outFile.write(line)
    inFile.close()
    outFile.write("   :caption: %s:\n\n" % CAT_NAME)
    for moduleName in listModules :
        outFile.write("   %s\n" % (moduleName))
    outFile.close()

def generateRST(inPath, outPath, moduleName, listModules, listFiles) :
    if len(listModules) > 0 and os.path.isdir(outPath) == False:
        os.mkdir(outPath)

    # title
    outFile = open(outPath + ".rst","w")
    outFile.write(moduleName[0].upper() + moduleName[1:] + "\n")
    outFile.write("=" * len(moduleName) + "\n\n")

    # doxygenfile
    for fileName in listFiles :
        outFile.write(".. doxygenfile:: %s/%s\n" % (inPath,fileName))
        outFile.write("   :project: myproject\n\n")

    # toctree
    outFile.write(".. toctree::\n")
    outFile.write("   :caption: %s:\n" % CAT_NAME)
    outFile.write("   :titlesonly:\n")
    outFile.write("   :maxdepth: 1\n")
    outFile.write("   :hidden:\n\n")
    for childModuleName in listModules :
       outFile.write("   %s/%s\n" % (moduleName, childModuleName) )
    outFile.close()

def generateRSTs(inDir, outDir, isRoot=False):
    listModules = []
    listFiles = []
    for fileName in os.listdir(inDir) :
        if os.path.isdir(inDir + "/" + fileName) == True:
            listModules.append(fileName)  
        else :
            fileExt = fileName.split(".")[-1]
            if fileExt == "hpp" or fileExt == "cpp" :
                listFiles.append(fileName)
    
    listModules = sorted(listModules)
    listFiles = sorted(listFiles)

    print isRoot, inDir, outDir, listModules, listFiles

    if isRoot == False :
        moduleName = outDir.split("/")[-1]
        generateRST(inDir, outDir, moduleName, listModules, listFiles)


    for moduleName in listModules :
        curInDir = inDir + "/" + moduleName
        curOutDir = outDir + "/" + moduleName
        generateRSTs(curInDir, curOutDir, False)

'''
Alphabet
========

.. doxygenfile:: alphabet.hpp
   :project: myproject

.. doxygenfile:: alphabet_container.hpp
   :project: myproject

.. doxygenfile:: compound_alphabet.hpp
   :project: myproject

.. toctree::
   :caption: Modules:
   :titlesonly:
   :maxdepth: 1
   :hidden:

   alphabet/aminoacid
   alphabet/gaps
   alphabet/nucleotide
'''


#    print listModules
#    print listFiles


###################
inDir = sys.argv[1]
outDir = sys.argv[2]

generateIndex(inDir, outDir)
generateRSTs(inDir, outDir, True)