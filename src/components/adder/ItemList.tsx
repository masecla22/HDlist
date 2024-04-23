import { Add, Delete, Remove } from "@mui/icons-material";
import { Box, Grid, IconButton } from "@mui/material";
import React from "react";
import { EditableAmountLabel } from "../attributes/AmountLabel";
import { EditablePriceLabel } from "../attributes/PriceLabel";
import { ImageSize } from "./ItemImage";
import ItemLabel from "./ItemLabel";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import itemPrices from "../../constants/Items";

type MultiplierOrPrice = string;

interface UserItemListItemDefinition {
    item: string;
    amount: number;
    multiplierOrPrice: MultiplierOrPrice;
}

interface UserItemList {
    items: UserItemListItemDefinition[];
    name: string;
}

function ItemListItem(props: UserItemListItemDefinition) {
    const { item } = props;
    return <ItemLabel name={item} imageSize={ImageSize.SIXTY_FOUR} />
}

function ItemList() {
    const { getSelectedList, addItemToList } = useSelectedListProvider();
    const { items } = getSelectedList()!;

    return <Box>
        <Grid container>
            {items.map((item, index) => {
                return <React.Fragment key={index}>
                    <Grid item xs={4}>
                        <ItemListItem {...item} />
                    </Grid>
                    <Grid item xs={2} display="flex" alignItems="center">
                        <EditableAmountLabel amount={item.amount} onChange={(newAmount) => {
                            addItemToList({ ...item, amount: newAmount }, false);
                        }} />
                    </Grid>
                    <Grid item xs={4} display="flex" alignItems="center" justifyContent="center">
                        <EditablePriceLabel price={item.multiplierOrPrice}
                            defaultPrice={itemPrices[item.item].price}
                            onChange={(newPrice) => {
                                addItemToList({ ...item, multiplierOrPrice: newPrice }, false);
                            }} />
                    </Grid>
                    <Grid item xs={2} display="flex" alignItems="center" justifyContent="flex-end">
                        <Box>
                            <IconButton onClick={() => {
                                addItemToList({ ...item, amount: item.amount + 1 }, false);
                            }}>
                                <Add />
                            </IconButton>
                            <IconButton onClick={() => {
                                addItemToList({ ...item, amount: item.amount - 1 }, false);
                            }}>
                                <Remove />
                            </IconButton>
                            <IconButton onClick={() => {
                                addItemToList({ ...item, amount: 0 }, false);
                            }}>
                                <Delete />
                            </IconButton>
                        </Box>
                    </Grid>
                </React.Fragment>
            })}
        </Grid>
    </Box>
}

export default ItemList
export type { MultiplierOrPrice, UserItemList, UserItemListItemDefinition };
