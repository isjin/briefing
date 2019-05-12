import url_parser
import os


class Briefing(object):
    def __init__(self):
        self.url = 'https://www.briefmenow.org/amazon/aws-sap-your-company-policies-require-encryption-of-sensitive-data-at-rest-you-are-considering-the-possible-options-for-protecting-data-while-storing-it-at-rest-on-an-ebs-data-volume-attache/'
        self.urlparser = url_parser.UrlParser()
        self.file = 'AWS-SAP_v3.txt'

    def soup_html(self, url):
        soup = self.urlparser.soup_request(url)
        return soup

    def get_urls(self):
        urls = [self.url]
        html = self.soup_html(self.url).find('ul', class_='wf_toc')
        html_soup = self.urlparser.lxml_html(html)
        tab_as = html_soup.find_all('a')
        for a in tab_as[1:]:
            urls.append(a['href'])
        return urls

    def iterater_url(self):
        # for url in self.get_urls()[0:1]:
        for url in self.get_urls():
            yield url

    @staticmethod
    def result(html):
        answers = []
        tab_ps = html.find_all('p')
        for p in tab_ps:
            if "color" in str(p):
                answers.append(p.text[0])
        return answers

    def main(self):
        if os.path.exists(self.file):
            os.remove(self.file)
        count = 1
        for url in self.iterater_url():
            # print(url)
            html = self.soup_html(url).find('div', class_="entry-content")
            html_content = self.urlparser.lxml_html(html)
            results = self.result(html_content)
            tab_ps = html_content.find_all('p')
            while True:
                try:
                    f = open(self.file, 'a+', encoding='utf-8')
                    f.write('Question ' + str(count) + '\n')
                    if count == 1:
                        f.write(url + '\n')
                    for p in tab_ps:
                        f.write(p.text + '\n')
                    if len(results) == 0:
                        f.write(url + '\n')
                        print(url)
                    answer = ""
                    for result in results:
                        answer = answer + result + ' '
                    f.write('Correct Answer: ' + answer + '\n')
                    f.write('\n')
                    f.close()
                    count += 1
                    break
                except Exception as e:
                    print(e.__str__())


if __name__ == '__main__':
    app = Briefing()
    app.main()
