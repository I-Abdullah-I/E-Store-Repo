import React, { useEffect } from "react";
import { Router } from "react-router";
import { Route, Switch, Redirect } from "react-router-dom";
import { history } from "../../helpers";
import { useStores } from "../../hooks/useStores";

//components
import { ProtectedRoute } from "../../Components/protected-route";
import { ApiCallStates } from "../../mobx-store/types";
//Pages
import { MarketApp, AdminApp } from "..";
import { LoginPage } from "../../Pages";
import { SignupPage, ProfilePage } from "../../Pages";
import { observer } from "mobx-react";
import { CircularProgress } from "@material-ui/core";
//css Files
import "./app.css";
import { UnAuthenticatedApp } from "../un-athenticated-app";
import { AuthenticatedApp } from "../authenticatedApp/authenticatedApp";

export const App = observer(() => {
  const { authStore } = useStores();
  const { isUserLoggedIn } = authStore;

  return (
    <div className="App">
      <Router history={history}>
        {isUserLoggedIn() ? <AuthenticatedApp /> : <UnAuthenticatedApp />}
      </Router>
    </div>
  );
});
