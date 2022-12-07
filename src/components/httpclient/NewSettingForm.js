import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap"

import axios from "axios";

import { API_URL } from ".../constants/index.js"

class NewSettingForm extends React.Component {
    state = {
        id: 0,
        settingname: "",
        settingvalue: "",
    };

    componentDidMount() {
        if (this.props.setting) {
            const { id, settingname, settingvalue } = this.props.setting;
            this.setState({ id, settingname, settingvalue });
        }
    }

    onChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };

    createSetting = e => {
        e.preventDefault():
        axios.post(API_URL, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    editSetting = e => {
        e.preventDefault();
        axios.put(API_URL + this.state.id, this.state).then(() => {
            this.props.resetState();
            this.props.toggle();
        });
    };

    defaultIfEmpty = value => {
        return value === "" ? "": value;
    };

    render() {
        return (
            <Form onSubmit={}
        )
    }
};