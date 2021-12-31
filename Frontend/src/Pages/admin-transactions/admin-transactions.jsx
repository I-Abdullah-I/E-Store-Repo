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

export const AdminTransactionsTable = observer(() => {
  const { authStore } = useStores();
  const { getAdminRecordsState, adminRecords, getAllAdminRecords } = authStore;

  useEffect(() => {
    const getData = () => {
      getAllAdminRecords();
      console.log("I am trying to get Data");
    };
    getData();
  }, []);

  if (getAdminRecordsState === ApiCallStates.LOADING) {
    return <CircularProgress />;
  }

  if (!adminRecords) {
    return <div style={{ marginBottom: "16px" }}>No Records</div>;
  }

  //   function getItemDetails(id){
  //     const response = await http.get(`items/item_by_ID/${id}`);
  //     console.log(response.data);
  //     return response.data;
  //   }
  //   const itemDetails = getItemDetails()

  //       }
  //   }

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
              <TableCell>Item Name</TableCell>
              <TableCell align="right">Buyer ID</TableCell>
              <TableCell align="right">Quantity</TableCell>
              <TableCell align="right">Date</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {adminRecords.my_sold_items.map(row => {
              let originalDate = new Date(row.date_created);
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
                    {row.item}
                  </TableCell>
                  <TableCell align="right">{row.buyer_id}</TableCell>
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
