import React from "react";
import { Route, Redirect, Router } from "react-router-dom";
import { AdminLayout } from "../../Layouts";
//components

//Pages
import {
  Adminpage,
  Products,
  CreateNewProduct,
  AdminTransactionsTable
} from "../../Pages";
//css Files
import "./admin-app.css";

export const AdminApp = () => {
  return (
    <AdminLayout className="AdminAppWrapper">
      <Route path="/admin" exact component={Adminpage} />
      <Route path="/admin/products" component={Products} />
      <Route path="/admin/create-new" component={CreateNewProduct} />
      <Route path="/admin/transactions" component={AdminTransactionsTable} />
    </AdminLayout>
  );
};
