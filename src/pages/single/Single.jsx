import "./single.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
import Chart from "../../components/chart/Chart"
import List from "../../components/table/Table"
import { useState } from "react"

import {userRows} from "../../../src/datatablesource"

const Single = () => {
    const  [ rows, setData ] = useState(userRows)
    const row = rows[1]
    let prop;
    return(
        <div className="single">
            <Sidebar/>
            <div className="singleContainer">
                <Navbar/>
                <div className="top">
                    <div className="left">
                        <div className="editButton">EditButton</div>
                        <h1 className="title">Information</h1>
                        <div className="item">
                            {/* <img
                                src="https://images.pexels.com/photos/733872/pexels-photo-733872.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260"
                                alt=""
                                className="itemImg"
                            /> */}
                            <div className="details">
                                <h1 className="itemTitle">{row.project}</h1>
                                {/* {Object.keys(row).map((key) => 
                                    <div className="detailItem" key={key}>
                                        <span className="itemKey">{key}</span>
                                        <span className="itemValue">{row[key]}</span>
                                    </div>
                                )}                 */}
                            </div>
                        </div>
                    </div>
                    <div className="right">
                        <Chart aspect={3 / 1} title="User Spending (Last 6 Months)"/>
                    </div>
                </div>
                <div className="bottom">
                <h1 className="title">Last Transaction</h1>
                    <List/>
                </div>
            </div>
        </div>
    )
}

export default Single