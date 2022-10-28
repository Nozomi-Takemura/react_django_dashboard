    B"react-router-dom"
import { setData } from "react"
const handleDelete = (data,id) => {
    setData(data.filter(item => item.id !== id))
}
export const actionColumnModel = [
    {
        field: "action",
        headerName: "Action",
        width: 200,
        // renderCell: (params) => {
        //     return (
        //         <div className="cellAction">
        //             <Link to="/projects/test/model">
        //                 <div className="viewButton">View</div>
        //             </Link> 
        //             <div className="deleteButton" onClick={() => handleDelete(params.row.id)}>Delete</div>
        //         </div>
        //     )
        // },
        // action: () => {
        //     return (
        //         <div className="cellAction">
        //             <Link to="/projects/test/model">
        //                 <div className="viewButton">View</div>
        //             </Link> 
        //             {/* <div className="deleteButton" onClick={() => handleDelete(params.row.id)}>Delete</div> */}
        //         </div>
        //     )
        // }
    }
]

export const actionRowModel = [
    {
        action: () => {
            return (
                <div className="cellAction">
                    <Link to="/projects/test/model">
                        <div className="viewButton">View</div>
                    </Link> 
                    {/* <div className="deleteButton" onClick={() => handleDelete(params.row.id)}>Delete</div> */}
                </div>
            )
        }
    }
]