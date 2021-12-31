import { useEffect } from "react";
import { CircularProgress } from "@material-ui/core";

import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";

import "./profile-page.css";
import { ProfileNavigator } from "../../Components/profile-navigator";
import { useStores } from "../../hooks/useStores";
import { ApiCallStates } from "../../mobx-store/types";
import { observer } from "mobx-react";

export const ProfilePage = observer(() => {
  const { authStore } = useStores();
  const { getUserData, user, getUserState, addBalance } = authStore;
  console.log("USer", user);
  useEffect(() => {
    async function getData() {
      getUserData();
    }
    getData();
  }, []);

  const handleSubmit = event => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    // eslint-disable-next-line no-console
    const formData = {
      balance: data.get("balance")
    };
    // console.log("formData", formData);
    addBalance(formData);
  };
  return (
    <div className="profile-page-wrapper">
      <ProfileNavigator userType={user.type} />
      <div className="wrapper">
        <div className="outer">
          <div className="content animated fadeInLeft">
            <span className="bg animated fadeInDown">
              {user.type === "E" ? "Customer" : "Vendor"}
            </span>
            <h1>Profile Info:</h1>
            <h2>
              <div style={{ marginLeft: "20px" }}>Name: {user.full_name}</div>
            </h2>
            <h2>
              <div style={{ marginLeft: "20px" }}> Email: {user.email}</div>
            </h2>

            <div className="button">
              <a className="cart-btn" href="#">
                <i className="cart-icon ion-bag"></i>Balance
              </a>
              <a href="#">{user.balance ? user.balance : 0}</a>

              {user.type === "E" ? (
                <div>
                  <Box
                    component="form"
                    noValidate
                    onSubmit={handleSubmit}
                    sx={{ mt: 3 }}
                  >
                    <Grid container spacing={2}>
                      <Grid item xs={6}>
                        <TextField
                          required
                          fullWidth
                          id="balance"
                          label="Amount to add"
                          name="balance"
                          autoComplete="balance"
                        />
                      </Grid>
                      <Grid item xs={6}>
                        <Button
                          type="submit"
                          fullWidth
                          variant="contained"
                          sx={{ mt: 3, mb: 2 }}
                        >
                          Save
                        </Button>
                      </Grid>
                    </Grid>
                  </Box>
                </div>
              ) : null}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
});
