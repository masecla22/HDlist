import { createContext, useContext, useEffect, useState } from "react";
import { UserItemList, UserItemListItemDefinition } from "../components/adder/ItemList";

type SelectedListContextType = {
    selectedList: string | null;
    getAvailableLists: () => Record<string, UserItemList>;
    getSelectedList: () => UserItemList | null;
    readonly setSelectedList: (list: string) => void;
    readonly setAvailableLists: (lists: Record<string, UserItemList>) => void;
    readonly updateList: (newList: UserItemList) => void;
    readonly addItemToList: (item: UserItemListItemDefinition, additive: boolean) => void;
    readonly removeItemFromList: (item: string) => void;
}

const SelectedListContext = createContext<SelectedListContextType>({
    selectedList: null,
    getAvailableLists: () => ({}),
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

    useEffect(() => {
        const storedLists = localStorage.getItem('userLists');
        const storedSelectedList = localStorage.getItem('selectedList');
        if (!storedSelectedList) setSelectedList('Default List');

        if (storedSelectedList) {
            setSelectedList(storedSelectedList);
        }
        if (storedLists) {
            setAvailableLists(JSON.parse(storedLists));
        } else if (Object.keys(availableLists).length === 0) {
            setAvailableLists({ 'Default List': createNewList('Default List') });
        }

        // Add a listener for local storage changes
        window.addEventListener('storage', (e) => {
            if (e.key === 'userLists') {
                const storedLists = localStorage.getItem('userLists');
                if (storedLists) {
                    setAvailableLists(JSON.parse(storedLists));
                }
            } else if (e.key === 'selectedList') {
                const storedSelectedList = localStorage.getItem('selectedList');
                if (storedSelectedList) {
                    setSelectedList(storedSelectedList);
                }
            }
        });
    }, []);

    useEffect(() => {
        if (Object.keys(availableLists).length <= 0)
            return;

        // Make sure you don't save the default value, 
        if (Object.keys(availableLists).length === 1 && Object.keys(availableLists)[0] === 'Default List' && !availableLists['Default List'].items.length)
            return;

        localStorage.setItem('userLists', JSON.stringify(availableLists));
        localStorage.setItem('selectedList', selectedList || 'Default List');
    }, [availableLists, selectedList]);

    const handleSetSelectedList = (list: string) => setSelectedList(list);

    return (
        <SelectedListContext.Provider value={{
            selectedList,
            getAvailableLists: () => availableLists,
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
                        existingItem.multiplierOrPrice = item.multiplierOrPrice;
                    } else {
                        items.push(item);
                    }
                }

                const filteredItems = items.filter(i => i.amount > 0);
                setAvailableLists({
                    ...availableLists, [selectedList!]: {
                        ...list,
                        items: filteredItems
                    }
                });
            },
            removeItemFromList: (item: string) => {
                const list = selectedList ? availableLists[selectedList] : null;
                if (!list) return;
                const items = list.items.filter(i => i.item !== item);
                setAvailableLists({
                    ...availableLists, [selectedList!]: {
                        ...list,
                        items
                    }
                });
            }
        }}>
            {props.children}
        </SelectedListContext.Provider>
    );
}

export { SelectedListProvider, useSelectedListProvider, createNewList };