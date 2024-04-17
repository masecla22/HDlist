import { Add, Delete } from "@mui/icons-material";
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, FormControl, IconButton, InputLabel, MenuItem, Select, TextField, Tooltip, Typography } from "@mui/material";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import { useState } from "react";

function NewListDialog(props: {
    open: boolean,
    onClose: () => void,
    onNewList: (name: string) => void
}) {
    const { open, onClose, onNewList } = props
    const [name, setName] = useState<string>("");

    return <Dialog
        open={open}
        onClose={onClose}
    >
        <DialogTitle>New List</DialogTitle>
        <DialogContent>
            <TextField
                autoFocus
                margin="dense"
                id="name"
                label="List Name"
                type="text"
                fullWidth
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
        </DialogContent>
        <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button onClick={() => {
                onNewList(name);
                onClose();
            }}>Create</Button>
        </DialogActions>
    </Dialog>
}

function ListSelector() {
    const { selectedList, availableLists, setSelectedList, setAvailableLists } = useSelectedListProvider();
    const [newListDialogOpen, setNewListDialogOpen] = useState<boolean>(false);

    return <>
        <NewListDialog open={newListDialogOpen} onClose={() => setNewListDialogOpen(false)} onNewList={(name) => {
            setAvailableLists({ ...availableLists, [name]: { name, items: [] } });
            setSelectedList(name);
        }} />
        <Box display="flex" gap={2} alignItems="center">
            <Box flex="0 0 20%">
                <Typography variant="h4" noWrap>
                    List Selected
                </Typography>
            </Box>
            <Box flex="0 0 50%">
                <FormControl fullWidth>
                    <InputLabel id="list-select-label">Select List</InputLabel>
                    <Select
                        labelId="list-select-label"
                        label="Select List"
                        id="list-select"
                        value={selectedList}
                        onChange={(e) => setSelectedList(e.target.value!)}
                    >
                        {Object.values(availableLists).map(list => (
                            <MenuItem key={list.name} value={list.name}>{list.name}</MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Box>
            <Box flex="0 0 20%">
                <IconButton onClick={() => setNewListDialogOpen(true)} >
                    <Add />
                </IconButton>
                {availableLists && Object.keys(availableLists).length > 1 &&
                    <Tooltip title="Delete List">
                        <IconButton
                            onClick={() => {
                                const newAvailableLists = { ...availableLists };
                                delete newAvailableLists[selectedList!];
                                setAvailableLists(newAvailableLists);
                                setSelectedList(Object.keys(newAvailableLists)[0]);
                            }}
                        >
                            <Delete />
                        </IconButton>
                    </Tooltip>
                }
            </Box>
        </Box></>
}

export default ListSelector