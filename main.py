from flask import Flask, render_template, request
import os

from analysis import papermanager
from analysis import textanalyzer

app = Flask(__name__)

PDF_FILE_TEMP = '/tmp/temp.pdf'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        pm = papermanager.PaperManager()
        text = None
        data = None

        n_keywords = int(request.form['n_keywords'])
        keyword = request.form['keyword']

        if 'analyze_doi' in request.form:
            paper_doi = request.form['paper_doi']
            if paper_doi:
                try:
                    pm.download_paper(paper_doi, PDF_FILE_TEMP)
                    if os.path.exists(PDF_FILE_TEMP):
                        text = pm.extract_text(PDF_FILE_TEMP)
                        os.remove(PDF_FILE_TEMP)
                except:
                    return render_template('home.html', message="Couldn't fetch paper, try to upload the pdf file.")

        if 'analyze_pdf' in request.form:
            pdf_file = request.files['pdf_file']
            if pdf_file:
                try:
                    pdf_file.save(PDF_FILE_TEMP)
                    text = pm.extract_text(PDF_FILE_TEMP)
                    os.remove(PDF_FILE_TEMP)
                except:
                    return render_template('home.html', message="Error reading pdf file.")

        if text:
            ta = textanalyzer.TextAnalyzer()
            data = dict()

            data['n_words'] = ta.count_words(text)
            data['keywords_list'] = ta.keywords(text, n_keywords)
            if keyword:
                data['keyword'] = keyword
                data['frequency'] = ta.frequency(text, keyword)
                sentences = ta.find_sentences(text, keyword)
                data['sentences'] = list(map(ta.clean_sentence, sentences))
                # data['sentences'] = list(filter(ta.valid_sentence, sentences))

        return render_template('home.html', data=data)


# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=5555)

if __name__ == '__main__':
    app.run()
