import { createContext, useContext, useEffect, useState } from "react";
import { UserItemList, UserItemListItemDefinition } from "../components/adder/ItemList";

type SelectedListContextType = {
    selectedList: string | null;
    availableLists: Record<string, UserItemList>;
    getSelectedList: () => UserItemList | null;
    readonly setSelectedList: (list: string) => void;
    readonly setAvailableLists: (lists: Record<string, UserItemList>) => void;
    readonly updateList: (newList: UserItemList) => void;
    readonly addItemToList: (item: UserItemListItemDefinition, additive: boolean) => void;
    readonly removeItemFromList: (item: string) => void;
}

const SelectedListContext = createContext<SelectedListContextType>({
    selectedList: null,
    availableLists: {},
    getSelectedList: () => null,
    setSelectedList: () => { },
    setAvailableLists: () => { },
    updateList: () => { },
    addItemToList: () => { },
    removeItemFromList: () => { }
});

function useSelectedListProvider() {
    const context = useContext(SelectedListContext);
    if (!context) {
        throw new Error("useSelectedListProvider must be used within a SelectedListProvider");
    }

    return context;
}

function createNewList(name: string): UserItemList {
    return {
        name,
        items: []
    }
}

function SelectedListProvider(props: { children: React.ReactNode }) {
    const [selectedList, setSelectedList] = useState<string | null>('Default List');
    const [availableLists, setAvailableLists] = useState<Record<string, UserItemList>>({
        'Default List': createNewList('Default List')
    });

    // Check if there's at least one list 

    useEffect(() => {
        const storedLists = localStorage.getItem('userLists');
        if (storedLists) {
            setAvailableLists(JSON.parse(storedLists));
        }

        if (Object.keys(availableLists).length === 0) {
            setAvailableLists({ 'Default List': createNewList('Default List') });
        }
    }, []);

    useEffect(() => {
        // if (!selectedList && Object.keys(availableLists).length > 0) {
        //     setSelectedList(Object.keys(availableLists)[0]);
        // }
    }, [availableLists]);

    useEffect(() => {
        localStorage.setItem('userLists', JSON.stringify(availableLists));
    }, [availableLists]);

    const handleSetSelectedList = (list: string) => setSelectedList(list);

    return (
        <SelectedListContext.Provider value={{
            selectedList,
            availableLists,
            setAvailableLists,
            setSelectedList: handleSetSelectedList,
            getSelectedList: () => selectedList ? availableLists[selectedList] : null,
            updateList: (newList: UserItemList) => {
                setAvailableLists({ ...availableLists, [newList.name]: newList });
            },
            addItemToList: (item: UserItemListItemDefinition, additive: boolean) => {
                const list = selectedList ? availableLists[selectedList] : null;
                if (!list) return;

                const items = [...list.items];
                if (additive) {
                    // Find the 
                    const existingItem = items.find(i => i.item === item.item);
                    if (existingItem) {
                        existingItem.amount += item.amount;
                    } else {
                        items.push(item);
                    }
                } else {
                    const existingItem = items.find(i => i.item === item.item);
                    if (existingItem) {
                        existingItem.amount = item.amount;
                    } else {
                        items.push(item);
                    }
                    console.log(items);
                }
                setAvailableLists({ ...availableLists, [selectedList!]: {
                    ...list,
                    items
                } });
            },
            removeItemFromList: (item: string) => {
                const list = selectedList ? availableLists[selectedList] : null;
                if (!list) return;
                const items = list.items.filter(i => i.item !== item);
                setAvailableLists({ ...availableLists, [selectedList!]: {
                    ...list,
                    items
                } });
            }
        }}>
            {props.children}
        </SelectedListContext.Provider>
    );
}

export { SelectedListProvider, useSelectedListProvider, createNewList };