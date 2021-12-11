import React, { useEffect } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import AddCircleIcon from "@mui/icons-material/AddCircle";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { observer } from "mobx-react";
import { useStores } from "../../hooks/useStores";
import { Link, useLocation } from "react-router-dom";

export const CreateNewProduct = observer(() => {
  const { authStore } = useStores();
  const { createProduct, updateProduct } = authStore;
  let location = useLocation();
  const itemData = location.data;

  const handleSubmit = event => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
    const formData = {
      name: data.get("name"),
      description: data.get("description"),
      price: data.get("price"),
      quantity: data.get("quantity")
    };
    itemData ? updateProduct(formData, itemData.id) : createProduct(formData);
  };
  return (
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center"
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <AddCircleIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          {itemData ? "Edit" : "Add"} Product
        </Typography>
        <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 3 }}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={12}>
              <TextField
                autoComplete="name"
                name="name"
                defaultValue={itemData ? itemData.name : ""}
                required
                fullWidth
                id="name"
                label="Product Name"
                autoFocus
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <TextField
                autoComplete="description"
                name="description"
                defaultValue={itemData ? itemData.description : ""}
                required
                fullWidth
                id="description"
                label="Product Describtion"
                autoFocus
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <TextField
                autoComplete="quantity"
                name="quantity"
                defaultValue={itemData ? itemData.quantity : ""}
                required
                fullWidth
                id="quantity"
                label="Stock"
                autoFocus
              />
            </Grid>
            <Grid item xs={12} sm={12}>
              <TextField
                autoComplete="price"
                name="price"
                defaultValue={itemData ? itemData.price : ""}
                required
                fullWidth
                id="price"
                label="Product Price"
                autoFocus
              />
            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            SAVE
          </Button>
        </Box>
      </Box>
    </Container>
  );
});
