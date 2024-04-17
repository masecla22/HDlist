import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import FullAppProvider from './providers/FullAppProvider.tsx'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <FullAppProvider>
      <App />
    </FullAppProvider>
  </React.StrictMode>,
)
