import { UnAuthenticatedApp } from "../un-athenticated-app";

import React, { useEffect } from "react";
import { Router } from "react-router";
import { Route, Switch, Redirect } from "react-router-dom";
import { history } from "../../helpers";
import { useStores } from "../../hooks/useStores";

//components
import { ProtectedRoute } from "../../Components/protected-route";
// import { ApiCallStates } from "../../mobx-store/types";
//Pages
import { MarketApp, AdminApp } from "..";
import { ProfilePage } from "../../Pages";
import { observer } from "mobx-react";
import { CircularProgress } from "@material-ui/core";

export const AuthenticatedApp = observer(() => {
  const { authStore } = useStores();
  const { getUserData, user, token } = authStore;
  console.log(token);

  useEffect(() => {
    async function getData() {
      getUserData();
    }
    getData();
  }, []);

  if (!user || !token) return <CircularProgress />;

  if (user.type === "E") {
    return (
      <Switch>
        <Route path="/market" component={MarketApp} />;
        <Route path="/profile" exact component={ProfilePage} />
        <Redirect to="/" to="/market" />
      </Switch>
    );
  }
  return (
    <Switch>
      <Route path="/admin" component={AdminApp} />;
      <Route path="/profile" exact component={ProfilePage} />
      <Redirect to="/" to="/admin" />
    </Switch>
  );
});
