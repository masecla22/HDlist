import itemPrices from "../constants/Items"
import fuzzysort from "fuzzysort";


function searchForItems(query: string): Fuzzysort.Results {
    const toSearch = Object.keys(itemPrices);

    const results = fuzzysort.go(query, toSearch, {
        limit: 5,
        threshold: -10000,
    });

    return results;
}

export default searchForItems;