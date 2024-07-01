import { Dialog, DialogTitle, Box, TextField, Button, DialogContent } from "@mui/material";
import TextImporter from "./TextImporter";

type ImporterProps = {
    
}

function ItemImporter(props: { open: boolean, onClose: () => void }) {
    const { open, onClose } = props;

    const importerProps = {

    }

    const importerTypes = {
        "text": <TextImporter {...importerProps} />
    }

    return <Dialog open={open} onClose={onClose}>

        <DialogTitle>
            Import Items
        </DialogTitle>

        <DialogContent>
            <Box display="flex" flexDirection="column" gap={2}>
                <TextField
                    label="Import Items"
                    multiline
                    rows={4}
                    fullWidth
                    variant="outlined"
                />

                <Button variant="contained" color="primary">
                    Import
                </Button>
            </Box>
        </DialogContent>
    </Dialog>
}

export default ItemImporter;