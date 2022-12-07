import React from "react"
import "./sidebar.scss"
import DashboardIcon from '@mui/icons-material/Dashboard';
import PersonOutlineOutlinedIcon from '@mui/icons-material/PersonOutlineOutlined';
import StoreMallDirectorySharpIcon from '@mui/icons-material/StoreMallDirectorySharp';
import CreditCardSharpIcon from '@mui/icons-material/CreditCardSharp';
import LocalShippingSharpIcon from '@mui/icons-material/LocalShippingSharp';
import AssessmentSharpIcon from '@mui/icons-material/AssessmentSharp';
import NotificationsNoneSharpIcon from '@mui/icons-material/NotificationsNoneSharp';
import SettingsSystemDaydreamOutlinedIcon from '@mui/icons-material/SettingsSystemDaydreamOutlined';
import PsychologyOutlinedIcon from '@mui/icons-material/PsychologyOutlined';
import SettingsApplicationsSharpIcon from '@mui/icons-material/SettingsApplicationsSharp';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import ExitToAppOutlinedIcon from '@mui/icons-material/ExitToAppOutlined';
import AccountTreeSharpIcon from '@mui/icons-material/AccountTreeSharp';
import AccountBoxSharpIcon from '@mui/icons-material/AccountBoxSharp';
import {Link} from "react-router-dom"
import { useContext } from "react" 
import { DarkModeContext } from "../context/darkModeContext";
import { TopicContext } from "../context/topicContext";

const Sidebar = () => {
    const { dispatch } = useContext(DarkModeContext)
    const { dispatchTopic } = useContext(TopicContext) 
    return (
        <div className='sidebar'>
            <div className="top">
                <Link to="/" style={{ textDecoration: "none"}}>
                    <span className="logo">Admin</span>
                </Link>
            </div>
            <hr/>
            <div className="center">
                <ul>
                    <p className="title">MAIN</p>
                        <li>
                            <DashboardIcon className="icon"/>
                            <span>Dashboard</span>
                        </li>
                    <p className="title">BenchApp</p>
                    <Link to="/benchapp/configuration" style= {{ textDecoration: "none" }}>
                        <li>
                            <DashboardIcon className="icon"/>
                            <span>Configuration</span>
                        </li>
                    </Link>
                    <p className="title">LIST</p>
                    <Link to="/ApplicationAccount" style={{ textDecoration: "none" }}>
                        <li>
                            <AccountBoxSharpIcon className="icon"/>
                            <span>ApplicationAccount</span>
                        </li>                        
                    </Link>
                    <Link to="/projects" style={{ textDecoration: "none"}}>
                        <li>
                            <AccountTreeSharpIcon className="icon"/>
                            {/* <div> */}
                                <span onClick = {() => dispatchTopic({ type: "project" })}>Projects</span>
                            {/* </div> */}

                        </li>
                    </Link>                    
                    <Link to="/users" style={{ textDecoration: "none"}}>
                        <li>
                            <PersonOutlineOutlinedIcon className="icon"/>
                            <span>Users</span>
                        </li>
                    </Link>
                    <Link to="/products" style={{ textDecoration: "none"}}>
                        <li>
                            <StoreMallDirectorySharpIcon className="icon"/>
                            <span>Products</span>
                        </li>
                    </Link>
                        <li>
                            <CreditCardSharpIcon className="icon"/>
                            <span>Orders</span>
                        </li>
                        <li>
                            <LocalShippingSharpIcon className="icon"/>
                            <span>Delivery</span>
                        </li>
                    <p className="title">USEFUL</p>
                        <li>
                            <AssessmentSharpIcon className="icon"/>
                            <span>Stats</span>
                        </li>
                        <li>
                            <NotificationsNoneSharpIcon className="icon"/>
                            <span>Notifications</span>
                        </li>
                    <p className="title">SERVICE</p>
                        <li>
                            <SettingsSystemDaydreamOutlinedIcon className="icon"/>
                            <span>System Health</span>
                        </li>
                        <li>
                            <PsychologyOutlinedIcon className="icon"/>
                            <span>Logs</span>   
                        </li>
                        <li>
                            <SettingsApplicationsSharpIcon className="icon"/>
                            <span>Settings</span>
                        </li>
                    <p className="title">USER</p>
                        <li>
                            <AccountCircleOutlinedIcon className="icon"/>
                            <span>Profile</span>
                        </li>
                        <li>
                            <ExitToAppOutlinedIcon/>
                            Logout
                        </li>
                </ul>
            </div>
            <div className="bottom">
                <div
                    className="colorOption"
                    onClick={() => dispatch({ type: "LIGHT" })}
                ></div>
                <div
                    className="colorOption"
                    onClick = {() => dispatch({ type: "DARK"})}
                ></div>
                <div className="colorOption"></div>
            </div>
        </div>
    )
}

export default Sidebar