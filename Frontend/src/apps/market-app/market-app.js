import React from "react";
import { Router, Route, Switch, Redirect } from "react-router-dom";
import { MarketLayout } from "../../Layouts";

//components
//Pages
import { MarketPage, TransactionsTable } from "../../Pages";
//css Files
import "./market-app.css";

export const MarketApp = () => {
  return (
    <MarketLayout className="marketAppWrapper">
      <Route path="/market" exact component={MarketPage} />
      <Route path="/market/transactions" component={TransactionsTable} />
    </MarketLayout>
  );
};
