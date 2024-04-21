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
            onKeyDown={(e) => {
                if (e.key === 'Enter') {
                    setInEditMode(false);
                }

                if (e.key === 'Escape') {
                    setInEditMode(false);
                }

                // Remove anything non numerical from the price
                const priceStr = price.replace(/[^0-9.\-]/g, '');
                const isMultiplier = price.includes('x') || price.includes('X');
                const incrementBy = isMultiplier ? 1 : 100;

                // Arrow up 
                if (e.key === 'ArrowUp') {
                    const newPrice = parseFloat(priceStr) + incrementBy;
                    const toReplace = price.replace(priceStr, newPrice.toString());

                    // Replace the old price with the new price
                    onChange(toReplace);
                    e.preventDefault();
                    e.stopPropagation();

                }

                // Arrow down
                if (e.key === 'ArrowDown') {
                    const newPrice = parseFloat(priceStr) - incrementBy;
                    const toReplace = price.replace(priceStr, newPrice.toString());

                    // Replace the old price with the new price
                    onChange(toReplace);
                    e.preventDefault();
                    e.stopPropagation();
                }
            }}
        /> :
        <Box onClick={() => setInEditMode(true)}>
            <PriceLabel price={price} />
        </Box>
}

export { EditablePriceLabel, PriceLabel }