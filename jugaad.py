__author__ = 'rehan_asif'
#sf_filepath='/Users/rehana/Downloads/feb.tsv'
#bl_filepath='/Users/rehana/Downloads/bl.csv'
from datetime import timedelta,datetime
import time
import numpy as np
import pandas as pd
import math
import json
import sys
import os
import subprocess
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import cm

df_glb = pd.DataFrame()
columns_ad = ['date','Total_Revenue','impression','tick', 'advertiser_namezz']
df_all_ad = pd.DataFrame(columns = columns_ad)
df_all_bar = pd.DataFrame()

advertiser_name=[]
impression_no=[]
revenue_total=[]
rpm_ratio=[]
pub_adv_map=dict()
pub_stat=dict()
count_ad=0



def plot_bar(df ):
    fig = plt.figure()
    count_arr = np.asarray(df.countz)
    ax = fig.add_subplot(111) # Create matplotlib axes
    width = 0.5
    ax.set_xticklabels(df.index)
    df[y].plot(kind = 'bar', color = 'red', ax = ax, width = width, position = 1, legend = lgnd)

    for ii,rect in enumerate(ax.patches):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., .8*height, '%d' % int(count_arr[ii]), ha = 'center', va = 'bottom', rotation = 'vertical')

    ax.set_ylabel(yname)
    ax.set_xlabel(xname)

    plt.title(title)
    plt.figure(figsize = (600, 400))
    print "Save:", filename
    fig.savefig(filename, bbox_inches = 'tight')
    plt.close('all')


def plot_bar_fill_total_revenue(df, filename, xname, yname, yname2, title, lgnd = True):

    fig = plt.figure()
    count_arr = np.asarray(df.countz)
    ax = fig.add_subplot(111) # Create matplotlib axes
    ax2 = ax.twinx() # Create another axes that shares the same x-axis as ax.

    width = 0.3

    df.fill_rate.plot(kind='bar', color='mediumpurple', ax=ax, width=width, position=1, legend=True)
    df.total_revenue.plot(kind='bar', color='g', ax=ax2, width=width, position=0, legend=True)
    ax.set_ylabel(yname)
    ax2.set_ylabel(yname2)

    ax.set_xticklabels(df.index)
    ax.set_xlabel(xname)
    ax.set_ylim([0,100])
    plt.title(title)
    plt.figure(figsize = (1000,400))
    print "Save:", filename
    fig.savefig(filename, bbox_inches = 'tight')
    plt.close('all')

def plot_all_ad( df ):

    #df = df.set_index(df.date)
    
    fig = plt.figure()


    #u, ind = np.unique(df.advertiser_namezz, return_index=True)
    #legend = u[np.argsort(ind)].tolist()
    legend = df.columns.tolist()
    ax = fig.add_subplot(111)
    for i in df.columns :
        df[i].plot(kind = 'line', ax=ax, marker='o')

    #df.groupby(['tick']).plot( y="Total_Revenue", kind='line', ax=ax, marker='o')
    plt.legend(labels=legend, fontsize='small')
    ax.set_ylabel('Total_Revenue($)')
    ax.set_xlabel('Date')
    plt.title('All advertiser comparison')
    fig.savefig('all_line_ad.png', bbox_inches = 'tight')
    plt.close('all')

def plot_all_ad_bar(publisher, df ):
    
    fig = plt.figure()
    #u, ind = np.unique(df.advertiser_namezz, return_index=True)
    legend = df.columns.tolist()
    print legend
    cs=cm.Set1(np.arange(len(legend)*1.)/len(legend))
    ax = fig.add_subplot(111)
    df.plot( kind='bar', ax=ax, legend=True)
    plt.legend(fontsize='small')
    ax.set_ylabel('Total_Revenue($)')
    ax.set_xlabel('Date')
    plt.title('All advertiser comparison')
    fig.savefig('all_bar_ad.png', bbox_inches = 'tight')
    
    plt.close('all')


def plot_line(df ):
    fig = plt.figure()
    ax = fig.add_subplot(111) # Create matplotlib axes
 
    # Create another axes that shares the same x-axis as ax.
    
    df.columns=['time','Active_Users']
    print df
    df['time']= np.array(df.time.tolist()).astype('datetime64[s]')
    df=df.set_index(df.time)
    print df

    df['Active_Users'].plot( kind = 'line', color = 'mediumpurple', ax=ax, marker='o')
    ax.legend(loc = 2)
    ax.set_ylabel('active')
    ax.set_xlabel('Time')
    plt.title('Active User Info')
    plt.figure(figsize = (1200,400))
    fig.savefig('sxdx.png', bbox_inches = 'tight')
    plt.close('all')






def main():



    columns_sf = ['pname','hour','views']
    sf_lld = pd.read_csv('active.csv', header=None)

    plot_line(sf_lld)

if __name__ == '__main__':
    main()

