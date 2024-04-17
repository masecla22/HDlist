import { Box, Typography } from "@mui/material";
import ItemImage, { ImageSize } from "./ItemImage";

function ItemLabel(props: {
    name: string,
    imageSize?: ImageSize,
}) {
    const { name } = props;
    const imageSize = props.imageSize || ImageSize.THIRTY_TWO;

    return <Box component="span" display="flex" alignItems="center">
        <ItemImage name={name} size={imageSize} />
        <Typography ml={1} variant="h5">
            {name}
        </Typography>
    </Box>
}

export default ItemLabel
