import React, { useEffect, useState } from "react";
import { history } from "../../../helpers";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import Button from "@mui/material/Button";
import { useStores } from "../../../hooks/useStores";
import { ApiCallStates } from "../../../mobx-store/types";
import { CircularProgress } from "@mui/material";
import { observer } from "mobx-react";
import { Link } from "react-router-dom";

export const ProductsTable = observer(() => {
  const [filter, setFilter] = useState(false);
  const { authStore } = useStores();
  const {
    getProductsState,
    products,
    getAllProducts,
    deleteProduct
  } = authStore;

  useEffect(() => {
    const getData = () => {
      getAllProducts();
      console.log("I am trying to get Data");
    };
    getData();
  }, []);

  if (getProductsState === ApiCallStates.LOADING) {
    return <CircularProgress />;
  }

  if (!products) {
    return (
      <Button
        variant={"outlined"}
        style={{ marginBottom: "16px" }}
        onClick={() => history.push("/admin/create-new")}
      >
        Add Product
      </Button>
    );
  }

  const filteredProducts = products.filter(product => {
    return product.quantity !== 0;
  });

  const displayedProducts = filter ? filteredProducts : products;
  console.log("filteredRecords", filteredProducts);
  return (
    <>
      <Button
        variant="outlined"
        style={{ marginBottom: "16px" }}
        onClick={() => history.push("/admin/create-new")}
      >
        Add Product
      </Button>
      <Button
        variant={filter ? "contained" : "outlined"}
        style={{ marginLeft: "16px", marginBottom: "16px" }}
        onClick={() => setFilter(!filter)}
      >
        Items in stock
      </Button>
      <TableContainer component={Paper}>
        <Table sx={{ minWidth: 650 }} aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
              <TableCell align="right">Description</TableCell>
              <TableCell align="right">Quantity</TableCell>
              <TableCell align="right">Price</TableCell>
              <TableCell align="right">Action</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {displayedProducts.map(row => (
              <TableRow
                key={row.name}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell component="th" scope="row">
                  {row.name}
                </TableCell>
                <TableCell align="right">{row.description}</TableCell>
                <TableCell align="right">{row.quantity}</TableCell>
                <TableCell align="right">{row.price}</TableCell>
                <TableCell align="right">
                  <Link
                    to={{
                      pathname: "/admin/create-new",
                      data: row
                    }}
                  >
                    <Button variant="contained">Edit</Button>
                  </Link>
                  <Button
                    variant="contained"
                    color="error"
                    onClick={() => deleteProduct(row.id)}
                    style={{ marginLeft: "8px" }}
                  >
                    Delete
                  </Button>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
});
