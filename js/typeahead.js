$.typeahead({
    input: '.js-typeahead-tickers',
    order: "desc",
    source: {
        data: [
           "AAPL", "FB", "TWTR", "NFLX", "GOOG", "AMZN", "F", "T", "C", "S", "MSFT", "INTC", "GILD", 
		   "NVDA", "GLD", "GDX", "CSCO", "AAL", "GE", "XOM", "IBM", "ORCL", "QCOM", "GRPN", "MU", "SIRI", 
		   "EBAY", "TSLA"
        ]
    },
    callback: {
        onInit: function (node) {
            console.log('Typeahead Initiated on ' + node.selector);
        }
    }
});