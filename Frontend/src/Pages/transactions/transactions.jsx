import React, { useEffect } from "react";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";

import { useStores } from "../../hooks/useStores";
import { ApiCallStates } from "../../mobx-store/types";
import { CircularProgress } from "@mui/material";
import { observer } from "mobx-react";

export const TransactionsTable = observer(() => {
  const { authStore } = useStores();
  const { getRecordsState, records, getAllRecords } = authStore;

  useEffect(() => {
    const getData = () => {
      getAllRecords();
      console.log("I am trying to get Data");
    };
    getData();
  }, []);

  if (getRecordsState === ApiCallStates.LOADING) {
    return <CircularProgress />;
  }

  if (!records) {
    return <div style={{ marginBottom: "16px" }}>No Records</div>;
  }
  console.log("hiiiiiiiiiiiiiiiiiiiiiiiiii");
  return (
    <>
      <TableContainer
        sx={{ minWidth: 900, maxWidth: 900 }}
        style={{ margin: "100px 0px 100px 200px" }}
      >
        <h1>Trasactions</h1>
        <Table aria-label="simple table" component={Paper}>
          <TableHead>
            <TableRow>
              <TableCell>Item ID</TableCell>
              <TableCell align="right">Quantity</TableCell>
              <TableCell align="right">Date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {records.map(row => {
              let originalDate = new Date(row.date_created);
              console.log("This is the original Date", originalDate);
              let formatedDate = originalDate.toLocaleString([], {
                year: "numeric",
                month: "short",
                day: "2-digit",
                hour: "2-digit",
                minute: "2-digit",
                hout12: true
              });
              return (
                <TableRow
                  key={row.item_id}
                  sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                >
                  <TableCell component="th" scope="row">
                    {row.item_id}
                  </TableCell>
                  <TableCell align="right">{row.quantity}</TableCell>
                  <TableCell align="right">{formatedDate}</TableCell>
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
});
