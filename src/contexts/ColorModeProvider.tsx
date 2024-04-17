import { ThemeProvider } from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';
import { createContext, useMemo, useState } from "react";
import darkTheme from '../themes/darkTheme';
import lightTheme from '../themes/lightTheme';

/**
 * This is the context type for the ColorModeContext.
 */
const ColorModeContext = createContext({
    toggleColorMode: () => { },
    currentTheme: 'dark'
});

const themeRegistry = {
    'dark': darkTheme,
    'light': lightTheme
};

/**
 * This component provides the ColorModeContext.
 * 
 * @param props - The props for the component.
 * @returns - The component
 */
function ColorModeProvider(props: { children: React.ReactNode }) {
    const [mode, setMode] = useState<'light' | 'dark'>(
        localStorage.getItem('colorMode') === 'dark' ? 'dark' : 'light'
    );

    const colorMode = useMemo(
        () => ({
            toggleColorMode: () => {
                setMode((prevMode) => {
                    const updatedMode = prevMode === 'light' ? 'dark' : 'light';
                    localStorage.setItem('colorMode', updatedMode);
                    return updatedMode;
                });
            },
        }),
        [],
    );

    const theme = useMemo(() => themeRegistry[mode], [mode]);

    return <ColorModeContext.Provider value={{ ...colorMode, currentTheme: mode }}>
        <ThemeProvider theme={theme}>
            <CssBaseline />
            {props.children}
        </ThemeProvider>
    </ColorModeContext.Provider>;
}

export default ColorModeProvider;
export { ColorModeContext };