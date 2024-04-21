import { Box, Button, Checkbox, Dialog, DialogActions, DialogContent, DialogTitle, FormControl, Grid, MenuItem, TextField } from "@mui/material";
import { useState } from "react";
import { useSelectedListProvider } from "../../contexts/SelectedListProvider";
import { UserItemList, UserItemListItemDefinition } from "../adder/ItemList";

function executeMerge(targetList: UserItemList, sourceLists: UserItemList[], deleteSourceLists: boolean,
    setAvailableLists: (lists: { [key: string]: UserItemList }) => void,
    availableLists: { [key: string]: UserItemList }) {

    const newItems: Record<string, UserItemListItemDefinition> = {};

    for (const item of targetList.items) {
        newItems[item.item] = item;
    }

    for (const sourceList of sourceLists) {
        for (const item of sourceList.items) {
            if (newItems[item.item]) {
                newItems[item.item].amount += item.amount;
            } else {
                newItems[item.item] = item;
            }
        }
    }

    const newList = {
        name: targetList.name,
        items: Object.values(newItems)
    } as UserItemList;

    const newLists = { ...availableLists, [newList.name]: newList };
    if (deleteSourceLists) {
        for (const sourceList of sourceLists) {
            delete newLists[sourceList.name];
        }
    }

    setAvailableLists(newLists);
}

function ListMerger(props: {
    open: boolean,
    onClose: () => void,
}) {
    const { open, onClose } = props

    const { availableLists, setAvailableLists } = useSelectedListProvider();

    const [targetList, setTargetList] = useState<UserItemList>(availableLists[Object.keys(availableLists)[0]]);
    const [sourceLists, setSourceLists] = useState<UserItemList[]>([]);
    const [deleteSourceLists, setDeleteSourceLists] = useState<boolean>(false);


    return <Dialog
        open={open}
        onClose={onClose}
        fullWidth
    >
        <DialogTitle>
            <Box display="flex" justifyContent="space-between">
                <Box>
                    Merge Lists
                </Box>
                <Box display="flex" alignItems="center">
                    <Checkbox checked={deleteSourceLists} onChange={(e) => setDeleteSourceLists(e.target.checked)} />
                    <Box>
                        Delete Original Lists
                    </Box>
                </Box>
            </Box>
        </DialogTitle>
        <DialogContent>
            <Grid container>
                <Grid item xs={12} md={4}>
                    <Box my={1}>
                        Copying into
                    </Box>
                </Grid>
                <Grid item xs={12} md={8}>
                    <Box my={1}>
                        Copying from
                    </Box>
                </Grid>
            </Grid>
            <Grid container display="flex" alignContent="center" alignItems="center">
                <Grid item xs={12} md={4}>
                    <FormControl fullWidth>
                        <TextField
                            select
                            label="Target List"
                            value={targetList.name}
                            onChange={(e) => {
                                setTargetList(availableLists[e.target.value]);
                                setSourceLists(sourceLists.filter((list) => list !== availableLists[e.target.value]));
                            }}
                            fullWidth
                        >
                            {Object.keys(availableLists).map((listName) => {
                                return <MenuItem key={listName} value={listName}>{listName}</MenuItem>
                            })}
                        </TextField>
                    </FormControl>
                </Grid>
                <Grid item xs={12} md={8}>
                    <Grid container pl={3}>
                        {Object.keys(availableLists).map((listName) => {
                            if (listName === targetList.name) {
                                return null;
                            }
                            return <Grid item xs={12} sm={6} md={6} key={listName}>
                                <Checkbox checked={sourceLists.includes(availableLists[listName])}
                                    onChange={(e) => {
                                        if (e.target.checked) {
                                            setSourceLists([...sourceLists, availableLists[listName]]);
                                        } else {
                                            setSourceLists(sourceLists.filter((list) => list !== availableLists[listName]));
                                        }
                                    }}
                                />
                                {listName}
                            </Grid>
                        })}
                    </Grid>
                </Grid>
            </Grid>

            <Box mt={2}>
                This will {deleteSourceLists ? "move" : "copy"} {sourceLists.map((list) => list.items.map(c => c.amount).reduce((a, b) => a + b, 0)).reduce((a, b) => a + b, 0)} items
                from {sourceLists.length} lists into {targetList.name} {deleteSourceLists ? "and delete the original lists" : ""}
                <br />
                <br />
                Prices will be kept from target list if possible, otherwise from whichever list the comes first.
            </Box>
        </DialogContent>
        <DialogActions>
            <Button onClick={onClose}>Cancel</Button>
            <Button onClick={() => {
                executeMerge(targetList, sourceLists, deleteSourceLists, setAvailableLists, availableLists);
                setSourceLists([]);
                onClose();
            }}>Confirm</Button>
        </DialogActions>
    </Dialog>
}

export default ListMerger