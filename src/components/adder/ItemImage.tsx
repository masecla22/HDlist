enum ImageSize {
    THIRTY_TWO = 32,
    SIXTY_FOUR = 64,
    ONE_HUNDRED_TWENTY_EIGHT = 128,
    TWO_HUNDRED_FIFTY_SIX = 256,
}

function ItemImage(props: {
    name: string,
    size: ImageSize,
}) {
    const { name, size } = props
    return <img src={`/assets/images_${size}/${name}.png`} alt={props.name} />
}

function ItemImageCustomSize(props: {
    name: string,
    size: number,
}) {
    const { name, size } = props

    // Find the smallest value in the enum that is greater than the size
    let closestSize = 32;
    while(closestSize < size && closestSize < 256) 
        closestSize *= 2;

    // Return the image from the closestSize with a modified height and width to match the size
    return <img src={`/assets/images_${closestSize}/${name}.png`} alt={props.name} height={size} width={size} />
}

export default ItemImage
export { ImageSize, ItemImageCustomSize }