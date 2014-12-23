var request = require('request');
var cheerio = require('cheerio');
var saveArticle = require('../saveArticle.js');

var getKSDKFeaturedArticles = function () {
	request('http://www.ksdk.com/local/crime-news/', function (error, response, html) {
		var title, link;
		var articles = [];
		if (!error && response.statusCode == 200) {
			var $ = cheerio.load(html);
			$('.hero-text a.load-story').each(function(i, element){
				title = $(this).text();
				link = "http://www.ksdk.com" + $(this).attr('href');
				saveArticle(title, link, "KSDK" );
			});
		}
	});
}

module.exports = getKSDKFeaturedArticles;