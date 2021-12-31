import React from "react";
import { Route, Redirect, Router, Switch } from "react-router-dom";
import { AdminLayout } from "../../Layouts";
//components

//Pages
import {
  Products,
  CreateNewProduct,
  AdminTransactionsTable
} from "../../Pages";
//css Files
import "./admin-app.css";

export const AdminApp = () => {
  return (
    <AdminLayout className="AdminAppWrapper">
      <Switch>
        <Route path="/admin/products" exact component={Products} />
        <Route path="/admin/create-new" exact component={CreateNewProduct} />
        <Route
          path="/admin/transactions"
          exact
          component={AdminTransactionsTable}
        />
        <Redirect to="/admin" to="/admin/products" />
      </Switch>
    </AdminLayout>
  );
};
