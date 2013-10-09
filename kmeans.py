
#metric should be able to compare two data points
#len(data) should be at least as large as k
#len(guessmeans) should be EXACTLY k
#this version of kmeans uses ONE OF THE ACTUAL DATA points for each mean.  The mean is the data point that minimizes the sum of the distances to each of the points in its cluster
def kmeans(data, metric, guessmeans, k = 6):

  #initialize the means
  clusters = {}
  for i in range(k):
    clusters[guessmeans[i]] = []

  for point in data:
    print point
    closestmean = None
    #In python, strings are bigger than ints or floats always
    closestdist = "biggest"
    for mean in clusters:
      distance = metric(mean, point)
      if distance < closestdist:
        closestdist = distance
        closestmean = mean
    clusters[closestmean].append(point)

  newmeans = calcmeans(clusters,metric)
  if equalmeans(newmeans,guessmeans):
    return clusters

  return kmeans(data,metric,newmeans,k)


def calcmeans(clusters,metric):
  newmeans = []
  for cluster in clusters:
    sumdistances = {}
    #init sumdistances to emptiness
    for point in clusters[cluster]:
      sumdistances[point] = 0

    i = 0
    for i in range(len(clusters[cluster])):
      j = i + 1
      for j in range(len(clusters[cluster])):
        print i,j
        distance = metric(clusters[cluster][i],clusters[cluster][j])
        sumdistances[clusters[cluster][i]] += distance
        sumdistances[clusters[cluster][j]] += distance  

    newmeans.append(min(sumdistances.items(),key = lambda x: x[1])[0])

  return newmeans
  

def equalmeans(newmeans, oldmeans):
  if len(newmeans) != len(oldmeans):
    return False

  equalflag = True
  for i in range(len(newmeans)):
    if newmeans[i] not in oldmeans:
      equalflag = False
  return equalflag

def quickguess(data, k = 6):
  means = []
  for i in range(k):
    means.append(data[i])
  return means
  
