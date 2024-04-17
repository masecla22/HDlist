import { Box, TextField, Typography } from "@mui/material"
import { useState } from "react"

function AmountLabel(props: { amount: number }) {
    const { amount } = props
    return <Typography variant="h6">{amount} Pieces</Typography>
}

function EditableAmountLabel(props: {
    amount: number,
    onChange: (newAmount: number) => void
}) {
    const { amount, onChange } = props
    const [inEditMode, setInEditMode] = useState(false)

    return inEditMode ?
        <TextField value={amount}
            onChange={(e) => onChange(parseInt(e.target.value))}
            inputProps={{ type: 'number' }}
            onBlur={() => setInEditMode(false)}
            inputRef={input => input && input.focus()}
        /> :
        <Box onClick={() => setInEditMode(true)}>
            <AmountLabel amount={amount} />
        </Box>
}

export { EditableAmountLabel, AmountLabel }
