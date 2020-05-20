Auction Coding Challenge

One of the things that the Engineering team at Sortable works on is software that runs ad auctions, either in the browser or server-side. The goal of this challenge is to write program that will run a simple auction, while enforcing data validity.

Concepts

Sortable manages ads on many different websites. Each site has a different configuration: which bidders are permitted to bid on ads on that site, and an auction 'floor' that bids must exceed.

Each bidder also has a configuration. For this challenge we have significantly reduced the configuration to consist of an adjustment to be applied to each bid to account for the difference between how much the bidder claims that they'll pay, and how much they will actually pay, based on historical data.

Running the auctions

On start-up, your program should load the config file (config.json) which lists all valid sites and bidders, and their respective configurations.

The program should then load the input (JSON) from standard input that contains a list of auctions to run. Each auction lists the site, which ad units are being bid on, and a list of bids that have been requested on your behalf.

For each auction, you should find the highest valid bidder for each ad unit, after applying the adjustment factor. An adjustment factor of -0.01 means that bids are reduced by 1%; an adjustment of 0.05 would increase them by 5%. (Positive adjustments are rare in real life, but possible.) For example, a bid of $0.95 and an adjustment factor of 0.05 (adjusted to $0.9975) will beat a bid of $1.10 with an adjustment factor of -0.1 (adjusted to $0.99). When reporting the winners, use the bid amounts provided by the bidder, rather than the adjusted values.

It is possible that a bidder will submit multiple bids for the same ad unit in the same auction.

A bid is invalid and should be ignored if the bidder is not permitted to bid on this site, the bid is for an ad unit not involved in this auction, the bidder is unknown, or if the adjusted bid value is less than the site's floor.

An auction is invalid if the site is unrecognized, or there are no valid bids. In the case of an invalid auction, just return an empty list.

The output of your program should be a list of auction results. The result of each auction is a list of winning bids.

Inputs

Ensuring that inputs are well-formed (e.g. all fields are present and are of the expected types) is important, but also uninteresting. You may therefore assume that all inputs will be well-formed. All numeric values will be 64-bit floats (as is default for JSON).