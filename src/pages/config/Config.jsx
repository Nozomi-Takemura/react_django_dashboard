import "./config.scss"
import Sidebar from "../../components/sidebar/Sidebar"
import Navbar from "../../components/navbar/Navbar"
import Chart from "../../components/chart/Chart"
import List from "../../components/table/Table"
import Setting from "../../components/setting/Setting" 
import { useState } from "react"

import {userRows} from "../../../src/datatablesource"
import {Outlet} from "react-router-dom"

const Config = () => {
    const  [ rows, setData ] = useState(userRows)
    const row = rows[1]
    let prop;
    return(
        <div className="single">
            <div className="single1">
            <Setting/>
            </div>
            <div id="detail">
                <Outlet />
            </div>
        </div>
    )

}

export default Config