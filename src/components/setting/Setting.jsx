import React from "react"
import "./setting.scss"
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

const Setting = () => {
    return (
        <div className='sidebar'>
            {/* <hr/> */}
            <div className="center">
                <ul>
                    <p className="title">BenchMarking</p>
                    <Link to="./scheme" style= {{ textDecoration: "none" }}>
                        <li>
                            <DashboardIcon className="icon"/>
                            <span>Scheme</span>
                        </li>
                    </Link>
                    {/* <p className="title">BenchApp</p> */}
                    <Link to="./data" style= {{ textDecoration: "none" }}>
                        <li>
                            <DashboardIcon className="icon"/>
                            <span>Data</span>
                        </li>
                    </Link>
                    {/* <p className="title">LIST</p> */}
                    <Link to="./files" style={{ textDecoration: "none" }}>
                        <li>
                            <AccountBoxSharpIcon className="icon"/>
                            <span>Files</span>
                        </li>                        
                    </Link>
                    <Link to="./settings" style={{ textDecoration: "none"}}>
                        <li>
                            <PersonOutlineOutlinedIcon className="icon"/>
                            <span>Settings</span>
                        </li>
                    </Link>
                </ul>
            </div>
        </div>
    )
}

export default Setting