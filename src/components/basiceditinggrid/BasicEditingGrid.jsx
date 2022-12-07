import * as React from 'react';
import { DataGrid, GridColumns, GridRowsProp } from '@mui/x-data-grid';
import {
  randomCreatedDate,
  randomTraderName,
  randomUpdatedDate,
} from '@mui/x-data-grid-generator';

import axios from "axios";
import { API_URL } from "../../constants";

export default function BasicEditingGrid() {
  return (
    <div style={{ height: 300, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        experimentalFeatures={{ newEditingApi: true }}
      />
    </div>
  );
}

const columns: GridColumns = [
  { field: 'settingname', headerName: 'Setting Name', width: 180, editable: false },
  { field: 'settingvalue', headerName: 'Setting Value', width: 180,type: 'string', editable: true },
  { field: 'owner', headerName: 'Owner', width: 180, editable: false },
  { field: 'group', headerName: 'Group', type: 'string', editable: false },
  // {
  //   field: 'dateCreated',
  //   headerName: 'Date Created',
  //   type: 'date',
  //   width: 180,
  //   editable: true,
  // },
  // {
  //   field: 'lastLogin',
  //   headerName: 'Last Login',
  //   type: 'dateTime',
  //   width: 220,
  //   editable: true,
  // },
];



axios.get(API_URL)
  .then(function (response) {
    // handle success
    console.log(API_URL);
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  //   console.log(error.response)
  })
  .then(function () {
    // always executed
  });

const rows: GridRowsProp = axios.get(API_URL)

// const rows: GridRowsProp = [
//   {
//     id: 1,
//     name: randomTraderName(),
//     age: 25,
//     dateCreated: randomCreatedDate(),
//     lastLogin: randomUpdatedDate(),
//   },
//   {
//     id: 2,
//     name: randomTraderName(),
//     age: 36,
//     dateCreated: randomCreatedDate(),
//     lastLogin: randomUpdatedDate(),
//   },
//   {
//     id: 3,
//     name: randomTraderName(),
//     age: 19,
//     dateCreated: randomCreatedDate(),
//     lastLogin: randomUpdatedDate(),
//   },
//   {
//     id: 4,
//     name: randomTraderName(),
//     age: 28,
//     dateCreated: randomCreatedDate(),
//     lastLogin: randomUpdatedDate(),
//   },
//   {
//     id: 5,
//     name: randomTraderName(),
//     age: 23,
//     dateCreated: randomCreatedDate(),
//     lastLogin: randomUpdatedDate(),
//   },
// ];