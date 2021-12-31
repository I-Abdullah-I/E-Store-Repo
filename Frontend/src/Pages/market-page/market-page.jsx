import React, { useEffect, useState } from "react";
import { observer } from "mobx-react";
import { useStores } from "../../hooks/useStores";
import { ProductCard } from "../../Components/product-card";
import InputAdornment from "@mui/material/InputAdornment";
import { CircularProgress, TextField } from "@mui/material";
import { ApiCallStates } from "../../mobx-store/types";
import "./market-page.css";

import SearchIcon from "@mui/icons-material/Search";

export const MarketPage = observer(() => {
  const { authStore } = useStores();
  const { products, getAllProducts, getProductsState } = authStore;

  const [searchQuery, setSearchQuery] = useState("");
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
    return <div style={{ marginBottom: "16px" }}>No Products found</div>;
  }

  const prepareProductsList = () => {
    let filteredProduct = products.filter(m => m.quantity > 0);

    if (searchQuery)
      filteredProduct = products.filter(m =>
        m.name.toLowerCase().startsWith(searchQuery.toLowerCase())
      );
    return filteredProduct;
  };
  const filteredProduct = prepareProductsList();
  return (
    <div className="products-container">
      <div
        style={{
          backgroundColor: "#fff",
          display: "flex",
          flexDirection: "column",
          margin: "0 200px"
        }}
      >
        <TextField
          id="input-with-icon-textfield"
          label="Search"
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchIcon />
              </InputAdornment>
            )
          }}
          value={searchQuery}
          onChange={e => setSearchQuery(e.target.value)}
          variant="filled"
        />
      </div>

      <h1 className="products-title">Our Products</h1>
      <div className="products-wrapper">
        {filteredProduct.map(product => {
          return (
            <ProductCard
              title={product.name}
              price={product.price}
              disc={product.description}
              id={product.id}
              quantity={product.quantity}
            />
          );
        })}
      </div>
    </div>
  );
  // else return "no permission";
});
