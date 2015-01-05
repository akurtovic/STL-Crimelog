var request = require('request');
var cheerio = require('cheerio');
var moment = require('moment');

// Load scraper for all content sources
var getPostDispatchFeaturedArticles = require('./scrapers/PDFeatured.js');
var getPostDispatchArticles = require('./scrapers/PD.js');
var getKMOXFeaturedArticles = require('./scrapers/KMOXFeatured.js');
var getKSDKFeaturedArticles = require('./scrapers/KSDKFeatured.js');


// Execute scrapers
getPostDispatchFeaturedArticles();
getPostDispatchArticles();
getKMOXFeaturedArticles();
getKSDKFeaturedArticles();