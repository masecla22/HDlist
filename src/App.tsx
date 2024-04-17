import { DarkMode, LightMode } from "@mui/icons-material";
import { Box, IconButton, Typography } from "@mui/material";
import { useContext } from "react";
import "./App.css";
import ItemList from "./components/adder/ItemList";
import ItemAdder from "./components/item/ItemAdder";
import ListSelector from "./components/list/ListSelector";
import { ColorModeContext } from "./contexts/ColorModeProvider";
import ListDisplayer from "./components/list/ListDisplayer";
import PriceCalculator from "./components/attributes/PriceCalculator";

function App() {
  const { toggleColorMode, currentTheme } = useContext(ColorModeContext);

  return (
    <>
      <Box position="absolute" top={10} right={10} zIndex={10}>
        <IconButton onClick={toggleColorMode} >
          {currentTheme === "light" ?
            <DarkMode /> :
            <LightMode />}
        </IconButton>
      </Box>
      <Box height="100vh" display="flex">
        <Box flex="0 0 50%" p={2}>
          <ListSelector />
          <Box my={2} />
          <ListDisplayer />
          <Box my={2} />
          <PriceCalculator />
        </Box>
        <Box flex="0 0 50%" p={2}>
          <Typography variant="h4">
            Items Selected
          </Typography>
          <ItemAdder />
          <ItemList />
        </Box>
      </Box>
    </>
  )
}

export default App
