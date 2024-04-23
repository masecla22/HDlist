import { Add, CallMerge, Delete } from "@mui/icons-material";
import { Box, Button, Dialog, DialogActions, DialogContent, DialogTitle, FormControl, IconButton, InputLabel, MenuItem, Select, TextField, Tooltip, Typography } from "@mui/material";
import { useState } from "react";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import ListMerger from "./ListMerger";

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
                onKeyDown={(e) => {
                    if (e.key === "Enter") {
                        onNewList(name);
                        setName("");
                        onClose();
                    }
                }}
            />
        </DialogContent>
        <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button onClick={() => {
                onNewList(name);
                setName("");
                onClose();
            }}>Create</Button>
        </DialogActions>
    </Dialog>
}

function ListSelector() {
    const { selectedList, getAvailableLists, setSelectedList, setAvailableLists } = useSelectedListProvider();
    const [newListDialogOpen, setNewListDialogOpen] = useState<boolean>(false);
    const [mergerDialogOpen, setMergerDialogOpen] = useState<boolean>(false);

    return <>
        <NewListDialog open={newListDialogOpen} onClose={() => setNewListDialogOpen(false)} onNewList={(name) => {
            setAvailableLists({ ...getAvailableLists(), [name]: { name, items: [] } });
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
                        {Object.values(getAvailableLists()).map(list => (
                            <MenuItem key={list.name} value={list.name}>{list.name}</MenuItem>
                        ))}
                    </Select>
                </FormControl>
            </Box>
            <Box flex="0 0 20%">
                <IconButton onClick={() => setNewListDialogOpen(true)} >
                    <Add />
                </IconButton>
                {getAvailableLists() && Object.keys(getAvailableLists()).length > 1 &&
                    <>
                        <Tooltip title="Delete List">
                            <IconButton
                                onClick={() => {
                                    const newAvailableLists = { ...getAvailableLists() };
                                    delete newAvailableLists[selectedList!];
                                    setAvailableLists(newAvailableLists);
                                    setSelectedList(Object.keys(newAvailableLists)[0]);
                                }}
                            >
                                <Delete />
                            </IconButton>
                        </Tooltip>
                        <Tooltip title="Merge Lists">
                            <IconButton onClick={() => setMergerDialogOpen(true)}>
                                <CallMerge />
                            </IconButton>
                        </Tooltip>
                    </>
                }
            </Box>

            <ListMerger open={mergerDialogOpen} onClose={() => setMergerDialogOpen(false)} />
        </Box></>
}

export default ListSelector