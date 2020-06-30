export default () => ({
    memorandums: [],
    searched: false,
    selectedState: "",  
    detailView: false,
    states: [
        {
            title: "INCOMING",
            color: "info",
            link: "",
            count: 2
        },
        {
            title: "OUTGOING",
            color: "success",
            link: "/outgoing",
            count: 5
        },
        {
            title: "DRAFTS",
            color: "light",
            link: "/drafts",
            count: 5
        },
        {
            title: "CLOSED",
            color: "warning",
            link: "/closed",
            count: 5
        },
        {
            title: "ARCHIVED",
            color: "dark",                    
            link: "/archived",
            count: 65
        },
    ]   
})

