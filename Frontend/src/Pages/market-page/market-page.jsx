import React, { useEffect, useState } from "react";
import { observer } from "mobx-react";
import { useStores } from "../../hooks/useStores";
import { ProductCard } from "../../Components/product-card";
import { Typography } from "@material-ui/core";
import InputBase from "@mui/material/InputBase";
import InputAdornment from "@mui/material/InputAdornment";
import { CircularProgress, TextField } from "@mui/material";
import { ApiCallStates } from "../../mobx-store/types";
import "./market-page.css";
import { styled, alpha } from "@mui/material/styles";

import SearchIcon from "@mui/icons-material/Search";
import AccountCircle from "@mui/icons-material/AccountCircle";
const Search = styled("div")(({ theme }) => ({
  position: "relative",
  borderRadius: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  "&:hover": {
    backgroundColor: alpha(theme.palette.common.white, 0.25)
  },
  marginRight: theme.spacing(2),
  marginLeft: 0,
  width: "100%",
  [theme.breakpoints.up("sm")]: {
    marginLeft: theme.spacing(3),
    width: "auto"
  }
}));

const SearchIconWrapper = styled("div")(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: "100%",
  position: "absolute",
  pointerEvents: "none",
  display: "flex",
  alignItems: "center",
  justifyContent: "center"
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: "inherit",
  "& .MuiInputBase-input": {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("md")]: {
      width: "20ch"
    }
  }
}));

export const MarketPage = observer(() => {
  const { authStore } = useStores();
  const {
    getUserData,
    user,
    getUserState,
    products,
    getAllProducts,
    getProductsState
  } = authStore;

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
    return (
      <div
        // variant="outlined"
        style={{ marginBottom: "16px" }}
        // onClick={() => history.push("/admin/create-new")}
      >
        No Products found
      </div>
    );
  }

  const handleSearch = query => {
    this.setState({ searchQuery: query, selectedGenre: null, currentPage: 1 });
  };

  const getData = () => {
    let filteredProduct = products;
    if (searchQuery)
      filteredProduct = products.filter(m =>
        m.name.toLowerCase().startsWith(searchQuery.toLowerCase())
      );
    return filteredProduct;
  };
  const filteredProduct = getData();
  console.log("SEARCHQUEIRY", searchQuery);
  return (
    <div className="products-container">
      <div
        style={{
          backgroundColor: "#fff",
          display: "flex",
          // alignItems: "center",
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

      {/* <Search>
        <SearchIconWrapper>
          <SearchIcon />
        </SearchIconWrapper>
        <StyledInputBase
          placeholder="Search…"
          inputProps={{ "aria-label": "search" }}
        />
      </Search> */}
      <h1 className="products-title">Our Products</h1>
      <div className="products-wrapper">
        {filteredProduct.map(product => {
          return (
            <ProductCard
              title={product.name}
              price={product.price}
              disc={product.description}
              id={product.id}
            />
          );
        })}
      </div>
    </div>
  );
  // else return "no permission";
});
