# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 10:37:51 2016

@author: Yan JIN - ING3 - DS
"""
import networkx as nx
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans

file_name='./dolphins.gml'
#TP de Python
class Graph_Objext:
    def __init__(self):
        G = nx.Graph()
        
    def get_graph(self,file_name):
        G = nx.read_gml(file_name)
        return G
        
    def Visulazation(self,G):
        nx.draw_networkx(G)
           
    def laplacian_matrix(self,G):
        return nx.laplacian_matrix(G)
    
    def methode_spectrale(self,M):
        w,v = LA.eigh(M)
        return v    
        
    def bissection(self,v,g):
        n1=[]
        n2=[]
        n=np.array(v[:,1])
        for i in range(len(n)):
            if n[i]>0:
                n1.append(i)                
            else:
                n2.append(i)
        pos=nx.spring_layout(g)
        nx.draw_networkx(g,pos,nodelist=n1,node_color='red')
        nx.draw_networkx(g,pos,nodelist=n2,node_color='blue')   
        plt.title('Bissection')
    
    def kmeans(self,v,g):
        a = [v[:,1], v[:,2], v[:,3]]
        b = np.transpose(a)
        kmeans = KMeans(n_clusters=2, random_state=0).fit(b)
        print kmeans.labels_
        return kmeans.labels_
        
def main():
    #Question 1
    fig=plt.figure(1)
    plt.subplot(321)
    graph = Graph_Objext()
    g = graph.get_graph(file_name) 
    graph.Visulazation(g)
    plt.title('Graph')
    
    #Question 2
    L = graph.laplacian_matrix(g)
    L = L.toarray()
    v = graph.methode_spectrale(L)
    
    #Question 3
    plt.subplot(322)
    plt.plot(v[:,1], v[:,2], 'o')
    plt.xlabel('v1')
    plt.ylabel('v2')
    plt.title('v1,v2')
    
    #Question 4   
    ax = fig.add_subplot(323, projection='3d')
    ax.scatter(v[:,1], v[:,2], v[:,3])
    plt.title('v1,v2,v3')
    ax.set_xlabel('v1')
    ax.set_ylabel('v2')
    ax.set_zlabel('v3')
    
    #Question 5
    plt.subplot(324)
    graph.bissection(v,g)    

    #Question 6   
    kmeanslabels=graph.kmeans(v,g)
    ax = fig.add_subplot(325, projection='3d')
    for i in range(len(v[:,1])):
        if(kmeanslabels[i]==0):
            ax.scatter(v[i,1], v[i,2], v[i,3],color='red')
        else:
            ax.scatter(v[i,1], v[i,2], v[i,3],color='blue')   
    ax.set_xlabel('v1')
    ax.set_ylabel('v2')
    ax.set_zlabel('v3')  
    plt.title('Kmeans')
        
    plt.subplot(326)
    n1=[]
    n2=[]
    n=np.array(v[:,1])
    for i in range(len(n)):
        if kmeanslabels[i]==0:
            n1.append(i)                
        else:
            n2.append(i)
    pos=nx.spring_layout(g)
    nx.draw_networkx(g,pos,nodelist=n1,node_color='red')
    nx.draw_networkx(g,pos,nodelist=n2,node_color='blue')   
    plt.title('Kmeans')
    plt.show()  

if __name__ == "__main__":
    main()
