import { Box, Typography } from "@mui/material";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import { ItemImageCustomSize } from "../adder/ItemImage";
import { UserItemList } from "../adder/ItemList";
import { PriceLabel } from "../attributes/PriceLabel";

function ItemGrid(props: {
    list: UserItemList
}) {
    const { list } = props;
    return <Box display="flex" gap={1} flexWrap={"wrap"}>
        {list.items.map((item, index) => {
            return <Box key={index} sx={{
                position: "relative",
                border: "1px solid #bbb",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                width: "110px",
                height: "110px",
            }}>
                <Box
                    sx={{
                        position: "absolute",
                        top: 0,
                        left: 0,
                        textShadow: "2px 1px 1px #000",
                        padding: "5px",
                        borderRadius: "5px",
                        zIndex: 890,
                    }}
                >
                    <Typography variant="h5">{item.amount}</Typography>
                </Box>
                <Box sx={{
                    position: "absolute",
                    bottom: 0,
                    right: 0,
                    textShadow: "1px 1px 1px #000",
                    padding: "5px",
                    borderRadius: "5px",
                    zIndex: 890,
                }}
                >
                    <PriceLabel price={item.multiplierOrPrice} />
                </Box>
                <ItemImageCustomSize name={item.item} size={80} />
            </Box>
        })}
    </Box>
}

function ListDisplayer() {
    const { getSelectedList } = useSelectedListProvider();

    return <Box>
        {getSelectedList() && <ItemGrid list={getSelectedList()!} />}
    </Box>
}

export default ListDisplayer