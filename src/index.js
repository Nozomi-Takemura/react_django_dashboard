import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import {DarkModeContextProvider } from "./components/context/darkModeContext"
import {TopicContextProvider} from "./components/context/topicContext"

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <DarkModeContextProvider>
      <TopicContextProvider>
        <App />
      </TopicContextProvider>
    </DarkModeContextProvider>
  </React.StrictMode>
);

