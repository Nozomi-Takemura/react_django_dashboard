import React from "react"
import "./widget.scss"
import KeyboardArrowUpSharpIcon from '@mui/icons-material/KeyboardArrowUpSharp';
import PersonOutlineOutlinedIcon from "@mui/icons-material/PersonOutlineOutlined";
import AccountBalanceWalletOutlinedIcon from "@mui/icons-material/AccountBalanceWalletOutlined";
import ShoppingCartOutlinedIcon from "@mui/icons-material/ShoppingCartOutlined";
import MonetizationOnOutlinedIcon from "@mui/icons-material/MonetizationOnOutlined";
import { useContext } from 'react';
import { TopicContext } from "../context/topicContext";

const Widget = ({ type }) => {
    const { dispatch } = useContext(TopicContext);
    let data;

    //temporary
    const amount = 100;
    const diff = 100;

    switch (type) {
        case "project":
            data = {
                title: "PROJECTS",
                isMoney: false,
                link: "See all projects",
                icon:
                    <PersonOutlineOutlinedIcon
                        className="icon"
                        style={{
                            color: "crimson",
                            backgroundColor: "rgba(255,0,0,0.2)",
                        }}
                    />
            };
            break;
        case "user":
            data = {
                title: "USERS",
                isMoney: false,
                link: "See all users",
                icon:
                    <PersonOutlineOutlinedIcon
                        className="icon"
                        style={{
                            color: "crimson",
                            backgroundColor: "rgba(255,0,0,0.2)",
                        }}
                    />  
            };
            break;
        case "order":
            data = {
                title: "ORDERS",
                isMoney: false,
                link: "View all orders",
                icon: (
                    <ShoppingCartOutlinedIcon
                       className="icon"
                       style={{
                        backgroundColor: "rgba(218,165,32,0.2)",
                        color: "goldenrod",
                       }}
                    />  
                ),
            };
            break;
        case "earning":
            data = {
                title: "EARNINGS",
                isMoney: true,
                link: "View net earnings",
                icon:
                    <MonetizationOnOutlinedIcon
                        className="icon"
                        style={{ backgroundColor: "rgba(0,128,0,0.2", color: "green" }}
                    />  
            };
            break;
        case "balance":
            data = {
                title: "BALANCE",
                isMoney: true,
                link: "See details",
                icon: (
                    <AccountBalanceWalletOutlinedIcon
                        className="icon"
                        style={{
                            backgroundColor: "rgba(128,0,128,0.2)",
                            color: "purple",
                        }}
                    />
                ),
            };
            break;                                         
        default:
            break;
    }
    return (
        <div className="widget">
            <div className="left">
                <span className="title">{data.title}</span>
                <span className="counter">
                    {data.isMoney && "$"} {amount}
                </span>
                <span className="link">{data.link}</span>
            </div>
            <div className="right">
                <div className="percentage positive">
                    <KeyboardArrowUpSharpIcon />
                    {diff} %
                </div>
                {data.icon}
            </div>
        </div>

    )
}

export default Widget