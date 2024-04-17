import { Box, TextField, Typography } from "@mui/material";
import { MultiplierOrPrice } from "../adder/ItemList";
import { useState } from "react";

function PriceLabel(props: { price: MultiplierOrPrice }) {
    const { price } = props;

    // Remove anything non numerical from the price
    const priceStr = price.replace(/[^0-9.\-]/g, '');

    // Check if the price contains an 'x' or a 'X'
    const isMultiplier = price.includes('x') || price.includes('X');

    if (isMultiplier) {
        return <Typography variant="h5">{priceStr}x</Typography>
    } else {
        return <Box component="span" display="flex" alignItems="center">
            <Typography variant="h5" mr={1}>{priceStr}</Typography>
            <img height="20" src="https://static.wikia.nocookie.net/hayday/images/6/6d/Coin.png" />
        </Box>
    }
}

function EditablePriceLabel(props: { price: MultiplierOrPrice, onChange: (newPrice: MultiplierOrPrice) => void }) {
    const { price, onChange } = props;
    const [inEditMode, setInEditMode] = useState(false);

    return inEditMode ?
        <TextField value={price}
            onChange={(e) => onChange(e.target.value)}
            onBlur={() => setInEditMode(false)}
            inputRef={input => input && input.focus()}
        /> :
        <Box onClick={() => setInEditMode(true)}>
            <PriceLabel price={price} />
        </Box>
}

export { EditablePriceLabel, PriceLabel }