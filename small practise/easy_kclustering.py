import sys
import random
import numpy as np

#N is the size, M the dimension
def data_generator(N, M, *distribution):
	#parameter the method? Gaussian
	if not distribution:
		return np.random.random((N, M))



#or this instead of using a different function, should use Lyrod method but with different parameter
#for transformation in the Eurcidean distance
#http://stats.stackexchange.com/questions/81481/why-does-k-means-clustering-algorithm-use-only-euclidean-distance-metric
def manhattan_distance():
	pass

def cluster_points(dataset, center, distance=np.linalg.norm):
	#fit the data into each cluster
	clusters = {}
	for x in dataset:
		#according to:
		#bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) for i in enumerate(mu)], key=lambda t:t[1])[0], can just use i[1] instaed of mu[i[0]]...
		#tip1. need to get the index of the center, need enumerate
		#tip2. make generator type tuple(i[0], manhattan distance value) aka. (0, 0.2), (1, 0.3)..
		#tip3. use lambda to sort based on manhattan value
		bestcenter = min([ (i[0], distance(x-center[i[0]])) for i in enumerate(center)] , key=lambda t: t[1])[0]
		#Don't need default dictionary
		try:
			clusters[bestcenter].append(x)
		except KeyError:
			clusters[bestcenter] = [x]
	return clusters

# if centroids never change (but the nodes inside it can change..?)
# here use the Lloyd's algorithm to re-evaluate center and converge (centroids never change)
def reevaluate_centers(center, clusters):
	updatecenter = []
	for key in clusters.keys():
		updatecenter.append(np.mean(clusters[key], axis=0))
	return updatecenter
	#return np.asarray(updatecenter)

def converge(oldcluster, newcluster):
	#oldcluster, newcluster type: np.array
	#if use oldcluster, newcluster directly, aka, oldcluster==newcluster, it'll compare each (x,y,) element separately
	#the sequence also differess list(oldcluster) != list(newcluster) [[1, 2], [3, 4]] != [[3,4], [1, 2]], need to transform to a tuple before make it to set
	return set([tuple(a) for a in oldcluster]) == set([tuple(b) for b in newcluster])


def do_kclustering(dataset, K, distance=np.linalg.norm, precision=converge, iteration=10):
	#Randome generate center
	#TODO: check dataset type (np array instead of list)
	size = len(dataset)
	center = random.sample(dataset, K)
	updatecenter = random.sample(dataset, K)
	count = 0
	while not precision(center, updatecenter):
		center = updatecenter
		clusters = cluster_points(dataset, center, distance) #it's a dictionary
		updatecenter = reevaluate_centers(center, clusters)
		count += 1
		if count >= iteration:
			break 

	return (updatecenter, clusters)


def main():
	N = 10
	M = 2
	X = data_generator(N, M)
	K = 2
	res = do_kclustering(X, K, distance=np.linalg.norm, precision=converge, iteration=10)
	print res



if __name__ == '__main__':
	main()

'''
notes:
no knowledge of the k cluster, then random generate the centroids. otherwise, should based on some
gussing. 
'''
