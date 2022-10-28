import { createContext, useReducer } from 'react'
import TopicReducer from './topicReducer'

const INITIAL_STATE = {
    topic: "project"
}

export const TopicContext = createContext(INITIAL_STATE)

export const TopicContextProvider = ({children}) => {
    const [state, dispatch] = useReducer(TopicReducer, INITIAL_STATE)

    return (
        <TopicContext.Provider value={{ topic: state.topic, dispatch}}>
            {children}
        </TopicContext.Provider>
    );
}