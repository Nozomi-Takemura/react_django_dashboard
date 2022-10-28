import React from 'react'
import "./table.scss"
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { useState } from "react"
import { userColumnsPerProject, userRowsPerProject } from "../../../src/datatablesource.js"
import { actionColumnModel, actionRowModel } from '../../../src/actioncolumnsource.js' 
import { Link } from "react-router-dom"

const List = () => {

  const [ rows, setData ] = useState(userRowsPerProject)
  const [ cols, setDataCol ] = useState(userColumnsPerProject)
  const [ actCols, setDataActCol ] = useState(actionColumnModel)
  const [ actRows, setDataActRow ] = useState(actionRowModel)

  const removeRow = (index) => {
    setData(rows.filter((obj, ind) => index !== ind));
  }  

  return (
    <TableContainer component={Paper} className="table">
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
          {cols.concat(actCols).map((col)=> (
            <TableCell className="tableCell" key={col.field}>
              {col.field}
            </TableCell>
          ))}
          {/* <TableCell className="tableCell">{actCol.headerName}</TableCell> */}
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              {Object.keys(row).map((key) =>
                <TableCell className="tableCell" align="right"  key={key}>{row[key]}</TableCell>
              )}
              <TableCell className="tableCell" align="right">
                <div className="cellAction">
                  <Link to="/projects/test/model">
                    <div className="viewButton">View</div>
                  </Link>
                </div>
                <div className="DeleteButton" onClick={() => removeRow(row.id)}>Delete</div>
              </TableCell>

            </TableRow>
          ))}            
        </TableBody>
      </Table>
    </TableContainer>
  )
}

export default List
