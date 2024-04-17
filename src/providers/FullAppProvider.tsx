import ColorModeProvider from "../contexts/ColorModeProvider";
import { SelectedListProvider } from "../contexts/SelectedListProvider";

/**
 * This component will inject all needed providers for the app.
 * 
 * @param props - The props for the component.
 * @param props.children - The children of the component.
 * @returns - The component.
 */
function FullAppProvider(props: { children: React.ReactNode | React.ReactNode[] }) {
    const { children } = props;

    return (
        <SelectedListProvider>
            <ColorModeProvider>
                {children}
            </ColorModeProvider>
        </SelectedListProvider>
    );
}

export default FullAppProvider;