#from svm import *
import sys
import os
import zlib
import NCD
import kmeans
from homeworkmap import buildMap
import pickle
NCD.COMPRESSIONLEVEL = 6

class BasicClusters:

  def __init__(self, homeworkpath):
    self.studenthomeworkmap = buildMap(homeworkpath)
    self.clusters = self._cluster()

  def __str__(self):
    this = ""
    for cluster in self.clusters:
      this += str(cluster) + ": " + str(self.clusters[cluster]) + "\n-----------------------------------\n"
    return this


class SimpleClusters(BasicClusters):

  def __init__(self, homeworkpath, clustergap = 0.25):
    self.clustergap = clustergap
    BasicClusters.__init__(self,homeworkpath)

  def _cluster(self):
    students = self.studenthomeworkmap.keys()
    #This is where we store the comparisons
    clusters = {}

    for student in students:
      foundclusters = []

      studentxhomeworkfile = open(self.studenthomeworkmap[student], 'r')
      studentxhomework = studentxhomeworkfile.read()
      studentxhomeworkfile.close()
      for cluster in clusters:
        i = 0
        incluster = False
        while i < len(clusters[cluster]) and not incluster:
          print student, clusters[cluster][i]
          studentyhomeworkfile = open(self.studenthomeworkmap[clusters[cluster][i]], 'r')
          studentyhomework = studentyhomeworkfile.read()
          studentyhomeworkfile.close()        
          
          xydistance = NCD.NCDkernel(studentxhomework, studentyhomework)      

          if xydistance < self.clustergap:
            incluster = True
            foundclusters.append(cluster)

          i+=1


      if not foundclusters:
        clusters[student] = [student]
      else:
        newcluster = []
        for cluster in foundclusters:
          newcluster.extend(clusters[cluster])
          del clusters[cluster]
        newcluster.append(student)
        clusters[student] = newcluster
        
    return clusters 


class KMeansClusters(SimpleClusters):
  
  def __init__(self,homeworkpath,k = 6):
    self.k = k
    BasicClusters.__init__(self,homeworkpath)

  def _cluster(self):
    data = self.studenthomeworkmap.keys()
    return kmeans.kmeans(data, self._metric, kmeans.quickguess(data,self.k), self.k)

  def _metric(self,x,y):
    x = open(self.studenthomeworkmap[x],'r')
    xdata = x.read()
    x.close()
    y = open(self.studenthomeworkmap[y],'r')
    ydata = y.read()
    y.close()
    return NCD.NCDkernel(xdata,ydata)
    

if __name__ == "__main__":
  clustered = KMeansClusters(sys.argv[1],int(sys.argv[2]))
  print clustered
  pickle.dump(clustered,open("lastcluster.p","wb"))
  
      
    
