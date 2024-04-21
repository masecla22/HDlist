import { Star } from "@mui/icons-material";
import { Box, Dialog, DialogContent, DialogTitle, IconButton, Tooltip, Typography } from "@mui/material";
import { useState } from "react";

function Credits() {
    const [open, setOpen] = useState(false);

    const contributors = {
        "masecla22": "Working on the app",
        "Spiridonas": "Helping with price data"
    }

    return <>
        <Dialog
            open={open}
            onClose={() => setOpen(false)}
        >
            <DialogTitle>Credits</DialogTitle>
            <DialogContent>
                <Typography>
                    This app was created by <a href="https://github.com/masecla22"
                        style={{ color: "#888" }}
                    >masecla22</a> to help people out.
                </Typography>
                <Box mt={2}>
                    <Typography variant="h6">Contributors:</Typography>
                    <ul>
                        {Object.entries(contributors).map(([name, contribution]) => (
                            <li key={name}>
                                <Typography> {name} - {contribution} </Typography>
                            </li>
                        ))}
                    </ul>
                </Box>
            </DialogContent>
        </Dialog>
        <Tooltip title="Credits">
            <IconButton onClick={() => setOpen(true)}>
                <Star />
            </IconButton>
        </Tooltip>
    </>
}

export default Credits;