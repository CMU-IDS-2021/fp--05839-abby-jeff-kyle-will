"""In order to run this webscraper you will need all of the packages installed. You will also need a chromdriver 
that matches your version of Google Chrome (REQUIRED). You can get a chromedriver from

    https://chromedriver.chromium.org/downloads. 

Additioannly, if you are using a mac you 
must bring the chromediver out of quarantine with the following command. 

    $xattr -d com.apple.quarantine ./chromedriver

For this code the chromedriver is stored in the same directory as ./chromedriver"""


"""The format of the page being extracted is as follows. This is important to understand in order to understand
the methods below:

MAIN PAGE - VOLUME <Link>
                - PAPER
                    -Title
                    -MetaData <Link>
                        -Date Published
                        Abstract
                    -PDF <Link>
                        -Download PDF
          - VOLUME <Link>
                - PAPER
                    -Title
                    -MetaData <Link>
                        -Date Published
                        Abstract
                    -PDF <Link>
                        -Download PDF
          - VOLUME <Link>
                - PAPER
                    -Title
                    -MetaData <Link>
                        -Date Published
                        Abstract
                    -PDF <Link>
                        -Download PDF
            
            
            ...


"""

import os
from selenium import webdriver
import time
from pdfminer import high_level
from pdfminer.high_level import extract_text
import requests
import json
import re
import bs4
from bs4 import BeautifulSoup

#path to chromedriver
chromedriver = "./chromedriver"

#needed to inialize the chromedriver with the options we desire
def initialize_chromedriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--user-agent=""Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36""')
    return webdriver.Chrome(executable_path = chromedriver, options = options)

#downloads a pdf to local and extracts text (not currently used)
def download_pdf_and_convert_to_text(full_url):
    driver.get(full_url)
    button = driver.find_elements_by_class_name("download")[0]
    button.click()
    print("PDF Downloaded")
    pdf_name = full_url.split("/")[-1]
    print(pdf_name)
    file = open("/Users/will/Downloads/"+pdf_name, 'wb')
    file.write(response.read())
    file.close()
    print("Downloaded and Stored PDF: "+ pdf_name)
    text = extract_text(pdf_name)
    return text

#extract all abstracts from each paper page
def extract_texts(links):
    texts = []
    for link in links:
        texts.append(download_pdf_and_convert_to_text(link))
    return texts

#extract abstract from paper page meta data
def extract_abstract(paper_meta_url):
    driver.get(paper_meta_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    abstract = soup.find_all("div", class_="article-abstract")[0].text
    abstract = abstract.replace("\t", "").replace("\n", "")
    return (abstract)

#downloads pdf to local
def download_pdf_to_local(full_url):
    response = urllib.request.urlopen(full_url)
    print("PDF Downloaded")
    pdf_name = full_url.split("/")[-1]
    print(pdf_name)
    file = open(pdf_name, 'wb')
    file.write(response.read())
    file.close()
    print("Downloaded and Stored PDF: "+ pdf_name)
    return pdf_name

#extract all dates for all papers from each paper page
def extract_date(paper_meta_url):
    driver.get(paper_meta_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    date_link_field = soup.find_all("div", class_="list-group-item date-published")[0].text
    date_link_field = date_link_field.replace("Published:", "").replace("\t", "").replace("\n", "")
    return (date_link_field)

#extract the pdf links for all articles from the volume page
def extract_pdf_links(volume_page_url):
    driver.get(volume_page_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    pdf_links_unparsed = soup.find_all("a", class_="galley-link btn btn-primary pdf")
    pdf_links = []
    for unparsed_link in pdf_links_unparsed:
        pdf_links.append(unparsed_link.get("href"))
    return (pdf_links)

#extract all titles for all papers from the volume page
def extract_titles(volume_page_url):
    driver.get(volume_page_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    titles_unparsed = soup.find_all("h3", class_="media-heading")
    titles = []
    for unparsed_title in titles_unparsed:
        titles.append(unparsed_title.text.replace("\t", "").replace("\n", ""))
    return (titles)

#extract the links for all paper page meta data from the volume page
def extract_meta_page_links(volume_page_url):
    driver.get(volume_page_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    meta_links_unparsed = soup.find_all("h3", class_="media-heading")
    meta_links = []
    for unparsed_meta_link in meta_links_unparsed:
        meta_links.append(unparsed_meta_link.find("a").get("href"))
    return (meta_links)

#extract the links for all volume pages from the main site
def extract_volume_page_links(page_url):
    driver.get(page_url)
    new_html = driver.page_source
    soup = BeautifulSoup(new_html, "html.parser")
    meta_links_unparsed = soup.find_all("h2", class_="media-heading")
    meta_links = []
    for unparsed_meta_link in meta_links_unparsed:
        meta_links.append(unparsed_meta_link.find("a").get("href"))
    return (meta_links)

#extract all dates, abstracts from all paper page meta data given links
def extract_all_dates_and_abstracts(volume_page_url):
    links = extract_meta_page_links(volume_page_url)
    dates = []
    abstracts = []
    for link in links:
        dates.append(extract_date(link))
        abstracts.append(extract_abstract(link))
    return dates, abstracts

#main runner for volume, extracts all data from a volume
def extract_volume_data(volume_page_url):
    dates, abstracts = extract_all_dates_and_abstracts(volume_page_url)
    pdf_links = extract_pdf_links(volume_page_url)
    titles = extract_titles(volume_page_url)
    #texts = extract_texts(pdf_links)
    return dates, abstracts, titles
        
#auxilliary used to combine list    
def combine_list(l1, l2):
    for item in l2:
        l1.append(item)
    return l1

#parse year from paper date
def extract_year(date):
    return date[-4:]

#turn into  list of json for processing
def turn_into_json_list(titles, dates, abstracts):
    json_list = []
    for i in range (len(titles)):
        json = {}
        json["Title"] = titles[i]
        json["Date"] = extract_year(dates[i])
        json["Text"] = abstracts[i]
        json_list.append(json)
    return json_list

    def corpus_by_year(json_list):
    corpus_by_year_json = {}
    for json in json_list:
        year = json["Date"]
        print(year)
        if year in corpus_by_year_json.keys():
            corpus_by_year_json[year] = corpus_by_year_json[year] + " " + json["Text"]
        else:    
            corpus_by_year_json[year] = json["Text"]
    return corpus_by_year_json

def title_by_year(json_list):
    corpus_by_year_json = {}
    for json in json_list:
        year = json["Date"]
        print(year)
        if year in corpus_by_year_json.keys():
            corpus_by_year_json[year] = corpus_by_year_json[year] + " " + json["Title"]
        else:    
            corpus_by_year_json[year] = json["Title"]
    return corpus_by_year_json
            
def all_corpus(json_list):
    corpus = ""
    for json in json_list:
        corpus = corpus + " " + json["Text"]
    return corpus

#page url
page_url = "https://jair.org/index.php/jair/issue/archive"

#Initialize ChromeDriver
driver = initialize_chromedriver()
#the main driver starts here by calling extract volume data on all volumes
volume_links = extract_volume_page_links(page_url)
total_dates = []
total_titles = []
total_texts = []

for volume_link in volume_links:
    dates, abstracts, titles = extract_volume_data(volume_link)
    total_titles = combine_list(total_titles, titles)
    total_dates = combine_list(total_dates, dates)
    total_texts = combine_list(total_texts, abstracts)

json_list = turn_into_json_list(total_titles, total_dates, total_texts)

output_abstract = open("output_abstract.txt", "w")
output_abstract.write(str(json_list))
output_abstract.close()
        
all_corpus_text = all_corpus(json_list)
corpus_by_year_text = corpus_by_year(json_list)
title_by_year_text = title_by_year(json_list)

output_corpus = open("whole_corpus.txt", "w")
output_corpus.write(str(all_corpus_text))
output_corpus.close()

output_corpus_year = open("corpus_by_year.txt", "w")
output_corpus_year.write(str(corpus_by_year_text))
output_corpus_year.close()

output_title_year = open("title_by_year.txt", "w")
output_title_year.write(str(title_by_year_text))
output_title_year.close()