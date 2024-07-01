import { Add, ImportExport } from "@mui/icons-material"
import { Box, IconButton, ListItemIcon, ListItemText, MenuItem, MenuList, Paper, TextField, Tooltip, Typography } from "@mui/material"
import fuzzysort from "fuzzysort"
import React, { useEffect, useState } from "react"
import { useSelectedListProvider } from "../../contexts/SelectedListProvider"
import searchForItems from "../../search/ItemSearch"
import ItemImage, { ImageSize } from "../adder/ItemImage"
import { MultiplierOrPrice } from "../adder/ItemList"
import ItemImporter from "./importer/ItemImporter"

function ItemAdder() {
    const [currentQuery, setCurrentQuery] = useState<string>("")

    const [searchResults, setSearchResults] = useState<Fuzzysort.Results>();
    const [queryFocused, setQueryFocused] = useState<boolean>(false);

    const [currentQuantity, setCurrentQuantity] = useState<number>(1);
    const [multiplierOrPrice, setMultiplierOrPrice] = useState<MultiplierOrPrice>("5x");

    const [queryRef, setQueryRef] = useState<HTMLInputElement | null>(null);
    const [quantityRef, setQuantityRef] = useState<HTMLInputElement | null>(null);

    const [openImporter, setOpenImporter] = useState<boolean>(false);

    const { addItemToList } = useSelectedListProvider();

    const handleEnterKey = (e: React.KeyboardEvent) => {
        if (!searchResults || searchResults.length == 0) return;
        if (e.key != "Enter") return;

        const additive = e.ctrlKey;
        const item = searchResults[0].target;

        addItemToList({
            item,
            amount: currentQuantity,
            multiplierOrPrice
        }, additive);

        setCurrentQuery("");
        setCurrentQuantity(1);
        setMultiplierOrPrice("5x");
        setSearchResults(undefined);

        // Switch focus back to first textbox
        if (queryRef) {
            queryRef.focus();
        }
    }

    useEffect(() => {
        if (currentQuery.length > 0) {
            setSearchResults(searchForItems(currentQuery));
        }
    }, [currentQuery])

    return <Box display="flex" alignItems="center" my={2} gap={2}
        justifyContent="space-between"
    >
        <Box height="75px" width="75px" border="1px solid #eee" borderRadius="10px"
            display="flex" alignItems="center" justifyContent="center"
        >
            {currentQuery.length > 0 && searchResults && searchResults.length > 0 ?
                <ItemImage name={searchResults[0].target} size={ImageSize.SIXTY_FOUR} /> :
                null
            }
        </Box>

        <Box>
            <TextField
                label="Add Item"
                autoComplete="off"
                value={currentQuery}
                onChange={(e) => {
                    const newText = e.target.value;
                    if (newText.length == 0) {
                        setSearchResults(undefined);
                        setCurrentQuery("");
                        return;
                    }

                    const lastChar = newText[newText.length - 1];
                    const isNumber = !isNaN(parseInt(lastChar));

                    if (!isNumber) {
                        setCurrentQuery(newText);
                        return;
                    }

                    if (!searchResults || searchResults.length == 0) {
                        setCurrentQuery(newText);
                        return;
                    }

                    // Autocomplete to the index result
                    let index = parseInt(lastChar);
                    if (index > 0 && index <= searchResults.length) {
                        setCurrentQuery(searchResults[index - 1].target);
                        if (quantityRef)
                            quantityRef.focus();
                    }
                }}
                onFocus={() => setQueryFocused(true)}
                onBlur={(e) => {
                    var attr = null;
                    var element = e.relatedTarget;
                    while (element && !attr) {
                        attr = element.attributes.getNamedItem("itemdata");
                        element = element.parentElement;
                    }
                    setQueryFocused(false);

                    if (attr) {
                        setCurrentQuery(attr.value);
                        if (quantityRef)
                            quantityRef.focus();
                    }
                }}
                onKeyDown={handleEnterKey}
                inputRef={input => {
                    setQueryRef(input);
                }}
            />
            {searchResults && queryFocused && currentQuery.length > 0 && searchResults.length > 0 &&
                !(searchResults.length == 1 && searchResults[0].target.toLowerCase() == currentQuery.toLowerCase()) &&
                <Paper tabIndex={-1} sx={{ width: 320, maxWidth: '100%', position: "absolute", zIndex: 20 }} >
                    <MenuList tabIndex={-1}>
                        {searchResults.map((result, index) =>
                            // @ts-ignore
                            <MenuItem key={index} tabIndex={-1} onClick={() => {
                                setCurrentQuery(result.target);
                            }}
                                itemdata={result.target}
                            >
                                <ListItemIcon tabIndex={-1}>
                                    <ItemImage name={result.target} size={ImageSize.THIRTY_TWO} />
                                </ListItemIcon>
                                <ListItemText tabIndex={-1} sx={{ ml: 2 }}>
                                    <div dangerouslySetInnerHTML={{
                                        __html: fuzzysort.highlight(result, "<b><u>", "</u></b>") || result.target
                                    }} />
                                </ListItemText>
                                <Typography tabIndex={-1} variant="body2" color="text.secondary">
                                    {index + 1}
                                </Typography>
                            </MenuItem>
                        )}
                    </MenuList>
                </Paper>
            }
        </Box>

        <TextField
            label="Quantity"
            type="number"
            autoComplete="off"
            value={currentQuantity}
            onChange={(e) => setCurrentQuantity(parseInt(e.target.value))}
            onKeyDown={handleEnterKey}
            inputRef={input => {
                setQuantityRef(input);
            }}
        />

        <TextField
            label="Multiplier/Price"
            autoComplete="off"
            value={multiplierOrPrice}
            onChange={(e) => setMultiplierOrPrice(e.target.value)}
            onKeyDown={handleEnterKey}
        />

        <Tooltip title={
            <Typography variant="body2">
                You can use Enter to add an item and override it, but if you press CTRL+Enter it'll add the items on top!
            </Typography>
        }>
            <IconButton onClick={(e) => handleEnterKey({ key: "Enter", ctrlKey: e.ctrlKey } as any)}>
                <Add />
            </IconButton>
        </Tooltip>

        <Tooltip title={
            <Typography variant="body2">
                Use this to import items in bulk!
            </Typography>
        }>
            <IconButton onClick={() => setOpenImporter(true)}>
                <ImportExport />
            </IconButton>
        </Tooltip>

        <ItemImporter open={openImporter} onClose={() => setOpenImporter(false)} />
    </Box>
}

export default ItemAdder