import math
import os
import ast
import numpy
import pandas as pd

# the dot product function is the first to start
# file_names = []         #  A list of the different names of the different documents in the document pool
sim_cluster = []        #  A list containing the names of  similar documents
dissim_cluster = []     #  A list containing the names of disimilar documents


def Form_vectors():
    #  List containing dictionaries
    dict_list = []
    os.chdir(
        "/Users/mrfomfoh/Documents/Lobga/Learn/School/Third Year Second Semester/CSC498/My Project/Program/untitled folder")
    p = open('Output2', 'r')

    #  Read strings drom output2
    r = p.read()

    #  Form a list containing the words in the lists
    index_terms = r.strip(' \'][\' ').strip(' \' ').split('\', \'')

    #  Access the data stored in Output1
    o2 = open('Output1', 'r')
    dw = o2.read()
    d = dw.split('\n')
    d.pop(-1)  # remove the empty character caused by the next line character

    i = 0
    # iterate over the list of dictionaries and remove the document file name and keep the dictionary
    # rem holds the names of the documents
    for stringss in d:  # loop through the list of dictionaries
        listss = stringss.split('f', 1)  # split the string into the name of the dictionary and the dictionaery itself
        dict_list.append(ast.literal_eval(listss[1]))  # convert the string dictionary to an actual dictionary
        i = i + 1
    print(i)
    print(dict_list)

    #  Check whether word in a particular document exists in the set of words
    j = 0
    doc_collection = []
    for l in dict_list:
        doc = []
        keys = l.keys()
        for i in index_terms:
            if i in keys:
                doc.append(1)
            else:
                doc.append(0)
        print(doc)
        doc_collection.append(doc)
        j = j+1
        print(j)
    print(doc_collection)
    print(j)
    return doc_collection

#  Function to calculate the length of each vector in the collection
def Calculate_vector_length():
    vector_collection = Form_vectors()  # d holds the various vectors in the vector collection
    length_squared = []
    vector_lengths = []
    print("Vector collection is: ", vector_collection)
    for vect in vector_collection:
        sums = 0
        vector_lengths.append(len(vect))
        for i in vect:
            sums = sums + (i*i)
        length_squared.append(sums)
    print(length_squared)
    print("The lengths of the vectors are: ", vector_lengths)
    return length_squared

# Function to calculate the dot product
def Calculate_vector_dotproduct():
    vector_collection = Form_vectors()  # vector_collection has the different vectors in the vector collection
    dotProducts = []  # hold all possible dot products
    squared_lengths = Calculate_vector_length()  # contains a list that has the square of the length of each document
    i = 0
    j = 0
    similarity_matrix = []

    #  Read file names from external file called file name in to a list
    r_file_names = open('file_names', 'r')
    f = r_file_names.read()
    file_names = f.strip(' \'][\' ').strip(' \' ').split('\', \'')

    for i in range(len(vector_collection)):
        # do the dot product of vect with all the values in the vector collection
        dotprod = []
        sim_matrix = []
        for j in range(len(vector_collection)):
            numerator = dot_prod(vector_collection[i], vector_collection[j])
            dotprod.append(numerator)
            denominator = math.sqrt(squared_lengths[i] * squared_lengths[j])
            # print("The cosines are:\n", math.acos((numerator/denominator)))
            sim_matrix.append((numerator/denominator))
        dotProducts.append(dotprod)
        similarity_matrix.append(sim_matrix)
    print("The dot products are: ", dotProducts)
    print("The similarity matrix is: \n", similarity_matrix)
    i = 0
    j = 0

    # !!!!! Use a table here instead of the format option
    print("{:<20} {:<20} {:20} {:20}".format('Docs', file_names[0], file_names[1], file_names[2]))
    for i in range(len(file_names)+1):
        if i > (len(file_names)-1):
            break
        print("{:<20} {:<20} {:20} {:20}".format(file_names[i], similarity_matrix[i][0], similarity_matrix[i][1], similarity_matrix[i][2]))
    print("yellow")
    Create_Cluster(similarity_matrix, file_names)
    print("Similar cluster: \n", sim_cluster)
    print("Disimilar set of documents: \n", dissim_cluster)


def dot_prod(a, b):
    sums = 0
    i = 0
    j = 0
    for i in range(len(a)):
        sums = sums + (a[i]*b[i])
    return sums


# Create a cluster
def Create_Cluster(a, b):
    #  Clustering is based on documents with similarity score above 0.1
    i = 0
    j = 0
    for i in range(len(a)+1):
        if i > len(a)-1:
            break
        for j in range(len(a[i])+1):
            sim = []
            dissim = []
            if j > len(a[i])-1 or i > len(a) - 1:
                break
            if a[i][j] > 0.1 and b[i] != b[j]:
                sim.append(b[i])
                sim.append(b[j])
            if a[i][j] <= 0.1:
                dissim.append(b[i])
                dissim.append(b[j])

            # Append sim or dissim to similarity cluster or disisimilarity cluster
            sim_cluster.append(sim)
            dissim_cluster.append(dissim)


Calculate_vector_dotproduct()