import { Box, IconButton, Tooltip, Typography } from "@mui/material";
import itemPrices from "../../constants/Items";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import { UserItemList } from "../adder/ItemList";
import { ItemImageCustomSize } from "../adder/ItemImage";
import { QuestionMarkOutlined } from "@mui/icons-material";

function calculatePrice(list: UserItemList) {
    if (!list) return [0, 0];
    let result = 0;
    let totalItems = 0;

    for (const item of list.items) {
        const price = item.multiplierOrPrice;
        // Remove anything non numerical from the price
        const priceStr = price.replace(/[^0-9.\-]/g, '');

        // Check if the price contains an 'x' or a 'X'
        const isMultiplier = price.includes('x') || price.includes('X');

        const pricePer = isMultiplier ?
            parseFloat(priceStr) * itemPrices[item.item].price :
            parseFloat(priceStr);

        result += pricePer * item.amount;
        totalItems += item.amount;
    }

    return [result, totalItems];
}

function getPriceDisplay(list: UserItemList) {
    const [price, count] = calculatePrice(list);

    const itemsToConvertTo = [
        "Blanket",
        "Diamond ring",
        "Violet dress",
        "Wooly chaps"
    ]

    return <Box>
        <Box display="flex" alignItems="center">
            <Typography variant="h5" mr={0.5}>
                Total Price: {price.toLocaleString(undefined)}
            </Typography>
            <img height="20" src="https://static.wikia.nocookie.net/hayday/images/6/6d/Coin.png" />
            <Typography variant="h5" ml={0.5}>
                ({count} item{count > 1 ? "s" : ""})
            </Typography>
        </Box>
        {itemsToConvertTo.map((item, index) => <Box key={index} display="flex" alignItems="center">
            <Typography variant="h5" mr={0.5}>
                {item}: {(price / itemPrices[item].price).toFixed(2)}
            </Typography>
            <ItemImageCustomSize name={item} size={20} />
        </Box>)}
    </Box>
}

function PriceCalculator() {
    const { getSelectedList } = useSelectedListProvider();


    return <Box position="relative">
        <Typography component={'span'}>
            {getPriceDisplay(getSelectedList()!)}
        </Typography>

        <Box position="absolute" top={10} right={10}>
            <Tooltip title="Trading is done with one player setting all items to 1, and then purchasing them back at max price to transfer coins.">
                <IconButton>
                    <QuestionMarkOutlined />
                </IconButton>
            </Tooltip>
        </Box>
    </Box>
}

export default PriceCalculator