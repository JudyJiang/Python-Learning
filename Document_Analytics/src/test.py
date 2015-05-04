from doc import*
import pandas
import matplotlib.pyplot as plt

contributes=pandas.read_csv(contributorFile,delimiter='\t',names=contributorHeader)
documents = list(packRecordObject(readcsv, docFile, '\t', header,key='docid',fields=['category']))
contributeStats = list(controlCompare(documents, None, changeFields='contributorid'))


def plot1():
	contribute=pandas.DataFrame(contributes,columns=contributorHeader)
	contributeStat=pandas.DataFrame(contributeStats,columns=['contributorid','downloads','downloadNum','viewNum'])

	histRange=len(contributeStat)
	hist= [len([contributeStat.iloc[index] for index in range(histRange) if contributeStat.iloc[index]['downloads'] <= 10]),
	         len([contributeStat.iloc[index] for index in range(histRange) if contributeStat.iloc[index]['downloads'] > 10 and contributeStat.iloc[index]['downloads']<=100]),
	         len([contributeStat.iloc[index] for index in range(histRange) if contributeStat.iloc[index]['downloads'] > 100 and contributeStat.iloc[index]['downloads']<=1000]),
	         len([contributeStat.iloc[index] for index in range(histRange) if contributeStat.iloc[index]['downloads'] >1000])]

	
	contribute[['contributorid', 'totalContribution']] = contribute[['contributorid', 'totalContribution']].astype(int)
	contribute = contributes.set_index(['contributorid'])

	contributeStat[['contributorid', 'downloads','downloadNum','viewNum']] = contributeStat[['contributorid', 'downloads','downloadNum','viewNum']].astype(int)
	contributeStat = contributeStat.set_index(['contributorid'])

	totalDownloadTimes=sum(contributeStat['downloadNum'])
	res = contribute.join(contributeStat)

	topContributor= res.loc[res['downloads'] >= 1000]
	sortedTop = topContributor.sort[['downloads','downloadNum'], ascending=True)
	#those contributors whose downloads are top

plot1()