var request = require('request');
var cheerio = require('cheerio');
var saveArticle = require('../saveArticle.js');

var getKMOXArticles = function () {
	request('http://stlouis.cbslocal.com/category/news/crime/', function (error, response, html) {
		var title, link;
		var articles = [];
		if (!error && response.statusCode == 200) {
			var $ = cheerio.load(html);
			$('.dynamic-lead-slideshow #section-dl .slides li a').each(function(i, element){
				link = $(this).attr('href');
				title = $(this).text();

				// Clean up headlines by spliting text on newline characters
				// Then take first part of headline and remove all \t characters
				title = title.split('\n');
				for (letter in title[4]){
					title[4] = title[4].replace('\t', '');
				}
				// Clean up titles, remove tabs and newlines
				saveArticle(title[4], link, "KMOX");
				
			});
		}
	});
}

module.exports = getKMOXArticles;