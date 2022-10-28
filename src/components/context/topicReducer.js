const TopicReducer = (state, action) => {
    switch (action.type) {
        case "Project":{
            return {
                topic: "Project",
            };
        }
        case "User":{
            return {
                topic: "User"
            };
        }
        default:
            return state;
    }
}

export default TopicReducer;